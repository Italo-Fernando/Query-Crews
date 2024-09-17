import streamlit as st
from home import getConexaoCursor

conexao, cursor = getConexaoCursor()

def pesquisar_filmes(conexao):
    st.header("Pesquisar Filmes")

    # Definir os gêneros fixos em minúsculas
    generos_disponiveis = [
        "ação", "aventura", "animação", "comédia", "drama", "fantasia",
        "ficção científica", "terror", "mistério", "romance", "suspense",
        "documentário", "musical", "histórico", "guerra", "ocultismo",
        "criminal", "biografia", "far oeste", "film-noir", "esporte",
        "família", "comédia romântica"
    ]

    # Buscar todos os canais disponíveis
    cursor = conexao.cursor()
    cursor.execute("SELECT num_canal, sigla FROM canal")
    canais = cursor.fetchall()
    canais = {f"{sigla} [ID: {num}]": num for num, sigla in canais}  # Mapeia sigla para num_canal
    cursor.close()

    # Filtros
    st.sidebar.subheader("Filtros")

    # Filtro por gênero
    filtro_genero = st.sidebar.selectbox("Gênero", ["Todos"] + generos_disponiveis)

    # Filtro por ano
    ano_min = st.sidebar.number_input("Ano Mínimo", min_value=1900, max_value=2100, value=1900, step=1)
    ano_max = st.sidebar.number_input("Ano Máximo", min_value=1900, max_value=2100, value=2024, step=1)

    # Filtro por canais de exibição
    filtro_canal = st.sidebar.selectbox("Canal", ["Todos"] + list(canais.keys()))

    # Montar a consulta SQL com filtros
    query = """
    SELECT f.num_filme, f.titulo_original, f.titulo_brasil, f.ano_lancamento, f.pais_origem, f.categoria, f.duracao
    FROM filme f
    LEFT JOIN exibicao e ON f.num_filme = e.num_filme
    WHERE (LOWER(f.categoria) = %s OR %s = 'todos')
    AND (f.ano_lancamento BETWEEN %s AND %s)
    AND (e.num_canal = %s OR %s = 'todos')
    """

    # Executar a consulta com filtros
    params = (
        filtro_genero.lower(),
        filtro_genero.lower(),
        ano_min,
        ano_max,
        canais.get(filtro_canal, None),
        filtro_canal.lower()
    )
    cursor = conexao.cursor()
    cursor.execute(query, params)
    filmes = cursor.fetchall()
    cursor.close()

    # Exibir os filmes encontrados
    if filmes:
        st.write("### Resultados da Pesquisa")
        for filme in filmes:
            st.write(f"**Título Original:** {filme[1]}")
            st.write(f"**Título no Brasil:** {filme[2] if filme[2] else 'Não disponível'}")
            st.write(f"**Ano de Lançamento:** {filme[3]}")
            st.write(f"**País de Origem:** {filme[4] if filme[4] else 'Não disponível'}")
            st.write(f"**Gênero:** {filme[5] if filme[5] else 'Não disponível'}")
            st.write(f"**Duração:** {filme[6]} minutos")
            st.write("---")
    else:
        st.write("Nenhum filme encontrado com os critérios de pesquisa.")

if conexao and cursor:
    pesquisar_filmes(conexao)
