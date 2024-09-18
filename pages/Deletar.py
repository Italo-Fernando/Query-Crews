import streamlit as st
import funcoes as f

with open('conexao.txt', 'r') as file:
    user = file.readline().strip()
    password = file.readline().strip()
    host = file.readline().strip()
    porta = file.readline().strip()

# Estabelecer conexão com o banco de dados
banco_de_dados = f.database(user, password, host, porta)
conexao, cursor = banco_de_dados.conectar()

# Função para deletar filme
def deletar_filme(conexao):
    st.header("Deletar Filme")

    # Buscar os filmes disponíveis no banco de dados
    cursor = conexao.cursor()
    cursor.execute("SELECT num_filme, titulo_original, ano_lancamento FROM filme")
    filmes = cursor.fetchall()  # Retorna uma lista de tuplas (num_filme, titulo_original, ano_lancamento)
    cursor.close()

    # Se não houver filmes disponíveis
    if not filmes:
        st.warning("Nenhum filme encontrado no banco de dados.")
        return

    # Cria uma lista de opções com os títulos dos filmes, número do filme e ano de lançamento
    opcoes_filmes = {f"{titulo} ({ano}) [ID: {num}]": num for num, titulo, ano in filmes}

    # Selectbox para o usuário escolher o filme a ser deletado
    filme_escolhido = st.selectbox('Selecione o filme que deseja deletar', list(opcoes_filmes.keys()))

    # Pegando o número do filme selecionado
    num_filme_selecionado = opcoes_filmes[filme_escolhido]

    # Botão para deletar o filme
    if st.button("Deletar"):
        cursor = conexao.cursor()

        # Deletar todas as exibições relacionadas a esse filme primeiro
        query_exibicao = "DELETE FROM exibicao WHERE num_filme = %s"
        cursor.execute(query_exibicao, (num_filme_selecionado,))

        # Agora deletar o filme da tabela 'filme'
        query_filme = "DELETE FROM filme WHERE num_filme = %s"
        cursor.execute(query_filme, (num_filme_selecionado,))

        # Confirmar as alterações no banco
        conexao.commit()
        cursor.close()

        # Mensagem de sucesso
        st.success(f'Filme "{filme_escolhido}" deletado com sucesso!')

# Verificar se a conexão está ativa e se o cursor foi criado corretamente
deletar_filme(conexao)