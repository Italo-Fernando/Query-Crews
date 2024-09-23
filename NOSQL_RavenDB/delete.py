from Ravendb import get_store
from ExemploInsercoes import Film

# def delete_filme_por_nome():
#     store = get_store()
    
#     with store.open_session() as session:
#         # Consulta todos os filmes
#         all_films = list(session.query(object_type=Film))
        
#         if not all_films:
#             print("Nenhum filme encontrado.")
#             return
        
#         print("Filmes disponíveis:")
#         for idx, film in enumerate(all_films):
#             print(f"{idx + 1}. {film.titulo_brasil} (ID: {session.advanced.get_document_id(film)})")
        
#         # Seleção do filme pelo número
#         selected_index = int(input("Escolha o número do filme que deseja deletar: ")) - 1
#         if selected_index < 0 or selected_index >= len(all_films):
#             print("Seleção inválida.")
#             return
        
#         selected_film = all_films[selected_index]
#         film_id = session.advanced.get_document_id(selected_film)

#         session.delete(film_id)  # Deleta o documento pelo ID
#         session.save_changes()     # Salva as alterações no banco
        
#         print(f"Filme deletado: {selected_film.titulo_brasil} (ID: {film_id})")

# delete_filme_por_nome()


def deletar_filmes_antigos():
    loja = get_store()
    
    ano_limite = int(input("Digite o ano limite para deletar filmes (filmes lançados antes deste ano serão excluídos): "))
    
    with loja.open_session() as sessao:
        filmes_antigos = list(sessao.query(object_type=Film).where_less_than("ano_lancamento", ano_limite))
        
        for filme in filmes_antigos:
            sessao.delete(filme)
        sessao.save_changes()
        
        print(f"Excluídos {len(filmes_antigos)} filmes lançados antes de {ano_limite}.")

# Exemplo de uso
deletar_filmes_antigos()

# def delete_exhibition():
#     store = get_store()
    
#     with store.open_session() as session:

#         films_with_exhibitions = list(session.query(object_type=Film).where_greater_than("exibicoes.length", 0))
        
#         if not films_with_exhibitions:
#             print("Nenhum filme encontrado com exibições.")
#             return
        
#         print("Filmes com exibições:")
#         for idx, film in enumerate(films_with_exhibitions):
#             print(f"{idx + 1}. {film.titulo_brasil} (ID: {session.advanced.get_document_id(film)})")
        
#         # Seleção do filme
#         selected_index = int(input("Escolha o número do filme para deletar uma exibição: ")) - 1
#         if selected_index < 0 or selected_index >= len(films_with_exhibitions):
#             print("Seleção inválida.")
#             return
        
#         selected_film = films_with_exhibitions[selected_index]
        
#         # Exibir as exibições do filme selecionado
#         print(f"Exibições para {selected_film.titulo_brasil}:")
#         for idx, exibicao in enumerate(selected_film.exibicoes):
#             # Carrega o canal usando a função load
#             canal = session.load(exibicao['num_canal'])
#             canal_nome = canal.nome if canal else "Canal não encontrado"
#             print(f"{idx + 1}. Canal: {canal_nome}, Data: {exibicao['data_exibicao']}")
        
#         # Seleção da exibição para deletar
#         exibicao_index = int(input("Escolha o número da exibição para deletar: ")) - 1
#         if exibicao_index < 0 or exibicao_index >= len(selected_film.exibicoes):
#             print("Seleção inválida.")
#             return
        
#         # Deletar exibição
#         deleted_exhibition = selected_film.exibicoes.pop(exibicao_index)
        
#         # Salvar alterações
#         session.store(selected_film)
#         session.save_changes()
        
#         print(f"Exibição deletada: Canal {canal_nome}, Data {deleted_exhibition['data_exibicao']} para o filme {selected_film.titulo_brasil}.")

# delete_exhibition()