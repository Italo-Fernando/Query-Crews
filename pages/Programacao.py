import streamlit as st
import funcoes as f
from time import sleep

# Conectar ao banco de dados
with open('conexao.txt', 'r') as file:
    user = file.readline().strip()
    password = file.readline().strip()
    host = file.readline().strip()
    porta = file.readline().strip()

banco_de_dados = f.database(user, password, host, porta)
conexao, cursor = banco_de_dados.conectar()

# Função para buscar filmes do banco de dados
def buscar_filmes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT num_filme, titulo_original, ano_lancamento FROM filme")
    filmes = cursor.fetchall()
    cursor.close()
    return filmes

# Menu principal da tela de programação
def main():
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox("Escolha a opção", ["Atualizar Filme", "Atualizar Exibição"])

    if option == "Atualizar Filme":
        st.header("Atualizar Filme 🎥")
        filmes = buscar_filmes(conexao)

        if not filmes:
            st.warning("Nenhum filme encontrado no banco de dados.")
            return

        # Menu dropdown para selecionar o filme
        opcoes_filmes = {f"{titulo} ({ano})": num for num, titulo, ano in filmes}
        filme_escolhido = st.selectbox('Selecione o filme para atualizar', list(opcoes_filmes.keys()))

        st.write(f'Filme selecionado: {filme_escolhido}')

    elif option == "Atualizar Exibição":
        st.header("Atualizar Exibição 🎞️")
        st.write("Essa parte ainda está em desenvolvimento...")

if __name__ == "__main__":
    main()
