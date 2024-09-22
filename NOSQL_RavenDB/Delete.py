from Ravendb import get_store 
from ExemploInsercoes import Film


def delete_old_movies():
    store = get_store()
    
    with store.open_session() as session:
        old_movies = list(session.query(object_type=Film).where_less_than("ano_lancamento", 2000))
        
        for movie in old_movies:
            session.delete(movie)
        session.save_changes()
        
        print(f"Excluídos {len(old_movies)} filmes lançados antes de 2000.")


delete_old_movies()
