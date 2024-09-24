from Ravendb import get_store
from ExemploInsercoes import Film

# #1
# def delete_filme_por_nome():
#     loja = get_store()
    
#     with loja.open_session() as sessao:
#         todos_os_filmes = list(sessao.query(object_type=Film))
        
#         if not todos_os_filmes:
#             print("Nenhum filme encontrado.")
#             return
        
#         print("Filmes disponíveis:")
#         for index, film in enumerate(todos_os_filmes):
#             print(f"{index + 1}. {film.titulo_brasil} (ID: {sessao.advanced.get_document_id(film)})")
        
#         # Seleção do filme pelo número
#         index_selecionado = int(input("Escolha o número do filme que deseja deletar: ")) - 1
#         if index_selecionado < 0 or index_selecionado >= len(todos_os_filmes):
#             print("Seleção inválida.")
#             return
        
#         filme_selecionado =todos_os_filmes[index_selecionado]
#         filme_id = sessao.advanced.get_document_id(filme_selecionado)

#         sessao.delete(filme_id)
#         sessao.save_changes()
        
#         print(f"Filme deletado: {filme_selecionado.titulo_brasil} (ID: {filme_id})")

# delete_filme_por_nome()


##2
# def deletar_filmes_antigos():
#     loja = get_store()
    
#     ano_limite = int(input("Digite o ano limite para deletar filmes (filmes lançados antes deste ano serão excluídos): "))
    
#     with loja.open_session() as sessao:
#         filmes_antigos = list(sessao.query(object_type=Film).where_less_than("ano_lancamento", ano_limite))
        
#         for filme in filmes_antigos:
#             sessao.delete(filme)
#         sessao.save_changes()
        
#         print(f"Excluídos {len(filmes_antigos)} filmes lançados antes de {ano_limite}.")

# deletar_filmes_antigos()

# def deletar_exibicao():
#     loja = get_store()
    
#     with loja.open_session() as sessao:

#         filme_com_exibicao = list(sessao.query(object_type=Film).where_greater_than("exibicoes.length", 0))
        
#         if not filme_com_exibicao:
#             print("Nenhum filme encontrado com exibições.")
#             return


# #3
# def deletar_exibicao():
#     loja = get_store()
    
#     with loja.open_session() as sessao:

#         filme_com_exibicao = list(sessao.query(object_type=Film).where_greater_than("exibicoes.length", 0))
        
#         if not filme_com_exibicao:
#             print("Nenhum filme encontrado com exibições.")
#             return

#         print("Filmes com exibições:")
#         for index, film in enumerate(filme_com_exibicao):
#             print(f"{index + 1}. {film.titulo_brasil} (ID: {sessao.advanced.get_document_id(film)})")
        
#         # Seleção do filme
#         index_selecionado = int(input("Escolha o número do filme para deletar uma exibição: ")) - 1
#         if index_selecionado < 0 or index_selecionado >= len(filme_com_exibicao):
#             print("Seleção inválida.")
#             return
        
#         filme_selecionado = filme_com_exibicao[index_selecionado]
        
#         # Exibir as exibições do filme selecionado
#         print(f"Exibições para {filme_selecionado.titulo_brasil}:")
#         for index, exibicao in enumerate(filme_selecionado.exibicoes):
#             # Carrega o canal usando a função load
#             canal = sessao.load(exibicao['num_canal'])
#             canal_nome = canal.nome if canal else "Canal não encontrado"
#             print(f"{index + 1}. Canal: {canal_nome}, Data: {exibicao['data_exibicao']}")
        
#         # Seleção da exibição para deletar
#         exibicao_index = int(input("Escolha o número da exibição para deletar: ")) - 1
#         if exibicao_index < 0 or exibicao_index >= len(filme_selecionado.exibicoes):
#             print("Seleção inválida.")
#             return
        
#         # Deletar exibição
#         exibicao_deletada = filme_selecionado.exibicoes.pop(exibicao_index)
        
#         sessao.store(filme_selecionado)
#         sessao.save_changes()
        
#         print(f"Exibição deletada: Canal {canal_nome}, Data {exibicao_deletada['data_exibicao']} para o filme {filme_selecionado.titulo_brasil}.")

# deletar_exibicao()