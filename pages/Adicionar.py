import streamlit as st
import pandas as pd
import funcoes as f
from datetime import datetime
from time import sleep

# Conectar ao banco de dados
with open('conexao.txt', 'r') as file:
    user = file.readline().strip()
    password = file.readline().strip()
    host = file.readline().strip()
    porta = file.readline().strip()

banco_de_dados = f.database(user, password, host, porta)
conexao, cursor = banco_de_dados.conectar()

# Funções para obter dados do banco
def selectDiretores():
    cursor.execute("SELECT * FROM diretor")
    diretores = cursor.fetchall()
    return pd.DataFrame(diretores, columns=[desc[0] for desc in cursor.description])

def getCategorias():
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    return pd.DataFrame(categorias, columns=[desc[0] for desc in cursor.description])

def obter_filmes(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT num_filme, titulo_original FROM filme")
        filmes = cursor.fetchall()
    return filmes

def obter_canais(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT num_canal, nome FROM canal")
        canais = cursor.fetchall()
    return canais

def adicionar_filme(conexao):
    st.title("Adicionar Filme 🎥")
    
    # Carregar a lista de diretores e categorias
    diretores_list = selectDiretores()  # Função que busca diretores no banco de dados
    categorias_list = getCategorias()  # Função que busca categorias no banco de dados

    with st.form('adicionar_filme'):
        titulo_original = st.text_input('Título Original', max_chars=80)
        titulo_brasil = st.text_input('Título no Brasil (opcional)', max_chars=80)
        ano_lancamento = st.number_input('Ano de Lançamento', min_value=1800, max_value=2024, step=1)
        poster_url = st.text_input('URL do Poster (opcional)', max_chars=500)
        pais_origem = st.text_input('País de Origem', max_chars=30)
        duracao = st.number_input('Duração (em minutos)', min_value=1, step=1)
        diretor_nome = st.selectbox('Diretor', diretores_list['nome_diretor'])
        id_diretor = int(diretores_list[diretores_list['nome_diretor'] == diretor_nome]['id_diretor'].values[0])
        categoria = st.multiselect('Categoria', categorias_list['nome_categoria'])
        id_categoria = categorias_list[categorias_list['nome_categoria'].isin(categoria)]['id_categoria'].values
        id_categoria = [int(cat) for cat in id_categoria]
        class_indicativa = st.text_input('Classificação Indicativa', max_chars=5)
        sinopse = st.text_input('Sinopse do Filme', max_chars=500)
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        cursor = conexao.cursor()
        query_filme = """
        INSERT INTO filme (titulo_original, titulo_brasil, ano_lancamento, poster_url, pas_origem, duracao, id_diretor, class_indicativo, sinopse)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores_filme = (titulo_original, titulo_brasil, ano_lancamento, poster_url, pais_origem, duracao, id_diretor, class_indicativa, sinopse)
        cursor.execute(query_filme, valores_filme)

        num_filme = cursor.lastrowid
        for cat_id in id_categoria:
            query_categoria_filme = """
            INSERT INTO categorias_filmes (num_filme, id_categoria)
            VALUES (%s, %s)
            """
            cursor.execute(query_categoria_filme, (num_filme, cat_id))

        conexao.commit()
        cursor.close()
        st.success('Filme cadastrado com sucesso!')
        sleep(3)
        st.rerun()


    st.title("Adicionar Novo Diretor 🎬")

    with st.form('adicionar_diretor'):
        novo_diretor = st.text_input("Nome do Diretor", max_chars=40)
        submit_diretor = st.form_submit_button("Adicionar Diretor")

    if submit_diretor:
        if novo_diretor:
            cursor = conexao.cursor()
            query_novo_diretor = "INSERT INTO diretor (nome_diretor) VALUES (%s)"
            cursor.execute(query_novo_diretor, (novo_diretor,))
            conexao.commit()
            cursor.close()

            st.rerun()  
            st.success("Novo diretor adicionado com sucesso!")
               
        else:
            st.error("Por favor, insira o nome do diretor.")
     
    

def selectFilmes():
    cursor.execute("SELECT * FROM filme")
    filmes = cursor.fetchall()
    return pd.DataFrame(filmes, columns=[desc[0] for desc in cursor.description])

def adicionar_exibicao(conexao):
    st.title("Adicionar Exibição 📅")
    filme_list = selectFilmes()

    filmes = obter_filmes(conexao)
    filmes_dict = {titulo: num_filme for num_filme, titulo in filmes}
    canais = obter_canais(conexao)
    canais_dict = {nome: num_canal for num_canal, nome in canais}
    
    with st.form('adicionar_filme'):
        filme_nome = st.selectbox('Filme', filme_list['titulo_brasil'])
        canal_selecionado = st.selectbox("Selecione um Canal", list(canais_dict.keys()))
        data_exibicao = st.date_input("Data de Exibição", format='DD/MM/YYYY')
        hora_exibicao = st.time_input("Hora de Exibição")

        submit_button = st.form_submit_button("Adicionar Exibicão")

    if submit_button:
        if filme_nome and canal_selecionado and data_exibicao and hora_exibicao:
            num_filme = int(filme_list [filme_list['titulo_brasil'] == filme_nome]['num_filme'].values[0]) 
            num_canal = canais_dict[canal_selecionado]
            data_hora_exibicao = datetime.combine(data_exibicao, hora_exibicao)

            if submit_button:
                cursor = conexao.cursor()

                query_filme = """
                INSERT INTO exibicao (num_filme,num_canal,data_exibicao)
                VALUES (%s, %s, %s)
                """
                valores_filme = (num_filme, num_canal, data_hora_exibicao)
                cursor.execute(query_filme, valores_filme)

                num_filme = cursor.lastrowid

                conexao.commit()
                cursor.close()
                st.success('Cadastro de exibição concluido!')
                sleep(3)
                st.rerun()
         
# Página principal com seleção
def main():
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox("Escolha a opção", ["Adicionar Filme / Diretor", "Adicionar Exibição"])

    if option == "Adicionar Filme / Diretor":
        adicionar_filme(conexao)
    elif option == "Adicionar Exibição":
        adicionar_exibicao(conexao)
if __name__ == "__main__":
    main()
