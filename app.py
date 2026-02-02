import streamlit as st
import calendar
from datetime import datetime

# Configuração de tela cheia e visual dark
st.set_page_config(page_title="Calendário Autocuidado", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    /* Estilizando os botões para parecerem células de calendário */
    div.stButton > button {
        height: 100px;
        background-color: #161a23;
        color: #9d4edd;
        border: 1px solid #3c096c;
        border-radius: 10px;
        font-size: 1.2rem;
    }
    div.stButton > button:hover {
        border-color: #ff00ff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Tarefas fixas
tarefas = {
    0: "🧘 Detox", 1: "✨ Brilho", 2: "💧 Hidratação", 
    3: "🛡️ Proteção", 4: "🍷 Reparo", 5: "🛀 Spa Day", 6: "💤 Descanso"
}

st.title("🌙 Meu Calendário de Autocuidado")

hoje = datetime.now()
cal = calendar.monthcalendar(hoje.year, hoje.month)
dias_nome = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

# Header dos dias
cols = st.columns(7)
for i, nome in enumerate(dias_nome):
    cols[i].markdown(f"<p style='text-align:center; color:#7b2cbf;'><b>{nome}</b></p>", unsafe_allow_html=True)

# Grade do Calendário usando Colunas do Streamlit (Mais seguro que HTML puro)
for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia != 0:
            data_atual = datetime(hoje.year, hoje.month, dia)
            label = tarefas[data_atual.weekday()]
            
            # Cada dia é um botão. Se clicar, mostra o que fazer.
            if cols[i].button(f"{dia}\n{label}", key=f"dia_{dia}"):
                st.session_state['selected_day'] = dia
                st.session_state['selected_task'] = label

# Painel de detalhes (Aparece quando você clica em um dia)
if 'selected_day' in st.session_state:
    st.divider()
    st.subheader(f"📅 Detalhes do Dia {st.session_state['selected_day']}")
    st.write(f"Sua missão de hoje é: **{st.session_state['selected_task']}**")
    st.checkbox("Feito!")
