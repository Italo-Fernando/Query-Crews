import mysql.connector

class Database_connection:
    def __init__(self):
        self.__user = None  # User object
        self.__password = None  # Password object
        self.__host = None  # Host object
        self.__port = 3306  # Default MySQL port
        self.database = None  # Database object

    def add_user(self):
        usuario = input("Digite o usuário da conexão: ")
        self.__user = usuario
        return self.__user

    def add_password(self):
        senha = input("Digite a senha da conexão: ")
        self.__password = senha
        return self.__password

    def add_host(self):
        host = input("Digite o host da conexão (sem porta): ")
        self.__host = host
        return self.__host

    def add_port(self):
        porta = input("Digite a porta da conexão (default 3306): ")
        if porta:
            self.__port = int(porta)  # Converte para inteiro
        return self.__port
    
    def add_database(self):
        database = input("Digite o nome do banco de dados(Schema): ")
        self.database = database
        return self.database

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
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == '__main__':
    main()
