from binascii import Error


def criar_banco(conexao,cursor):    
    with open("Criar-esquema_script.sql", 'r') as file: # Abrindo e lendo o arquivo SQL
        sql_script = file.read()
        for statement in sql_script.split(';'):
            if statement.strip():
                try:
                    cursor.execute(statement)
                    conexao.commit()  # Fazendo commit das alterações no banco
                except Error as e:
                    print(f"Erro ao executar o comando: {statement}")
                    print(f"Erro: {e}")

# def popular_banco()

