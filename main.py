from local_connection import Database_connection
import mysql.connector
import subprocess

def main():
    db = Database_connection()
    user = db.add_user()
    password = db.add_password()
    host = db.add_host()
    port = db.add_port()
    database = db.add_database()
    
    config = {
        'user': user,
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }

    try:
        conexao = mysql.connector.connect(**config)
        if conexao.is_connected():
            print("Conectado ao banco de dados com sucesso!")

            print("Rodando tarefas iniciais no home.py...")
            subprocess.run(["streamlit", "run", "home.py"])
            
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == '__main__':
    main()

