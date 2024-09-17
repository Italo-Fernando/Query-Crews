# import streamlit as st
# from main import db_manager  # Certifique-se de que o nome do arquivo está correto
# from home import getConexaoCursor

# conexao, cursor = getConexaoCursor()
# # Função para deletar filme
# def deletar_filme(conexao):
#     st.header("Deletar Filme")

#     # Buscar os filmes disponíveis no banco de dados
#     cursor = conexao.cursor()
#     cursor.execute("SELECT num_filme, titulo_original, ano_lancamento FROM filme")
#     filmes = cursor.fetchall()  # Retorna uma lista de tuplas (num_filme, titulo_original, ano_lancamento)
#     cursor.close()

#     # Se não houver filmes disponíveis
#     if not filmes:
#         st.warning("Nenhum filme encontrado no banco de dados.")
#         return

#     # Cria uma lista de opções com os títulos dos filmes, número do filme e ano de lançamento
#     opcoes_filmes = {f"{titulo} ({ano}) [ID: {num}]": num for num, titulo, ano in filmes}

#     # Selectbox para o usuário escolher o filme a ser deletado
#     filme_escolhido = st.selectbox('Selecione o filme que deseja deletar', list(opcoes_filmes.keys()))

#     # Pegando o número do filme selecionado
#     num_filme_selecionado = opcoes_filmes[filme_escolhido]

#     # Botão para deletar o filme
#     if st.button("Deletar"):
#         cursor = conexao.cursor()

#         # Deletar todas as exibições relacionadas a esse filme primeiro
#         query_exibicao = "DELETE FROM exibicao WHERE num_filme = %s"
#         cursor.execute(query_exibicao, (num_filme_selecionado,))

#         # Agora deletar o filme da tabela 'filme'
#         query_filme = "DELETE FROM filme WHERE num_filme = %s"
#         cursor.execute(query_filme, (num_filme_selecionado,))

#         # Confirmar as alterações no banco
#         conexao.commit()
#         cursor.close()

#         # Mensagem de sucesso
#         st.success(f'Filme "{filme_escolhido}" deletado com sucesso!')

# if conexao and cursor:
#     deletar_filme(conexao)