import streamlit as st
import calendar
from datetime import datetime

# 1. Configuração de Tela Cheia
st.set_page_config(page_title="Calendário de Autocuidado", layout="wide")

# 2. CSS para o Visual Roxo/Preto e Clique
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    
    .dia-celula {
        background: #161a23;
        border: 1px solid #3c096c;
        border-radius: 12px;
        height: 110px;
        padding: 12px;
        position: relative;
    }
    .num-dia { font-size: 1.4rem; font-weight: bold; color: #9d4edd; }
    .label-tarefa { font-size: 0.7rem; color: #aaa; display: block; margin-top: 5px; }
    .event-dot {
        height: 6px; width: 6px;
        background-color: #ff00ff;
        border-radius: 50%;
        display: inline-block;
        margin-top: 8px;
    }

    /* Botão invisível sobre a célula */
    .stButton > button {
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        height: 110px !important;
        width: 100% !important;
        position: absolute;
        top: -110px;
        z-index: 10;
    }
    .stButton > button:hover { background: rgba(157, 78, 221, 0.1) !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Dicionário com 31 Tarefas Diferentes (Uma para cada dia)
tarefas_31_dias = {
    1: ["Limpeza Dupla", "Beber 3L de água", "Trocar fronha"],
    2: ["Esfoliação Química", "Chá de Camomila", "Meditação"],
    3: ["Máscara de Argila", "Caminhada 20min", "Hidratar cutículas"],
    4: ["Sérum Vitamina C", "Comer fruta", "Organizar skincare"],
    5: ["Gua Sha / Massagem", "Alongamento", "Sem açúcar hoje"],
    6: ["Ácido Hialurônico", "Dormir 8h", "Hidratar pescoço"],
    7: ["Spa Day Capilar", "Banho relaxante", "Fazer as unhas"],
    8: ["Máscara de Tecido", "Ler 10 páginas", "Lavar pincéis"],
    9: ["Patch de Olhos", "Chá Verde", "Postura correta"],
    10: ["Peeling Enzimático", "Sem celular 1h antes de dormir", "Massagem pés"],
    11: ["Sérum Niacinamida", "Comer salada", "Skincare corporal"],
    12: ["Bálsamo Labial", "Organizar looks", "Chá de hortelã"],
    13: ["Vapor Facial", "Treino 30min", "Drenagem manual"],
    14: ["Retinol (Noite)", "Beber 2L água", "Ouvir música"],
    15: ["Máscara Nutritiva", "Dia sem make", "Definir metas"],
    16: ["Creme Ceramidas", "Cuidar plantas", "Fio dental"],
    17: ["Vitamina C + FPS 50", "Menos café", "Agradecer 3 coisas"],
    18: ["Ice Roller (Gelo)", "Comer nozes", "Limpar celular"],
    19: ["Argila Branca", "Yoga / Pilates", "Hidratar mãos"],
    20: ["Esfoliação Labial", "Dormir cedo", "Banho gelado matinal"],
    21: ["Sérum Peptídeos", "Água com limão", "Planejar semana"],
    22: ["Detox de Pele", "15min de sol", "Usar perfume"],
    23: ["Tônico Facial", "Proteína de manhã", "Arrumar gaveta"],
    24: ["Máscara de Dormir", "Chá de Melissa", "Afirmações"],
    25: ["Limpeza Profunda", "Treino intenso", "Esfoliar pés"],
    26: ["Antioxidante", "Água de coco", "Ligar para amiga"],
    27: ["Hidratação Labial", "Chocolate amargo", "Desenhar/Escrever"],
    28: ["Revitalização", "Massagem ombros", "Checar validades"],
    29: ["Máscara Calmante", "Desligar avisos", "Limpar espelhos"],
    30: ["Banho de Sais", "Beber 3L água", "Visualizar amanhã"],
    31: ["Ritual Completo", "Auto-elogio", "Novo plano mensal"]
}

st.markdown("<h1 style='text-align: center; color: #9d4edd;'>Meu Autocuidado Diário</h1>", unsafe_allow_html=True)

# 4. Gerar Calendário
hoje = datetime.now()
cal = calendar.monthcalendar(hoje.year, hoje.month)
cols_header = st.columns(7)
for i, d in enumerate(["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SÁB"]):
    cols_header[i].markdown(f"<p style='text-align:center; color:#7b2cbf; font-weight:bold;'>{d}</p>", unsafe_allow_html=True)

for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia != 0:
            missao = tarefas_31_dias.get(dia, ["Tarefa básica", "Saúde", "Bem-estar"])
            with cols[i]:
                st.markdown(f"""<div class="dia-celula"><span class="num-dia">{dia}</span><br>
                                <span class="label-tarefa">{missao[0]}</span><br>
                                <span class="event-dot"></span></div>""", unsafe_allow_html=True)
                if st.button("", key=f"dia_{dia}"):
                    st.session_state['dia_ativo'] = dia
                    st.session_state['missao_ativa'] = missao

# 5. Painel de Informação (Aparece ao clicar)
if 'dia_ativo' in st.session_state:
    d = st.session_state['dia_ativo']
    m = st.session_state['missao_ativa']
    st.markdown(f"""<div style="background: #161a23; padding: 20px; border-radius: 15px; border-left: 5px solid #ff00ff; margin-top: 20px;">
        <h2 style='color:#9d4edd; margin:0;'>📅 Missão do Dia {d}</h2><hr style='border-color: #3c096c;'>
        <p style='font-size: 1.2rem;'><b>🧖 Pele:</b> {m[0]}</p>
        <p style='font-size: 1.2rem;'><b>🍎 Saúde:</b> {m[1]}</p>
        <p style='font-size: 1.2rem;'><b>🌟 Bem-estar:</b> {m[2]}</p></div>""", unsafe_allow_html=True)
else:
    st.info("👆 Clique em um dia para ver sua missão exclusiva.")
