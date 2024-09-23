from Ravendb import get_store


# Defina a classe do filme
from Ravendb import get_store

class Film:
    def __init__(self, titulo_original, titulo_brasil, sinopse, ano_lancamento, poster_url, pas_origem, duracao, id_diretor, class_indicativo, exibicoes=None):
        self.titulo_original = titulo_original
        self.titulo_brasil = titulo_brasil
        self.sinopse = sinopse
        self.ano_lancamento = ano_lancamento
        self.poster_url = poster_url
        self.pas_origem = pas_origem
        self.duracao = duracao
        self.id_diretor = id_diretor    
        self.class_indicativo = class_indicativo
        self.exibicoes = exibicoes if exibicoes else []

# Função para adicionar filmes com ID gerado automaticamente pelo RavenDB
def add_movies(movies):
    store = get_store()
    with store.open_session() as session:
        for movie in movies:
            film = Film(**movie)  # Cria uma instância da classe Film
            session.store(film)   # Deixa o RavenDB gerar o ID automaticamente
        session.save_changes()

        # Recuperar e exibir os IDs gerados
        for movie in movies:
            film_id = session.advanced.get_document_id(film)
            print(f"Filme inserido com ID: {film_id}")

exhibitions_inside_out = [
    {"num_canal": "channels/7-A", "data_exibicao": '2024-09-18 00:00:00'},
    {"num_canal": "channels/12-A", "data_exibicao": '2024-09-18 04:30:00'},
]

exhibitions_interstellar = [
    {"num_canal": "channels/10-A", "data_exibicao": '2024-09-25 10:30:00'},
    {"num_canal": "channels/4-A", "data_exibicao": '2024-09-30 15:00:00'},
]

exhibitions_shape_of_water = [
    {"num_canal": "channels/1-A", "data_exibicao": '2024-09-17 08:30:00'},
    {"num_canal": "channels/7-A", "data_exibicao": '2024-09-18 11:00:00'}
]
exhibitions_The_Dark_Knight = [
    {"num_canal": "channels/11-A", "data_exibicao": '2024-10-06 10:50:00'},
    {"num_canal": "channels/11-A", "data_exibicao": '2024-07-22 23:00:00'}
]
exhibitions_clube_da_luta = [
    {"num_canal": "channels/4-A", "data_exibicao": '2024-08-25 20:30:00'},
    {"num_canal": "channels/1-A", "data_exibicao": '2024-09-23 23:00:00'}
]

exhibitions_coco = [
    {"num_canal": "channels/14-A", "data_exibicao": '2024-11-11 14:30:00'},
    {"num_canal": "channels/14-A", "data_exibicao": '2024-09-23 11:00:00'}
]

exhibitions_Mad_Max = [
    {"num_canal": "channels/1-A", "data_exibicao": '2024-12-11 11:30:00'},
    {"num_canal": "channels/14-A", "data_exibicao": '2024-10-21 06:00:00'}
]

novos_filmes = [
    {
        "titulo_original": "Inside Out 2",
        "titulo_brasil": "Divertida Mente 2",
        "sinopse": "Com um salto temporal, Riley se encontra mais velha...",
        "ano_lancamento": 2024,
        "poster_url": "https://s2-gshow.glbimg.com/dNCoZiC_keIRzhEw4UmfREovP9g=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/Y/Q/t3mVQNQu6qdzvBjCthUg/divertidamente-divertida-mente-ansiedade-alegria-inside-out-filme-pixar.jpg",
        "pas_origem": "EUA",
        "duracao": 96,
        "id_diretor": "directors/1-A",
        "class_indicativo": "Livre",
        "exibicoes": exhibitions_inside_out
        
    },
    {
        "titulo_original": "Interstellar",
        "titulo_brasil": "Interestelar",
        "sinopse": "As reservas naturais da Terra estão chegando ao fim...",
        "ano_lancamento": 2014,
        "poster_url": "https://beam-images.warnermediacdn.com/BEAM_LWM_DELIVERABLES/aa5b9295-8f9c-44f5-809b-3f2b84badfbf/8a7dd34b09c9c25336a3d850d4c431455e1aaaf0.jpg?host=wbd-images.prod-vod.h264.io&partner=beamcom",
        "pas_origem": "EUA",
        "duracao": 169,
        "id_diretor": "directors/2-A",
        "class_indicativo": "10",
        "exibicoes": exhibitions_interstellar

    },
      {
        "titulo_original": "Inception",
        "titulo_brasil": "A Origem",
        "sinopse": "Dom Cobb é um ladrão habilidoso, o melhor na perigosa arte da extração, que rouba segredos valiosos do fundo do subconsciente durante o estado de sonho, quando a mente está mais vulnerável. A rara habilidade de Cobb fez dele um cobiçado jogador nesse traiçoeiro novo mundo de espionagem corporativa, mas também fez dele um fugitivo internacional e custou-lhe tudo o que já amou.",
        "ano_lancamento": 2010,
        "poster_url": "https://i0.wp.com/ovicio.com.br/wp-content/uploads/2020/08/20200802-filme-a-origem.jpg",
        "pas_origem": "EUA",
        "duracao": 148,
        "id_diretor": "directors/2-A",
        "class_indicativo": "12",
    },
    {
        "titulo_original": "The Matrix",
        "titulo_brasil": "Matrix",
        "sinopse": "Um jovem programador é atormentado por estranhos pesadelos nos quais se vê conectado por cabos a um imenso sistema de computadores do futuro. Em todas as noites, ele acorda com a mesma pergunta: o que é a Matrix? A resposta o leva a um submundo onde ele descobre que a vida que conhece é uma ilusão criada por uma inteligência cibernética, para que os humanos nunca percebam a verdade.",
        "ano_lancamento": 1999,
        "poster_url": "https://rollingstone.com.br/media/uploads/carrie-anne_moss_e_keanu_reeves_em_matrix_foto_divulgacao.jpg",
        "pas_origem": "EUA",
        "duracao": 136,
        "id_diretor": "directors/3-A",
        "class_indicativo": "16"
    },
    {
        "titulo_original": "Parasite",
        "titulo_brasil": "Parasita",
        "sinopse": "Toda a família de Ki-taek está desempregada, vivendo em um porão sujo e apertado. Um dia, seu filho consegue um emprego como tutor de uma garota rica, iniciando uma série de eventos que colocam as duas famílias em rota de colisão.",
        "ano_lancamento": 2019,
        "poster_url": "https://diplomatique.org.br/wp-content/uploads/2020/01/filme-parasita.jpg",
        "pas_origem": "Coreia do Sul",
        "duracao": 132,
        "id_diretor": "directors/4-A",
        "class_indicativo": "16"
    },
    {
        "titulo_original": "The Godfather",
        "titulo_brasil": "O Poderoso Chefão",
        "sinopse": "A saga da família Corleone, uma das mais poderosas da máfia italiana nos Estados Unidos, liderada por Don Vito Corleone. Quando o patriarca da família é quase morto, seu filho Michael assume o controle dos negócios, iniciando uma violenta guerra entre as famílias mafiosas.",
        "ano_lancamento": 1972,
        "poster_url": "https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9c272e7-4e43-4b20-9407-de4e14638a34_1000x563.jpeg",
        "pas_origem": "EUA",
        "duracao": 175,
        "id_diretor": "directors/5-A",
        "class_indicativo": "18"
    },
     {
        "titulo_original": "The Shawshank Redemption",
        "titulo_brasil": "Um Sonho de Liberdade",
        "sinopse": "Dois homens presos desenvolvem um vínculo ao longo de vários anos, encontrando consolo e redenção através de atos de decência comum.",
        "ano_lancamento": 1994,
        "poster_url": "https://media.gazetadopovo.com.br/2022/04/15182712/usdl.jpg",
        "pas_origem": "EUA",
        "duracao": 142,
        "id_diretor": "directors/6-A",
        "class_indicativo": "16"
    },
    {
        "titulo_original": "Pulp Fiction",
        "titulo_brasil": "Pulp Fiction: Tempo de Violência",
        "sinopse": "As vidas de dois assassinos de aluguel, um boxeador, a esposa de um gângster e dois bandidos se entrelaçam em quatro histórias de violência e redenção.",
        "ano_lancamento": 1994,
        "poster_url": "https://m.media-amazon.com/images/S/pv-target-images/c55624c14560ba8f1604fcb95f590d62889c476a78d0ccf6de60feda54237f6a._SX1080_FMjpg_.jpg",
        "pas_origem": "EUA",
        "duracao": 154,
        "id_diretor": "directors/7-A",
        "class_indicativo": "18"
    },
    {
        "titulo_original": "The Dark Knight",
        "titulo_brasil": "Batman: O Cavaleiro das Trevas",
        "sinopse": "Quando o Coringa emerge como uma nova ameaça, Batman deve aceitar um dos maiores testes psicológicos e físicos de sua capacidade de lutar contra a injustiça.",
        "ano_lancamento": 2008,
        "poster_url": "https://m.media-amazon.com/images/I/51k0qa6q0oL._AC_.jpg",
        "pas_origem": "EUA",
        "duracao": 152,
        "id_diretor": "directors/2-A",
        "class_indicativo": "12",
        "exibicoes": exhibitions_The_Dark_Knight
    },
    {
        "titulo_original": "Forrest Gump",
        "titulo_brasil": "Forrest Gump: O Contador de Histórias",
        "sinopse": "A história de um homem simples e sua jornada extraordinária através de eventos históricos dos EUA.",
        "ano_lancamento": 1994,
        "poster_url": "https://m.media-amazon.com/images/I/61Kc8oZ3aKL._AC_SY679_.jpg",
        "pas_origem": "EUA",
        "duracao": 142,
        "id_diretor": "directors/8-A",
        "class_indicativo": "12"
    },
    {
        "titulo_original": "Fight Club",
        "titulo_brasil": "Clube da Luta",
        "sinopse": "Um homem deprimido que sofre de insônia encontra um vendedor de sabonetes e juntos formam um clube de luta clandestino que evolui para algo muito maior.",
        "ano_lancamento": 1999,
        "poster_url": "https://rollingstone.com.br/media/_versions/brad-pitt-edward-norton-clube-da-luta-reprod_widelg.jpg",
        "pas_origem": "EUA",
        "duracao": 139,
        "id_diretor": "directors/9-A",
        "class_indicativo": "18",
        "exibicoes": exhibitions_clube_da_luta
    },
    {
        "titulo_original": "Inglourious Basterds",
        "titulo_brasil": "Bastardos Inglórios",
        "sinopse": "Durante a Segunda Guerra Mundial, um grupo de soldados judeus americanos conhecidos como 'Os Bastardos' espalha medo entre o Terceiro Reich ao realizar assassinatos brutais.",
        "ano_lancamento": 2009,
        "poster_url": "https://m.media-amazon.com/images/I/81tK5xXbQPL._AC_SY679_.jpg",
        "pas_origem": "DE",
        "duracao": 153,
        "id_diretor": "directors/7-A",
        "class_indicativo": "18"
    },
     {
        "titulo_original": "Coco",
        "titulo_brasil": "Viva: A Vida é uma Festa",
        "sinopse": "Um jovem aspirante a músico embarca em uma jornada na Terra dos Mortos para descobrir a verdade sobre sua família e seu legado.",
        "ano_lancamento": 2017,
        "poster_url": "https://cinemacao.com/wp-content/uploads/2018/01/Viva-A-Vida-E-Uma-Festa-2.jpg",
        "pas_origem": "EUA",
        "duracao": 105,
        "id_diretor": "directors/10-A",
        "class_indicativo": "Livre",
        "exibicoes": exhibitions_coco
    },
    {
        "titulo_original": "Mad Max",
        "titulo_brasil": "Mad Max: Estrada da Fúria",
        "sinopse": "Em um mundo pós-apocalíptico, Max ajuda um grupo de mulheres a escapar de um tirano que as mantém prisioneiras.",
        "ano_lancamento": 2015,
        "poster_url": "https://m.media-amazon.com/images/I/71j5Zy9v4cL._AC_SY679_.jpg",
        "pas_origem": "Austrália",
        "duracao": 120,
        "id_diretor": "directors/11-A",
        "class_indicativo": "16",
        "exibicoes": exhibitions_Mad_Max
    },
    {
        "titulo_original": "The Social Network",
        "titulo_brasil": "A Rede Social",
        "sinopse": "A história da criação do Facebook e a batalha judicial que se seguiu.",
        "ano_lancamento": 2010,
        "poster_url": "https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia13405/a-rede-social-cursos-cpt.jpg",
        "pas_origem": "EUA",
        "duracao": 120,
        "id_diretor": "directors/9-A",
        "class_indicativo": "12"
    },
    {
        "titulo_original": "The Grand Budapest Hotel",
        "titulo_brasil": "O Grande Hotel Budapeste",
        "sinopse": "As aventuras de um concierge lendário em um famoso hotel europeu entre as guerras.",
        "ano_lancamento": 2014,
        "poster_url": "https://www.pjf.mg.gov.br/noticias/arquivo/18%2008%20Sessao%20Cidadao_175702.jpeg",
        "pas_origem": "HUN",
        "duracao": 120,
        "id_diretor": "directors/12-A",
        "class_indicativo": "12"
    },
     {
        "titulo_original": "The Shape of Water",
        "titulo_brasil": "A Forma da Água",
        "sinopse": "Em um laboratório secreto do governo, uma zeladora muda se apaixona por uma criatura aquática presa.",
        "ano_lancamento": 2017,
        "poster_url": "https://ogimg.infoglobo.com.br/in/22353040-c59-70e/FT1500A/690/image.jpg",
        "pas_origem": "EUA",
        "duracao": 120,
        "id_diretor": "directors/13-A",
        "class_indicativo": "16",
        "exibicoes": exhibitions_shape_of_water
    },
    {
        "titulo_original": "The Revenant",
        "titulo_brasil": "O Regresso",
        "sinopse": "Um caçador de peles é deixado para morrer por seus companheiros após ser atacado por um urso. Ele sobrevive e parte em busca de vingança.",
        "ano_lancamento": 2015,
        "poster_url": "https://blogdescalada.com/critica-do-filme-o-regresso/critica-o-regresso-6/",
        "pas_origem": "EUA",
        "duracao": 156,
        "id_diretor": "directors/14-A",
        "class_indicativo": "16"
    },
    {
    "titulo_original": "Zootopia",
    "titulo_brasil": "Zootopia: Essa Cidade é o Bicho",
    "sinopse": "Em uma cidade de animais antropomórficos, uma coelha policial e uma raposa trapaceira devem trabalhar juntas para desvendar uma conspiração.",
    "ano_lancamento": 2016,
    "poster_url": "https://cfnoticias.com.br/wp-content/uploads/2016/03/1-Zootopia-2.jpg",
    "pas_origem": "EUA",
    "duracao": 108,
    "id_diretor": "directors/15-A",
    "class_indicativo": "Livre"
    },
]

