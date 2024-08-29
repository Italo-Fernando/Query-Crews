create schema Cinema_filmes;
use Cinema_filmes;

create table filme (num_filme int primary key,
título_original varchar(80) not null,
título_brasil varchar(80),
ano_lancamento year not null,
país_origem varchar(30),
categoria int,
duraco int not null,
foreign key (categoria) references categoria  (id_categoria)
);

create table canal (num_canal int primary key,
nome varchar(50),
sigla varchar(25));

create table exibicao
(num_filme int,
num_canal int,
data datetime,
primary key (num_filme, num_canal, data),
foreign key (num_filme) references filme (num_filme),
foreign key (num_canal) references canal (num_canal));

create table categoria (
id_categoria int AUTO_INCREMENT primary key ,
nome_categoria varchar(30) not null
)
