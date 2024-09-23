from Ravendb import get_store  # Função para conectar ao RavenDB
from ExemploInserções import Film  # Importa o modelo Film usado para definir os dados dos filmes

def update_film():
    store = get_store()
    
    with store.open_session() as session:
        # Consulta todos os filmes
        all_films = list(session.query(object_type=Film))
        
        if not all_films:
            print("Nenhum filme encontrado.")
            return
        
        print("Filmes disponíveis:")
        for idx, film in enumerate(all_films):
            print(f"{idx + 1}. {film.titulo_brasil} (ID: {session.advanced.get_document_id(film)})")
        
        # Seleção do filme pelo número
        selected_index = int(input("Escolha o número do filme que deseja atualizar: ")) - 1
        if selected_index < 0 or selected_index >= len(all_films):
            print("Seleção inválida.")
            return
        
        selected_film = all_films[selected_index]

        # Exibir os campos do filme e solicitar atualizações
        print("\nCampos do filme selecionado:")
        print(f"1. Título (Original): {selected_film.titulo_original}")
        print(f"2. Título (Brasil): {selected_film.titulo_brasil}")
        print(f"3. Sinopse: {selected_film.sinopse}")
        print(f"4. Ano de Lançamento: {selected_film.ano_lancamento}")
        print(f"5. Poster URL: {selected_film.poster_url}")

        # Escolher o campo para atualizar
        field_choice = int(input("\nEscolha o campo que deseja atualizar (digite o número): "))
        
        # Dicionário para mapeamento dos campos com seus atributos
        field_map = {
            1: 'titulo_original',
            2: 'titulo_brasil',
            3: 'sinopse',
            4: 'ano_lancamento',
            5: 'poster_url'
        }

        if field_choice not in field_map:
            print("Seleção de campo inválida.")
            return
        
        # Solicita o novo valor para o campo selecionado
        new_value = input(f"Digite o novo valor para {field_map[field_choice]}: ")

        # Conversão de tipo para campos específicos, se necessário
        if field_map[field_choice] == 'ano_lancamento':
            try:
                new_value = int(new_value)  # Convertendo para inteiro se for o ano de lançamento
            except ValueError:
                print("Erro: O ano de lançamento deve ser um número.")
                return
        
        # Atualiza o campo do filme com o novo valor
        setattr(selected_film, field_map[field_choice], new_value)

        # Salva as mudanças no banco de dados
        session.store(selected_film)
        session.save_changes()
        
        print(f"\nO filme '{selected_film.titulo_brasil}' foi atualizado com sucesso!")

# Exemplo de uso
if __name__ == "__main__":
    update_film()
