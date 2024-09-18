import mysql.connector
import os
class database:

    def __init__(self,user,password,host,port):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.esquema = "cinema_filmes"
        self.conexao = None
        self.cursor = None

    def criar_banco(self):
        conexao = self.conexao
        cursor = self.cursor
        with open('scripts_SQL\Script_esquema.sql', 'r') as file:
            script = file.read()
            for declaracao in script.split(';'):
                if declaracao.strip():
                    try:
                        cursor.execute(declaracao)
                        conexao.commit()
                        
                    except Exception as e:
                        print(f'Erro: {e}')
            return None
        
    def criar_triggers(self):
        conexao = self.conexao
        cursor = self.cursor

        trigger_1 = """
        CREATE TRIGGER checar_exibicao_antes_lancamento
        BEFORE INSERT ON exibicao
        FOR EACH ROW
        BEGIN
            DECLARE filme_ano_lancamento YEAR;

            -- Obtendo o ano de lançamento do filme
            SELECT ano_lancamento INTO filme_ano_lancamento
            FROM filme
            WHERE num_filme = NEW.num_filme;

            -- Verificando se a exibição ocorre antes do ano de lançamento
            IF YEAR(NEW.data_exibicao) < filme_ano_lancamento THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'ERROR: Filme não pode ser exibido na televisão antes do ano de lançamento';
            END IF;
        END;
        """
        trigger2 = '''
        CREATE TRIGGER filmes_conflitantes 
        BEFORE INSERT ON exibicao
        FOR EACH ROW
        BEGIN
            DECLARE data_fim DATETIME;
             SELECT ADDTIME(NEW.data_exibicao, SEC_TO_TIME(f.duracao * 60)) INTO data_fim
            FROM filme f
            WHERE f.num_filme = NEW.num_filme;

            IF EXISTS (
            SELECT 1
            FROM exibicao e
            JOIN filme f ON e.num_filme = f.num_filme
            WHERE e.num_canal = NEW.num_canal
            AND (
            NEW.data_exibicao BETWEEN e.data_exibicao AND ADDTIME(e.data_exibicao, SEC_TO_TIME(f.duracao * 60))
            OR
            data_fim BETWEEN e.data_exibicao AND ADDTIME(e.data_exibicao, SEC_TO_TIME(f.duracao * 60))
            )
            )  THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'ERROR: Dois filmes não podem ser exibidos ao mesmo tempo no mesmo canal.';
                    END IF;

        END;'''
        cursor.execute(trigger_1)
        cursor.execute(trigger2)
        conexao.commit()
        return None

    def popular_banco(self):
        conexao = self.conexao
        cursor = self.cursor
        with open('scripts_SQL\Script_popular.sql', 'r') as file:
            script = file.read()
            for declaracao in script.split(';'):
                if declaracao.strip():
                    try:
                        cursor.execute(declaracao)
                        conexao.commit()
                        
                    except Exception as e:
                        print(f'Erro: {e}')
            return None
        
    

    def criar_conexao(self): # so usar pela primeira vez na home
        try:
            config = {
                'user': self.user,
                'password': self.password,
                'host': self.host,
                'port': self.port
            }
            self.conexao = mysql.connector.connect(**config)
            self.cursor = self.conexao.cursor()
            return self.conexao
        except mysql.connector.Error as e:
            print(f'Erro: {e}')
            print('Verifique se o banco de dados está rodando e se as informações estão corretas.')
            return None
        
    def conectar(self):
        try:
            config = {
                'user': self.user,
                'password': self.password,
                'host': self.host,
                'port': self.port,
                'database': self.esquema
            }
            self.conexao = mysql.connector.connect(**config)
            self.cursor = self.conexao.cursor()
            return self.conexao, self.cursor
        except mysql.connector.Error as e:
            print(f'Erro: {e}')
            print('Verifique se o banco de dados está rodando e se as informações estão corretas.')
            return None
        
    def banco_setup(self):
        self.criar_banco()
        self.criar_triggers()
        self.popular_banco()
        return None

    def conexao_info(self):
        if not os.path.exists('conexao.txt'):
            with open('conexao.txt', 'w') as file:
                file.write(f'{self.user}\n{self.password}\n{self.host}\n{self.port}')
                return None
            