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


def criar_triggers(conexao,cursor):
    trigger1 = """
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
    cursor.execute(trigger1)
    cursor.execute(trigger2)
    conexao.commit()

def popular_banco(conexao,cursor):
    with open("popular-banco.sql", 'r') as file: # Abrindo e lendo o arquivo SQL
        sql_script = file.read()
        for statement in sql_script.split(';'):
            if statement.strip():
                try:
                    cursor.execute(statement)
                    conexao.commit()  # Fazendo commit das alterações no banco
                except Error as e:
                    print(f"Erro ao executar o comando: {statement}")
                    print(f"Erro: {e}")

