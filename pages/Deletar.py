import streamlit as st
import funcoes as f
from time import sleep

with open('conexao.txt', 'r') as file:
    user = file.readline().strip()
    password = file.readline().strip()
    host = file.readline().strip()
    porta = file.readline().strip()

banco_de_dados = f.database(user, password, host, porta)
conexao, cursor = banco_de_dados.conectar()

def buscar_filmes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT num_filme, titulo_original, ano_lancamento FROM filme")
    filmes = cursor.fetchall()
    cursor.close()
    return filmes

def deletar_filme(conexao):
    st.header("Deletar Filme 🎥")

    filmes = buscar_filmes(conexao)

    if not filmes:
        st.warning("Nenhum filme encontrado no banco de dados.")
        return

    opcoes_filmes = {f"{titulo} ({ano})": num for num, titulo, ano in filmes}
    filme_escolhido = st.selectbox('Selecione o filme', list(opcoes_filmes.keys()))
    num_filme_selecionado = opcoes_filmes[filme_escolhido]

    if st.button("Deletar Filme"):
        cursor = conexao.cursor()

        query_exibicao = "DELETE FROM exibicao WHERE num_filme = %s"
        cursor.execute(query_exibicao, (num_filme_selecionado,))

        query_filme = "DELETE FROM filme WHERE num_filme = %s"
        cursor.execute(query_filme, (num_filme_selecionado,))

        conexao.commit()
        cursor.close()
        st.success(f'Filme "{filme_escolhido}" deletado com sucesso!')
        sleep(3)
        st.rerun()

def deletar_exibicao(conexao):
    st.header("Deletar Exibição 🎞️")

    filmes = buscar_filmes(conexao)

    if not filmes:
        st.warning("Nenhum filme encontrado no banco de dados.")
        return

    opcoes_filmes = {f"{titulo} ({ano})": num for num, titulo, ano in filmes}
    filme_escolhido = st.selectbox('Selecione o filme', list(opcoes_filmes.keys()))
    num_filme_selecionado = opcoes_filmes[filme_escolhido]

    cursor = conexao.cursor()
    cursor.execute("SELECT num_canal, data_exibicao FROM exibicao WHERE num_filme = %s", (num_filme_selecionado,))
    exibicoes = cursor.fetchall()
    cursor.close()

    if not exibicoes:
        st.warning("Nenhuma exibição encontrada para este filme.")
        return

    # Formatar as datas para o formato DD/MM/YYYY
    opcoes_exibicoes = {
        f"Canal: {canal} | Data: {data.strftime('%d/%m/%Y')}": (canal, data)
        for canal, data in exibicoes
    }

    exibicao_escolhida = st.selectbox('Selecione a exibição que deseja deletar', list(opcoes_exibicoes.keys()))
    canal_exibicao_selecionado, data_exibicao_selecionada = opcoes_exibicoes[exibicao_escolhida]

    if st.button("Deletar Exibição"):
        cursor = conexao.cursor()
        query_exibicao = "DELETE FROM exibicao WHERE num_filme = %s AND num_canal = %s AND data_exibicao = %s"
        cursor.execute(query_exibicao, (num_filme_selecionado, canal_exibicao_selecionado, data_exibicao_selecionada))

        conexao.commit()
        cursor.close()
        st.success(f'Exibição no canal {canal_exibicao_selecionado} na data {data_exibicao_selecionada.strftime("%d/%m/%Y")} deletada com sucesso!')
        sleep(3)
        st.rerun()
pagina = st.sidebar.selectbox("Escolha a página", ["Deletar Filme", "Deletar Exibição"])

if pagina == "Deletar Filme":
    deletar_filme(conexao)
elif pagina == "Deletar Exibição":
    deletar_exibicao(conexao)