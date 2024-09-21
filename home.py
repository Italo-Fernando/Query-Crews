# Importar o Streamlit e outros módulos necessários
import streamlit as st
import pandas as pd
from components.components import card_component
import funcoes as f
import os
from time import sleep

def selectFilmes():
    cursor.execute("SELECT * FROM exibicao e NATURAL LEFT JOIN filme f NATURAL LEFT JOIN canal c")

    filmes = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(filmes, columns=[desc[0] for desc in cursor.description])

    return df

def selectFilmesDrama():
    conexao, cursor = banco_de_dados.conectar()
    cursor.execute("SELECT * FROM filme f NATURAL LEFT JOIN canal c NATURAL JOIN categorias_filmes NATURAL JOIN categoria NATURAL JOIN exibicao e WHERE nome_categoria = 'Ficção Científica'")

    filmes = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(filmes, columns=[desc[0] for desc in cursor.description])

    return df

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
            item_selecionado = st.slider(f'{title}', 0, len(cards) - 2, len(cards)-1)
        else:
            st.write("Não há filmes suficientes para exibir no slider.")
        col1, col2 = st.columns(2)
        with col1:
            card_component(
                title=cards[item_selecionado]["title"],
                description=cards[item_selecionado]["description"],
                logo_url=cards[item_selecionado]["logo_url"],
                logo_caption=cards[item_selecionado]["logo_caption"],
                background_image=cards[item_selecionado]["background_image"],
                unique_id=f"card1_{item_selecionado}"  # Adicionando um identificador único
            )
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
                
def mostrar_filmes_categroria(filmes_df, title):    
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
            item_selecionado_categoria = st.slider(f'{title}', 0, len(cards) - 2, len(cards)-1)
        else:
            st.write("Não há filmes suficientes para exibir no slider.")
        col1, col2 = st.columns(2)
        with col1:
            card_component(
                title=cards[item_selecionado_categoria]["title"],
                description=cards[item_selecionado_categoria]["description"],
                logo_url=cards[item_selecionado_categoria]["logo_url"],
                logo_caption=cards[item_selecionado_categoria]["logo_caption"],
                background_image=cards[item_selecionado_categoria]["background_image"],
                unique_id=f"card1_{item_selecionado_categoria}"  # Adicionando um identificador único
            )
        with col2:
            if item_selecionado_categoria + 1 < len(cards):
                card_component(
                    title=cards[item_selecionado_categoria + 1]["title"],
                    description=cards[item_selecionado_categoria + 1]["description"],
                    logo_url=cards[item_selecionado_categoria + 1]["logo_url"],
                    logo_caption=cards[item_selecionado_categoria + 1]["logo_caption"],
                    background_image=cards[item_selecionado_categoria + 1]["background_image"],
                    unique_id=f"card2_{item_selecionado_categoria + 1}"  # Adicionando um identificador único
                )


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
            
            filmes_df = selectFilmes()
    
            mostrar_filmes(filmes_df, "Filmes da Semana")
    
            mostrar_filmes_categroria(selectFilmesDrama(), "Filmes de Drama")
                
        except:  # Ajuste o tipo de exceção
            st.write(f'Erro: ')
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
    
    filmes_df = selectFilmes()
    
    mostrar_filmes(filmes_df, "Filmes da Semana")
    
    mostrar_filmes_categroria(selectFilmesDrama(), "Filmes de Drama")