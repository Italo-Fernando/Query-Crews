CREATE SCHEMA Cinema_filmes;
USE Cinema_filmes;

CREATE TABLE diretor (
    id_diretor INT AUTO_INCREMENT PRIMARY KEY,
    nome_diretor VARCHAR(40) not null
);

CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(30) NOT NULL
);

CREATE TABLE filme (
    num_filme INT PRIMARY KEY,
    título_original VARCHAR(80) NOT NULL,
    título_brasil VARCHAR(80),
    ano_lancamento YEAR NOT NULL,
    país_origem VARCHAR(30),
    categoria INT,
    duraco INT NOT NULL,
    id_diretor INT NOT NULL,
    FOREIGN KEY (id_diretor) REFERENCES diretor (id_diretor),
    FOREIGN KEY (categoria) REFERENCES categoria (id_categoria)
);

CREATE TABLE canal (
    num_canal INT PRIMARY KEY,
    nome VARCHAR(50),
    sigla VARCHAR(25)
);

CREATE TABLE exibicao (
    num_filme INT,
    num_canal INT,
    data DATETIME,
    PRIMARY KEY (num_filme, num_canal, data),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme),
    FOREIGN KEY (num_canal) REFERENCES canal (num_canal)
);

CREATE TABLE custo_ganho (
    num_filme INT,
    bilheteria DECIMAL(12,2),
    orcamento DECIMAL(12,2) not null,
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme)
);

CREATE TABLE premio (
    id_premio INT AUTO_INCREMENT PRIMARY KEY,
    premios VARCHAR(70) NOT NULL
);

CREATE TABLE premio_filme (
    id_premio INT,
    num_filme INT,
    FOREIGN KEY (id_premio) REFERENCES premio (id_premio),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(50) NOT NULL,
    email_usuario VARCHAR(50) NOT NULL
);

CREATE TABLE favoritos (
    id_usuario INT,
    num_filme INT,
    starhate INT CHECK (starhate BETWEEN 0 AND 5),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    FOREIGN KEY (num_filme) REFERENCES filme (num_filme)
);

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
('International Documentary Association Awards'), ('Cinema Eye Honors'), ('DocAviv Film Festival Awards'), ('Sheffield Doc/Fest Awards')
