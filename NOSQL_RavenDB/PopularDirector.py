from Ravendb import get_store

class Director:
    def __init__(self, nome_diretor):
        self.nome_diretor = nome_diretor

def add_directors(directors):
    store = get_store()
    with store.open_session() as session:
        for index, director in enumerate(directors, start=1):
            director_instance = Director(**director) 
            director_id = f"directors/{index}"  
            session.store(director_instance, director_id) 
        session.save_changes()

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





