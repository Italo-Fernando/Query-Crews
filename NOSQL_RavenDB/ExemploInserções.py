from Ravendb import get_store


class Film:
    def __init__(self, titulo_original, titulo_brasil, sinopse, ano_lancamento, poster_url, pas_origem, duracao, id_diretor, class_indicativo, exibicoes=None):
        self.titulo_original = titulo_original
        self.titulo_brasil = titulo_brasil
        self.sinopse = sinopse
        self.ano_lancamento = ano_lancamento
        self.poster_url = poster_url
        self.pas_origem = pas_origem
        self.duracao = duracao
        self.id_diretor = id_diretor    
        self.class_indicativo = class_indicativo
        self.exibicoes = exibicoes if exibicoes else []


def add_movie(movie):
    store = get_store()  
    with store.open_session() as session:
        film = Film(**movie)
        session.store(film)
        session.save_changes()
        film_id = session.advanced.get_document_id(film)
        print(f"Filme inserido com ID: {film_id}")

exhibitions = [
    {"num_canal": "channels/10", "data_exibicao": '2024-17-20 01:00:00'},
    {"num_canal": "channels/4", "data_exibicao": '2024-05-20 13:30:00'},
]



movie_data = {
    "titulo_original": "Spider-Man: Into the Spider-Verse",
    "titulo_brasil": "Homem-Aranha no Aranhaverso",
    "sinopse": "Após ser atingido por uma teia radioativa, Miles Morales, um jovem negro do Brooklyn, se torna o Homem-Aranha, inspirado no legado do já falecido Peter Parker...",
    "ano_lancamento": 2019,
    "poster_url": "https://img.odcdn.com.br/wp-content/uploads/2023/06/homem-aranha-atraves-do-aranhaverso.jpg",
    "pas_origem": "EUA",
    "duracao": 117,
    "id_diretor": "directors/4",
    "class_indicativo": "Livre",
    "exibicoes": exhibitions
}

add_movie(movie_data)