CREATE SCHEMA IF NOT EXISTS Cinema_filmes DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE Cinema_filmes;

CREATE TABLE IF NOT EXISTS diretor (
    id_diretor INT AUTO_INCREMENT PRIMARY KEY,
    nome_diretor VARCHAR(40) NOT NULL,
    UNIQUE (nome_diretor)
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(30) NOT NULL
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS canal (
    num_canal INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    sigla VARCHAR(25),
    logo_canal VARCHAR(255)
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS premio (
    id_premio INT AUTO_INCREMENT PRIMARY KEY,
    premios VARCHAR(70) NOT NULL
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS filme (
    num_filme INT AUTO_INCREMENT PRIMARY KEY,
    titulo_original VARCHAR(80) NOT NULL,
    titulo_brasil VARCHAR(80),
    sinopse VARCHAR(500),
    ano_lancamento YEAR NOT NULL,
    poster_url VARCHAR(500),
    pas_origem VARCHAR(30),
    duracao INT NOT NULL,
    id_diretor INT,
    class_indicativo VARCHAR(5),
    FOREIGN KEY (id_diretor) REFERENCES diretor (id_diretor),
    UNIQUE (titulo_brasil, titulo_original)
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS premio_filme (
    id_premio INT,
    num_filme INT,
    FOREIGN KEY (id_premio) REFERENCES premio (id_premio) ON DELETE CASCADE,
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme) ON DELETE CASCADE
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS exibicao (
    num_filme INT,
    num_canal INT,
    data_exibicao DATETIME,
    PRIMARY KEY (num_filme, num_canal, data_exibicao),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme) ON DELETE CASCADE,
    FOREIGN KEY (num_canal) REFERENCES canal (num_canal)
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE IF NOT EXISTS categorias_filmes (
    num_filme INT,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme) ON DELETE CASCADE
    
) DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;