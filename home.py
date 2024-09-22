# Importar o Streamlit e outros módulos necessários
import streamlit as st
import pandas as pd
from components.components import card_component
import funcoes as f
import os

# Função para selecionar filmes com base na categoria
def select_filmes_por_categoria(categoria):
    conexao, cursor = banco_de_dados.conectar()
    
    if categoria == "Todos":
        query = """
        SELECT f.*, c.logo_canal, e.data_exibicao 
        FROM exibicao e
        NATURAL LEFT JOIN filme f
        NATURAL LEFT JOIN canal c
        """
    else:
        query = f"""
        SELECT f.*, c.logo_canal, e.data_exibicao 
        FROM filme f
        NATURAL LEFT JOIN canal c
        NATURAL JOIN categorias_filmes 
        NATURAL JOIN categoria 
        NATURAL JOIN exibicao e 
        WHERE categoria.nome_categoria = '{categoria}'
        """
    
    cursor.execute(query)
    filmes = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(filmes, columns=[desc[0] for desc in cursor.description])
    return df

# Função para exibir os filmes
# Função para exibir os filmes
def mostrar_filmes(filmes_df, title):
    cards = [
        {
            "title": filme['titulo_brasil'],
            "description": filme['sinopse'],
            "logo_url": filme['logo_canal'],
            "logo_caption": filme['data_exibicao'], 
            "background_image": filme['poster_url']
        }
        for _, filme in filmes_df.iterrows()
    ]

    st.subheader(title)

    if len(cards) > 1:
        # Se houver mais de um filme, o slider é exibido
        item_selecionado = st.slider(f'{title}', 0, len(cards) - 2, len(cards) - 1)
    else:
        # Se houver apenas um filme, não exibe o slider e seleciona o primeiro item
        st.write("Não há filmes suficientes para exibir no slider.")
        item_selecionado = 0

    col1, col2 = st.columns(2)
    
    # Exibe o primeiro card
    with col1:
        card_component(
            title=cards[item_selecionado]["title"],
            description=cards[item_selecionado]["description"],
            logo_url=cards[item_selecionado]["logo_url"],
            logo_caption=cards[item_selecionado]["logo_caption"],
            background_image=cards[item_selecionado]["background_image"],
            unique_id=f"card1_{item_selecionado}"  # Adicionando um identificador único
        )
    
    # Exibe o segundo card, se houver
    with col2:
        if item_selecionado + 1 < len(cards):
            card_component(
                title=cards[item_selecionado + 1]["title"],
                description=cards[item_selecionado + 1]["description"],
                logo_url=cards[item_selecionado + 1]["logo_url"],
                logo_caption=cards[item_selecionado + 1]["logo_caption"],
                background_image=cards[item_selecionado + 1]["background_image"],
                unique_id=f"card2_{item_selecionado + 1}"  # Adicionando um identificador único
            )


def get_categorias_filmes():
    conexao, cursor = banco_de_dados.conectar()
    
    query = """
    SELECT DISTINCT c.nome_categoria
    FROM categoria c
    JOIN categorias_filmes cf ON c.id_categoria = cf.id_categoria
    JOIN exibicao e ON cf.num_filme = e.num_filme
    """
    
    cursor.execute(query)
    categorias = cursor.fetchall()
    cursor.close()

    # Transforma a lista de tuplas em uma lista simples
    categorias = [categoria[0] for categoria in categorias]

    # Adiciona a opção "Todos" no início da lista
    categorias.insert(0, "Todos")

    return categorias

# Verificar a conexão com o banco de dados
if not os.path.exists('conexao.txt'):
    st.set_page_config(layout="wide")

    user = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')
    host = st.text_input('Host')
    porta = st.text_input('Porta')

    if st.button('Conectar'):
        banco_de_dados = f.database(user, password, host, porta)
        banco_de_dados.conexao_info()
        try:
            banco_de_dados.criar_conexao()
            banco_de_dados.banco_setup()
            conexao, cursor = banco_de_dados.conectar()
            st.write('Banco de dados criado com sucesso!')
            st.title("🎥 **Query Crews - Guia de Filmes e Canais**")
            st.write("**Encontre facilmente os horários dos seus filmes favoritos nos canais disponíveis.**")
            st.divider()

            # Buscar categorias dinamicamente
            categorias = get_categorias_filmes()

            # Adicionar uma selectbox para escolher a categoria
            categoria_escolhida = st.selectbox("Escolha a categoria de filme", categorias)

            # Selecionar e exibir os filmes com base na categoria escolhida
            filmes_df = select_filmes_por_categoria(categoria_escolhida)
            mostrar_filmes(filmes_df, f"Filmes de {categoria_escolhida}")
                
        except Exception as e:
            st.write(f'Erro: {e}')
            st.write('Verifique se o banco de dados está rodando e se as informações estão corretas.')
        st.rerun()
else:
    with open('conexao.txt', 'r') as file:
        user = file.readline().strip()
        password = file.readline().strip()
        host = file.readline().strip()
        porta = file.readline().strip()

    banco_de_dados = f.database(user, password, host, porta)
    conexao, cursor = banco_de_dados.conectar()
    st.set_page_config(layout="wide")
    st.title("🎥 **Query Crews - Guia de Filmes e Canais**")
    st.write("**Encontre facilmente os horários dos seus filmes favoritos nos canais disponíveis.**")
    st.divider()

    # Buscar categorias dinamicamente
    categorias = get_categorias_filmes()

    # Adicionar uma selectbox para escolher a categoria
    categoria_escolhida = st.selectbox("Escolha a categoria de filme", categorias)

    # Selecionar e exibir os filmes com base na categoria escolhida
    filmes_df = select_filmes_por_categoria(categoria_escolhida)
    mostrar_filmes(filmes_df, f"Filmes de {categoria_escolhida}")
