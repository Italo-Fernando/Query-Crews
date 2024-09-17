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


