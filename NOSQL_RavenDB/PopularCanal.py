from Ravendb import get_store

class Channel:
    def __init__(self, nome, sigla, logo_canal):
        self.nome = nome
        self.sigla = sigla
        self.logo_canal = logo_canal

# Função para adicionar canais
def add_channels(channels):
    store = get_store()
    with store.open_session() as session:
        for index, channel in enumerate(channels, start=1):
            channel_instance = Channel(**channel)  
            channel_id = f"channels/{index}"  
            session.store(channel_instance, channel_id)  
        session.save_changes()


channels = [
    {"nome": "Rede Globo", "sigla": "Globo", "logo_canal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1S3WHuIf9kmExAfpJDGzxYTMuBLgdlczp-w&s"},
    {"nome": "Sistema Brasileiro de Televisão", "sigla": "SBT", "logo_canal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcVYPc-pELbp8t_0EhGtRFsSj1gXPMQWJgwA&s"},
    {"nome": "RecordTV", "sigla": "Record", "logo_canal": "https://play-lh.googleusercontent.com/86YxRYXi1bikmEQInrLFY7913Ng0xgzwZPuXU5k7NWnePoxX4E6UxMK8I5axLJZqWsDb=w240-h480-rw"},
    {"nome": "Rede Bandeirantes", "sigla": "Band", "logo_canal": "https://cdn.worldvectorlogo.com/logos/band-1.svg"},
    {"nome": "RedeTV!", "sigla": "RedeTV", "logo_canal": "https://pbs.twimg.com/media/FywWpO1X0AAfD3B.jpg:large"},
    {"nome": "TV Cultura", "sigla": "Cultura", "logo_canal": "https://upload.wikimedia.org/wikipedia/commons/8/82/Cultura_logo_2013.svg"},
    {"nome": "TV Brasil", "sigla": "TVB", "logo_canal": "https://yt3.googleusercontent.com/fs6EI0tEgITiQzy3j5nXhp6hv9KBWYPMjqJTbPdH6ogzGnEI2P-lF9oBMlbku7bp1VXxcy8cxw=s176-c-k-c0x00ffffff-no-rj-mo"},
    {"nome": "Canal Futura", "sigla": "Futura", "logo_canal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLorEDMiv4WNKxoCRPxaPWfYPvc5ntwWgjVDKyRRbwVylAlOTLi0KyacUcjOfU6x8EZCY&usqp=CAU"},
    {"nome": "Esporte Interativo", "sigla": "EI", "logo_canal": "https://upload.wikimedia.org/wikipedia/commons/1/19/LOGO_EI-2.jpg"},
    {"nome": "Fox Sports", "sigla": "Fox Sports", "logo_canal": "https://logowik.com/content/uploads/images/fox-sports3529.jpg"},
    {"nome": "HBO Brasil", "sigla": "HBO", "logo_canal": "https://logowik.com/content/uploads/images/hbo.jpg"},
    {"nome": "CNN Brasil", "sigla": "CNN", "logo_canal": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgT-R52bE5nFi11FvXv3Er0ADTmXuBd3ieeQ&s"},
    {"nome": "MTV Brasil", "sigla": "MTV", "logo_canal": "https://cdn.dribbble.com/users/174209/screenshots/1465961/media/1956c5abb6840358546e32cf3298057a.jpg?resize=400x300&vertical=center"},
    {"nome": "Telecine", "sigla": "Telecine", "logo_canal": "https://gkpb.com.br/wp-content/uploads/2019/07/novo-logo-telecine-seu-momento-cinema-versao-negativa-1024x1024.jpg"}
]

