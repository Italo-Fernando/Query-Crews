from Ravendb import get_store

class Director:
    def __init__(self, nome_diretor):
        self.nome_diretor = nome_diretor

def add_directors(directors):
    store = get_store()
    with store.open_session() as session:
        for director in directors:
            director_instance = Director(**director)
            session.store(director_instance) 
        session.save_changes()


        for director in directors:
            director_id = session.advanced.get_document_id(director_instance)
            print(f"Diretor inserido com ID: {director_id}")

novo_diretor = [
    {"nome_diretor": "Kelsey Mann"},
    {"nome_diretor": "Christopher Nolan"},
    {"nome_diretor": "Lilly Wachowski"},
    {"nome_diretor": "Bong Joon-ho"},
    {"nome_diretor": "Francis Ford Coppola"},
    {"nome_diretor": "Frank Darabont"},
    {"nome_diretor": "Quentin Tarantino"},
    {"nome_diretor": "Robert Zemeckis"},
    {"nome_diretor": "David Fincher"},
    {"nome_diretor": "Adrian Molina"},
    {"nome_diretor": "George Miller"},
    {"nome_diretor": "Wes Anderson"},
    {"nome_diretor": "Guillermo del Toro"},
    {"nome_diretor": "Alejandro González Iñárritu"},
    {"nome_diretor": "Byron Howard"},
]





