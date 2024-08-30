# Importar o Streamlit e outros módulos necessários
import streamlit as st

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
