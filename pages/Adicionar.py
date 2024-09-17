import streamlit as st
import pandas as pd
import funcoes as f


with open('conexao.txt', 'r') as file:
    user = file.readline().strip()
    password = file.readline().strip()
    host = file.readline().strip()
    porta = file.readline().strip()

banco_de_dados = f.database(user, password, host, porta)
conexao, cursor = banco_de_dados.conectar()
# conexao , cursor = banco_de_dados.conexao, banco_de_dados.cursor

# # Obtenha a conexão e o cursor
# conexao, cursor = getConexaoCursor()

# # Função para buscar diretores e retornar a lista em DataFrame
def selectDiretores():
     cursor.execute("SELECT * FROM diretor")
     diretores = cursor.fetchall()
     diretores_list = pd.DataFrame(diretores, columns=[desc[0] for desc in cursor.description])
     return diretores_list

def getCategorias():
    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    categorias_list = pd.DataFrame(categorias, columns=[desc[0] for desc in cursor.description])
    return categorias_list

# Função para adicionar filme e vincular a um canal
def adicionar_filme(conexao):
    st.header("Adicionar Filme e Exibição")

    # Buscar diretores e categorias
    diretores_list = selectDiretores()
    categorias_list = getCategorias()
    
#     # Formulário para inserção de filme
    with st.form('adicionar_filme'):
        titulo_original = st.text_input('Título Original', max_chars=80)
        titulo_brasil = st.text_input('Título no Brasil (opcional)', max_chars=80)
        ano_lancamento = st.number_input('Ano de Lançamento', min_value=1800, max_value=2024, step=1)
        poster_url = st.text_input('URL do Poster (opcional)', max_chars=255)
        pais_origem = st.text_input('País de Origem', max_chars=30)
        duracao = st.number_input('Duração (em minutos)', min_value=1, step=1)
        diretor_nome = st.selectbox('Diretor', diretores_list['nome_diretor'])
        id_diretor = int(diretores_list[diretores_list['nome_diretor'] == diretor_nome]['id_diretor'].values[0])  # Converter para int
        categoria = st.multiselect('Categoria', categorias_list['nome_categoria'])
        id_categoria = categorias_list[categorias_list['nome_categoria'].isin(categoria)]['id_categoria'].values
        id_categoria = [int(cat) for cat in id_categoria]  # Converter todos os valores para int
        class_indicativa = st.text_input('Classificação Indicativa', max_chars=5)
        
        # Botão de submissão
        submit_button = st.form_submit_button("Submit")

    # Se o botão for clicado, insere os dados no banco
    if submit_button:
        cursor = conexao.cursor()

        # Inserir na tabela 'filme' sem especificar num_filme (será gerado automaticamente)
        query_filme = """
        INSERT INTO filme (titulo_original, titulo_brasil, ano_lancamento, poster_url, pas_origem, duracao, id_diretor, class_indicativo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores_filme = (titulo_original, titulo_brasil, ano_lancamento, poster_url, pais_origem, duracao, id_diretor, class_indicativa)
        cursor.execute(query_filme, valores_filme)
        
        # Obter o ID do último filme inserido
        num_filme = cursor.lastrowid

        # Inserir categorias para o filme
        for cat_id in id_categoria:
            query_categoria_filme = """
            INSERT INTO categorias_filmes (num_filme, id_categoria)
            VALUES (%s, %s)
            """
            cursor.execute(query_categoria_filme, (num_filme, cat_id))

        conexao.commit()
        cursor.close()

        st.success('Filme e exibição cadastrados com sucesso!') 

# Verifique se há uma conexão válida e chame a função de adicionar filme

adicionar_filme(conexao)