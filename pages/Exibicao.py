import streamlit as st
import funcoes as f
from datetime import datetime

with open('conexao.txt', 'r') as file:
    user = file.readline().strip()
    password = file.readline().strip()
    host = file.readline().strip()
    porta = file.readline().strip()

# Cria a conexão e o cursor usando o módulo funcoes
banco_de_dados = f.database(user, password, host, porta)
conexao, _ = banco_de_dados.conectar()

# Função para obter os filmes existentes no banco de dados
def obter_filmes(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT num_filme, titulo_original FROM filme")
        filmes = cursor.fetchall()
    return filmes

# Função para obter os canais do banco de dados
def obter_canais(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT num_canal, nome FROM canal")
        canais = cursor.fetchall()
    return canais

# Função para adicionar um filme a um canal
def adicionar_exibicao(conexao, num_filme, num_canal, data_exibicao):
    with conexao.cursor() as cursor:
        query = """
        INSERT INTO exibicao (num_filme, num_canal, data_exibicao)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (num_filme, num_canal, data_exibicao))
        conexao.commit()

# Página Streamlit
def exibir(conexao):
    st.title("Adicionar Filme a Canal")
    
    # Seleção de filme existente
    filmes = obter_filmes(conexao)
    filmes_dict = {titulo: num_filme for num_filme, titulo in filmes}
    filme_selecionado = st.selectbox("Selecione um Filme", list(filmes_dict.keys()))
    
    # Seleção de canal
    canais = obter_canais(conexao)
    canais_dict = {nome: num_canal for num_canal, nome in canais}
    canal_selecionado = st.selectbox("Selecione um Canal", list(canais_dict.keys()))
    
    # Data e hora de exibição
    data_exibicao = st.date_input("Data de Exibição")
    hora_exibicao = st.time_input("Hora de Exibição")
    
    if st.button("Adicionar Exibição"):
        if filme_selecionado and canal_selecionado and data_exibicao and hora_exibicao:
            num_filme = filmes_dict[filme_selecionado]
            num_canal = canais_dict[canal_selecionado]
            
            # Combina data e hora em um único datetime
            data_hora_exibicao = datetime.combine(data_exibicao, hora_exibicao)
            
            adicionar_exibicao(conexao, num_filme, num_canal, data_hora_exibicao)
            st.success(f"Filme '{filme_selecionado}' adicionado ao canal '{canal_selecionado}' com sucesso!")
        else:
            st.error("Por favor, selecione um filme, um canal, uma data e uma hora de exibição.")

# Chama a função exibir com conexão como argumento
exibir(conexao)