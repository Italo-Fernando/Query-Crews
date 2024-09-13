from local_connection import Database_connection
from port_SQL_to_Python import criar_banco, criar_triggers, popular_banco
import mysql.connector
import subprocess

def main():
    db = Database_connection()
    user = db.add_user()
    password = db.add_password()
    host = db.add_host()
    port = db.add_port()
    # database = db.add_database()
    
    config = {
        'user': user,
        'password': password,
        'host': host,
        'port': port
    }
    try:
        conexao = mysql.connector.connect(**config)
        if conexao.is_connected():
            cursor = conexao.cursor()
            print("Conectado ao banco de dados com sucesso!")
            print("Rodando tarefas iniciais no home.py...")
            criar_banco(conexao,cursor)
            criar_triggers(conexao,cursor)
            popular_banco(conexao,cursor)

            
            subprocess.run(["streamlit", "run", "home.py"])
            
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha inválidos!")      
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe!")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print("Host não encontrado!")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print("Porta inválida!")
        else:
            print(f"Erro ao conectar ao banco de dados: {err}")

if __name__ == '__main__':
    main()

