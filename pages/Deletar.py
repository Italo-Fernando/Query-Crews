import streamlit as st
from datetime import time

# Lista de canais de exemplo
canais = ['SBT','Globo','Record','Band','RedeTV','Cultura','TVB','Futura','EI','Fox Sports','HBO','CNN','Disney','CN','NatGeo','Discovery','MTV','Nick','Telecine','History' ]

# Título da aplicação
st.title("Deletar Filme")

# Input para o nome do filme
nome_filme = st.text_input("Nome do Filme")

# Selectbox para escolher o canal
canal_filme = st.selectbox("Canal", options=canais)

# Input para o horário que o filme seria passado
# Usar time_input para permitir a seleção de horário
horario_filme = st.time_input("Horário", value=time(0, 0))  # Valor padrão é 00:00

# Botão para deletar o filme
if st.button("Deletar Filme"):
    st.write(f"Você está tentando deletar o filme '{nome_filme}' que seria exibido no canal '{canal_filme}' às {horario_filme.strftime('%H:%M')}.")