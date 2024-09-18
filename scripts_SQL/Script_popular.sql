
INSERT INTO canal (nome, sigla, logo_canal) VALUES
('Rede Globo', 'Globo', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1S3WHuIf9kmExAfpJDGzxYTMuBLgdlczp-w&s'),
('Sistema Brasileiro de Televisão', 'SBT', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcVYPc-pELbp8t_0EhGtRFsSj1gXPMQWJgwA&s'),
('RecordTV', 'Record', 'https://play-lh.googleusercontent.com/86YxRYXi1bikmEQInrLFY7913Ng0xgzwZPuXU5k7NWnePoxX4E6UxMK8I5axLJZqWsDb=w240-h480-rw'),
('Rede Bandeirantes', 'Band', 'https://cdn.worldvectorlogo.com/logos/band-1.svg'),
('RedeTV!', 'RedeTV', 'https://pbs.twimg.com/media/FywWpO1X0AAfD3B.jpg:large'),
('TV Cultura', 'Cultura', 'https://upload.wikimedia.org/wikipedia/commons/8/82/Cultura_logo_2013.svg'),
('TV Brasil', 'TVB', 'https://yt3.googleusercontent.com/fs6EI0tEgITiQzy3j5nXhp6hv9KBWYPMjqJTbPdH6ogzGnEI2P-lF9oBMlbku7bp1VXxcy8cxw=s176-c-k-c0x00ffffff-no-rj-mo'),
('Canal Futura', 'Futura', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLorEDMiv4WNKxoCRPxaPWfYPvc5ntwWgjVDKyRRbwVylAlOTLi0KyacUcjOfU6x8EZCY&usqp=CAU'),
('Esporte Interativo', 'EI', 'https://upload.wikimedia.org/wikipedia/commons/1/19/LOGO_EI-2.jpg'),
('Fox Sports', 'Fox Sports', 'https://logowik.com/content/uploads/images/fox-sports3529.jpg'),
('HBO Brasil', 'HBO', 'https://logowik.com/content/uploads/images/hbo.jpg'),
('CNN Brasil', 'CNN', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgT-R52bE5nFi11FvXv3Er0ADTmXuBd3ieeQ&s'),
('MTV Brasil', 'MTV', 'https://cdn.dribbble.com/users/174209/screenshots/1465961/media/1956c5abb6840358546e32cf3298057a.jpg?resize=400x300&vertical=center'),
('Telecine', 'Telecine', 'https://gkpb.com.br/wp-content/uploads/2019/07/novo-logo-telecine-seu-momento-cinema-versao-negativa-1024x1024.jpg');



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

INSERT INTO diretor (nome_diretor) VALUES
('Steven Spielberg'), ('Quentin Tarantino'), 
('Christopher Nolan'), ('David Fincher'), ('James Cameron'), 
('Ridley Scott'), ('Tim Burton'), ('Peter Jackson'), 
('Clint Eastwood'), ('Woody Allen'), ('Spike Lee'), 
('Francis Ford Coppola'),('Francis Lawrence'), ('Alfred Hitchcock'), ('Stanley Kubrick'), 
('George Lucas'), ('Robert Zemeckis'),('Zack Snyder'), ('Michael Bay'), 
('Oliver Stone'), ('John Carpenter'), ('Brian De Palma'), 
('Wes Craven'), ('John Hughes'), ('John Landis'), ('Joss Whedon'),
('J.J. Abrams'), ('Sam Raimi'), ('Joel Coen'), ('Ethan Coen'), 
('Paul Thomas Anderson'), ('David Lynch'), ('Darren Aronofsky'), 
('Pedro Almodóvar'), ('Lars von Trier'), 
('Ingmar Bergman'), ('Federico Fellini'), ('Akira Kurosawa'), 
('Hayao Miyazaki'), ('Sergio Leone'), ('Jean-Luc Godard'), 
('François Truffaut'), ('Michelangelo Antonioni'), ('Bernardo Bertolucci'), 
('Luchino Visconti'), ('Vittorio De Sica'), ('Roberto Rossellini'), 
('Fritz Lang'), ('John Huston'), ('Howard Hawks'), 
('Orson Welles'), ('Frank Capra'), ('George Cukor'), ('William Wyler'), 
('John Ford'), ('Michael Curtiz'), ('Victor Fleming'), 
('Cecil B. DeMille'), ('King Vidor'), ('George Stevens'), ('Fred Zinnemann'), 
('Elia Kazan'), ('Joseph L. Mankiewicz'), ('Vincente Minnelli'), 
('Billy Wilder'), ('Delbert Mann'), ('Jerome Robbins'), ('Robert Wise'), 
('Tony Richardson'), 
('Mike Nichols'), ('Carol Reed'), ('Franklin J. Schaffner'), 
('William Friedkin'), ('Milos Forman'), ('Robert Redford'), ('Warren Beatty'), 
('Richard Attenborough'), ('Sydney Pollack'), ('Kevin Costner'), 
('Jonathan Demme'), ('Mel Gibson'), ('Ron Howard'), 
('Anthony Minghella'), ('Sam Mendes'), ('Steven Soderbergh'), 
('Danny Boyle'), ('Kathryn Bigelow'), ('Tom Hooper'), ('Michel Hazanavicius'), 
('Ang Lee'), ('Alfonso Cuarón'), ('Alejandro González Iñárritu'), ('Damien Chazelle'), 
('Guillermo del Toro'), ('Bong Joon-ho'), ('Chloé Zhao'), 
('David Cronenberg'), ('David O. Russell'), ('David Ayer'), 
('David Twohy'), ('David Gordon Green'), ('David Dobkin'), ('David Koepp'), 
('David Mamet'),('David Zucker'), 
('David Wain'), ('David Schwimmer'),
('John McTiernan'), ('John Woo'), 
('John Sturges'), ('John Frankenheimer'), 
('John Waters'), ('John Singleton'), 
('John Sayles'), ('John Lasseter'), ('John Boorman'), 
('John Milius'), ('John Badham'), ('John G. Avildsen'), 
('John Glen');


INSERT INTO filme(titulo_original, titulo_brasil, sinopse, ano_lancamento, poster_url, pas_origem, duracao, id_diretor, class_indicativo) VALUES
('Inside Out 2', 'Divertida Mente 2', 'Com um salto temporal, Riley se encontra mais velha, passando pela tão temida adolescência. Junto com o amadurecimento, a sala de controle também está passando por uma adaptação para dar lugar a algo totalmente inesperado: novas emoções. As já conhecidas, Alegria, Raiva, Medo, Nojinho e Tristeza não têm certeza de como se sentir quando novos inquilinos chegam ao local.', 2024, 'https://s2-gshow.glbimg.com/dNCoZiC_keIRzhEw4UmfREovP9g=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/Y/Q/t3mVQNQu6qdzvBjCthUg/divertidamente-divertida-mente-ansiedade-alegria-inside-out-filme-pixar.jpg', 'EUA', 96, 1, 'Livre'),
('Interstellar', 'Interestelar', 'As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie. Cooper é chamado para liderar o grupo e aceita a missão sabendo que pode nunca mais ver os filhos. Ao lado de Brand, Jenkins e Doyle, ele seguirá em busca de um novo lar.', 2014, 'https://beam-images.warnermediacdn.com/BEAM_LWM_DELIVERABLES/aa5b9295-8f9c-44f5-809b-3f2b84badfbf/8a7dd34b09c9c25336a3d850d4c431455e1aaaf0.jpg?host=wbd-images.prod-vod.h264.io&partner=beamcom', 'EUA', 169, 4, '10');


INSERT INTO categorias_filmes (num_filme, id_categoria) VALUES
(1, 1),  
(1, 2),  
(2, 3),  
(2, 4);  


INSERT INTO exibicao (num_filme, num_canal, data_exibicao) VALUES
(1, 7, '2024-09-18 00:00:00'),
(2, 12, '2024-09-18 04:30:00');