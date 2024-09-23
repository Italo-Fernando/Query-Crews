from ravendb import DocumentStore

def get_store():
    store = DocumentStore(["http://localhost:8080"], "IAADProjectL")
    store.initialize()
    return store

def initialize_database():
    from PopularCanal import add_channels, channels
    from PopularMovie import add_movies, novos_filmes
    from PopularDirector import add_directors, novo_diretor
 

    add_movies(novos_filmes)
    add_channels(channels)
    add_directors(novo_diretor)
 

if __name__ == "__main__":
    store = get_store()
    initialize_database()
    print("Todos os dados foram adicionados com sucesso!")
