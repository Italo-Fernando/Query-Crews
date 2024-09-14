# Importar o Streamlit e outros módulos necessários
import streamlit as st
from components.components import card_component

# Configurar a página para ficar wide
st.set_page_config(layout="wide")

# Cabeçalho principal com título e descrição
st.title("🎥 **Query Crews - Guia de Filmes e Canais**")
st.write("**Encontre facilmente os horários dos seus filmes favoritos nos canais disponíveis.**")
st.divider()

# Colunas para uma apresentação visual mais organizada
col1, col2 = st.columns(2)

with col1:
    # Seção de canais disponíveis com ícones e botão expansível
    st.subheader("📺 **Canais Disponíveis**")
    with st.expander("Ver todos os canais"):
        st.write("""
        - **Telecine**
        - **HBO**
        - **Cinemax**
        - **TNT**
        - **FX**
        - **AMC**
        - **Paramount**
        - **Universal**
        [...]
        """)

with col2:
    # Seção de filmes disponíveis com ícones e botão expansível
    st.subheader("🎬 **Filmes Disponíveis**")
    with st.expander("Ver todos os filmes"):
        st.write("""
        - **A Culpa é das Estrelas**
        - **O Menino que Descobriu o Vento**
        - **O Menino do Pijama Listrado** 
        - **Inception**
        - **Matrix**
        - **Titanic** 
        [...]
        """)

# Seção de horários de exibição com sliders para escolher horário e canal
st.subheader("🕒 **Horários de Exibição**")
st.write("Selecione um canal e um intervalo de tempo para ver os filmes disponíveis:")

# Widgets interativos para escolher o canal e o horário
canal_selecionado = st.selectbox("Escolha um canal", ["Telecine", "HBO", "Cinemax", "TNT", "FX", "AMC"])
horario = st.slider("Escolha o intervalo de horário", 0, 24, (18, 22))

# Exibição dos filmes de acordo com o canal e horário selecionado
st.write(f"**Filmes no canal {canal_selecionado} entre {horario[0]}:00 e {horario[1]}:00:**")
st.write("- **Filme 1**: 19:00")
st.write("- **Filme 2**: 20:30")
st.write("- **Filme 3**: 21:45")

# Seção de busca com campo de texto
st.subheader("🔍 **Buscar por Filme ou Canal**")
busca = st.text_input("Digite o nome do filme ou canal")
if busca:
    st.write(f"Resultados para **{busca}**:")
    # Exemplo de resultado de busca
    st.write("- **Telecine**: Inception, 20:00")

st.divider()

cards = [
    {
        "title": "Avatar",
        "description": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "logo_url": "https://telaviva.com.br/wp-content/uploads/2016/02/Novo-logo-AXN.png",
        "logo_caption": "AXN<br>Domingo, 18:00h",
        "background_image": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMDg1Nzk1MV5BMl5BanBnXkFtZTcwMDk0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    },
    {
        "title": "I Am Legend",
        "description": "Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure.",
        "logo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1S3WHuIf9kmExAfpJDGzxYTMuBLgdlczp-w&s",
        "logo_caption": "Globo<br>Domingo, 18:00h",
        "background_image": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0MTI2NjMzMzFeQTJeQWpwZ15BbWU2MDMwNDc3OA@@._V1_.jpg"
    },
    {
        "title": "300",
        "description": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
        "logo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1S3WHuIf9kmExAfpJDGzxYTMuBLgdlczp-w&s",
        "logo_caption": "Globo<br>Domingo, 18:00h",
        "background_image": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0MjQzOTEwMV5BMl5BanBnXkFtZTcwMzE2NTIyMw@@._V1_SX1777_CR0,0,1777,947_AL_.jpg"
    },
    {
        "title": "The Avengers",
        "description": "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
        "logo_url": "https://telaviva.com.br/wp-content/uploads/2016/02/Novo-logo-AXN.png",
        "logo_caption": "AXN<br>Domingo, 20:00h",
        "background_image": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0NjY0NzE4OTReQTJeQWpwZ15BbWU3MDczODg2Nzc@._V1_SX1777_CR0,0,1777,999_AL_.jpg"
    },
    {
        "title": "The Wolf of Wall Street",
        "description": "Based on the True story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
        "logo_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1S3WHuIf9kmExAfpJDGzxYTMuBLgdlczp-w&s",
        "logo_caption": "Globo<br>Domingo, 22:00h",
        "background_image": "https://images-na.ssl-images-amazon.com/images/M/MV5BNDIwMDIxNzk3Ml5BMl5BanBnXkFtZTgwMTg0MzQ4MDE@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    },
    {
        "title": "Interstellar",
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "logo_url": "https://telaviva.com.br/wp-content/uploads/2016/02/Novo-logo-AXN.png",
        "logo_caption": "AXN<br>Domingo, 18:00h",
        "background_image": "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA3NTEwOTMxMV5BMl5BanBnXkFtZTgwMjMyODgxMzE@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    }
]

item_selecionado = st.slider("Filmes da Semana", 0, len(cards) - 2, 0)

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
    card_component(
        title=cards[item_selecionado + 1]["title"],
        description=cards[item_selecionado + 1]["description"],
        logo_url=cards[item_selecionado + 1]["logo_url"],
        logo_caption=cards[item_selecionado + 1]["logo_caption"],
        background_image=cards[item_selecionado + 1]["background_image"],
        unique_id=f"card2_{item_selecionado + 1}"  # Adicionando um identificador único
    )