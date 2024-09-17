from local_connection import Database_connection
from port_SQL_to_Python import criar_banco, criar_triggers, popular_banco
import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.config = self._get_config()
        self.conexao = None
        self.cursor = None

    def _get_config(self):
        db = Database_connection()
        return {
            'user': db.user,
            'password': db.password,
            'host': db.host,
            'port': db.port,
            'database': db.database
        }

    def connect(self):
        try:
            self.conexao = mysql.connector.connect(**self.config)
            self.cursor = self.conexao.cursor() if self.conexao.is_connected() else None
            print("Conectado ao banco de dados com sucesso!") if self.cursor else None
        except mysql.connector.Error as err:
            self._handle_error(err)
        return self.conexao, self.cursor

    def _handle_error(self, err):
        error_messages = {
            mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR: "Usuário ou senha inválidos!",
            mysql.connector.errorcode.ER_BAD_DB_ERROR: "Banco de dados não existe!",
            mysql.connector.errorcode.CR_CONN_HOST_ERROR: "Host ou porta inválidos!"
        }
        print(error_messages.get(err.errno, f"Erro ao conectar ao banco de dados: {err}"))

    def setup_database(self):
        if self.conexao and self.cursor:
            criar_banco(self.conexao, self.cursor)
            criar_triggers(self.conexao, self.cursor)
            popular_banco(self.conexao, self.cursor)
            print("Banco de dados configurado com sucesso!")

# Criar a instância do DatabaseManager
db_manager = DatabaseManager()

def main():
    conexao, cursor = db_manager.connect()
    if cursor:
        db_manager.setup_database()
        conexao.close()

def getConexaoCursor():
    return db_manager.connect()
