from Ravendb import get_store
from datetime import datetime

class Exhibition:
    def __init__(self, num_filme, num_canal, data_exibicao):
        self.num_filme = num_filme
        self.num_canal = num_canal
        self.data_exibicao = data_exibicao

def add_exhibitions(exhibitions):
    store = get_store()
    with store.open_session() as session:
        for exhibition in exhibitions:
            exhibition_instance = Exhibition(**exhibition)
            data_str = datetime.strptime(exhibition['data_exibicao'], '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
            exhibition_id = f"exhibitions/{exhibition['num_filme']}_{exhibition['num_canal']}_{data_str}"  # Inclua a data no ID
            session.store(exhibition_instance, exhibition_id)
        session.save_changes()

exhibitions = [
    {"num_filme": "films/1", "num_canal": "channels/7", "data_exibicao": '2024-09-18 00:00:00'},
    {"num_filme": "films/2", "num_canal": "channels/12", "data_exibicao": '2024-09-18 04:30:00'},
    {"num_filme": "films/4", "num_canal": "channels/10", "data_exibicao": '2024-09-25 10:30:00'},
    {"num_filme": "films/8", "num_canal": "channels/4", "data_exibicao": '2024-09-30 15:00:00'},
    {"num_filme": "films/13", "num_canal": "channels/13", "data_exibicao": '2024-10-08 16:30:00'},
    {"num_filme": "films/1", "num_canal": "channels/7", "data_exibicao": '2024-10-01 08:30:00'},
]


