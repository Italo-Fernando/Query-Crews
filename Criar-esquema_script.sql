CREATE SCHEMA Cinema_filmes;
USE Cinema_filmes;

CREATE TABLE IF NOT EXISTS  diretor (
    id_diretor INT AUTO_INCREMENT PRIMARY KEY,
    nome_diretor VARCHAR(40) not null
);

CREATE TABLE IF NOT EXISTS  categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS  canal (
    num_canal INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    sigla VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS  premio (
    id_premio INT AUTO_INCREMENT PRIMARY KEY,
    premios VARCHAR(70) NOT NULL
);

CREATE TABLE IF NOT EXISTS  filme (
    num_filme INT PRIMARY KEY,
    título_original VARCHAR(80) NOT NULL,
    título_brasil VARCHAR(80),
    ano_lancamento YEAR NOT NULL,
    país_origem VARCHAR(30),
    duracao INT NOT NULL,
    id_diretor INT NOT NULL,
    class_indicativo VARCHAR(3),
    FOREIGN KEY (id_diretor) REFERENCES diretor (id_diretor)
);

CREATE TABLE IF NOT EXISTS  premio_filme (
    id_premio INT,
    num_filme INT,
    FOREIGN KEY (id_premio) REFERENCES premio (id_premio),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme)
);

CREATE TABLE IF NOT EXISTS  exibicao (
    num_filme INT,
    num_canal INT,
    data_exibicao DATETIME,
    PRIMARY KEY (num_filme, num_canal, data_exibicao),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme),
    FOREIGN KEY (num_canal) REFERENCES canal (num_canal)
);

CREATE TABLE IF NOT EXISTS categorias_filmes(
	num_filme INT,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria),
	FOREIGN KEY (num_filme) REFERENCES filme (num_filme)
);

INSERT INTO canal (nome, sigla) VALUES
('Rede Globo', 'Globo'),
('Sistema Brasileiro de Televisão', 'SBT'),
('RecordTV', 'Record'),
('Rede Bandeirantes', 'Band'),
('RedeTV!', 'RedeTV'),
('TV Cultura', 'Cultura'),
('TV Brasil', 'TVB'),
('Canal Futura', 'Futura'),
('Esporte Interativo', 'EI'),
('Fox Sports', 'Fox Sports'),
('HBO Brasil', 'HBO'),
('CNN Brasil', 'CNN'),
('Disney Channel', 'Disney'),
('Cartoon Network', 'CN'),
('National Geographic Channel', 'NatGeo'),
('Discovery Channel', 'Discovery'),
('MTV Brasil', 'MTV'),
('Nickelodeon Brasil', 'Nick'),
('Telecine', 'Telecine'),
('History Channel', 'History');

insert into premio (premios) values 
('Academy Awards'), ('Cannes Film Festival'), ('Golden Globe Awards'), ('British Academy of Film and Television Arts'), ('Venice Film Festival'),
('Berlin International Film Festival'), ('Screen Actors Guild Awards'), ("Critics' Choice Movie Awards"), ('Independent Spirit Awards'), ('Sundance Film Festival'),
('European Film Awards'), ('Asian Film Awards'), ('Annie Awards'), ('Satellite Awards'), ('MTV Movie & TV Awards'), ('Gotham Independent Film Awards'),
('Hollywood Film Awards'), ('International Emmy Awards'), ('Ariel Awards'), ('Genie Awards'), ('Jutra Awards'), ('Premios Platino del Cine Iberoamericano'),
('Premios Fénix'), ('Grande Prêmio do Cinema Brasileiro'), ('Academia de las Artes y las Ciencias Cinematográficas de Argentina'), ('Premios Cóndor de Plata'),
('César Awards'), ('Goya Awards'), ('David di Donatello Awards'), ('German Film Awards'), ('Magritte Awards'), ('Bodil Awards'), ('Robert Awards'), ('Guldbagge Awards'),
('Amanda Awards'), ('Irish Film & Television Awards'), ('Swiss Film Award'), ('Golden Orange Awards'), ('Blue Dragon Film Awards'), ('Golden Bell Awards'),
('Nika Awards'), ('Polish Film Awards'), ('Luxembourg Film Prize'), ('Filmfare Awards'), ('National Film Awards'), ('Japan Academy Prize'), ('Grand Bell Awards'),
('Golden Horse Awards'), ('Hong Kong Film Awards'), ('Fajr International Film Festival'), ('Asia Pacific Screen Awards'), ('Africa Movie Academy Awards'),
("Africa Magic Viewers' Choice Awards"), ('Panafrican Film and Television Festival of Ouagadougou'), ('Australian Academy of Cinema and Television Arts Awards'),
('New Zealand Film Awards'), ('Saturn Awards'), ('Hugo Awards'), ('Razzie Awards'), ("Kids' Choice Awards"), ('Teen Choice Awards'), ("Women's Image Network Awards"),
('Toronto International Film Festival'), ('South by Southwest'), ('Tribeca Film Festival'), ('Locarno Film Festival'), ('San Sebastián International Film Festival'),
('Karlovy Vary International Film Festival'), ('Rotterdam International Film Festival'), ('Mar del Plata Film Festival'), ('Busan International Film Festival'),
('International Documentary Association Awards'), ('Cinema Eye Honors'), ('DocAviv Film Festival Awards'), ('Sheffield Doc/Fest Awards');

INSERT INTO categoria (nome_categoria) VALUES
('Ação'), ('Aventura'), ('Animação'), 
('Biografia'), ('Comédia'), ('Crime'), 
('Documentário'), ('Drama'), ('Épico'), 
('Família'), ('Fantasia'), ('Faroeste'), 
('Ficção Científica'), ('Guerra'), ('Histórico'), 
('Mistério'), ('Musical'), ('Policial'), 
('Romance'), ('Suspense'), ('Terror'), 
('Thriller'), ('Noir'), ('Esporte'), 
('Tribunal'), ('Espionagem'), ('Artes Marciais'), 
('Independente'), ('Experimental'), ('LGBTQ+'), 
('Fantasia Urbana'), ('Road Movie'), ('Pós-apocalíptico'), 
('Super-heróis'), ('Religioso'), ('Zumbi'), 
('Vampiro'), ('Monstros'), ('Antológico'), 
('Dança'), ('Aventura Espacial'), ('Natal'), 
('Cult'), ('Psicológico'), ('Social');
 
 
 
DELIMITER //
CREATE TRIGGER checar_exibicao_antes_lancamento
BEFORE INSERT ON exibicao
FOR EACH ROW
BEGIN
	DECLARE filme_ano_lancamento YEAR;
    
    SELECT ano_lancamento INTO filme_ano_lancamento
    FROM filme
    WHERE num_filme = NEW.num_filme;
    
    IF YEAR(NEW.data_exibicao) < filme_ano_lancamento THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'ERROR: Filme não pode ser exibido na televisão antes do ano de lançamento';
	END IF;
END;
//
DELIMITER ;

DELIMITER //
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
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'ERROR: Dois filmes não podem ser exibidos ao mesmo tempo no mesmo canal.';
    END IF;

END;
//
DELIMITER ;

-- FOREIGN KEY (categoria) REFERENCES categoria (id_categoria)
-- categoria INT,