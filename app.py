import streamlit as st
import calendar
from datetime import datetime

# 1. Configuração de Tela Cheia
st.set_page_config(page_title="Autocuidado Diário", layout="wide")

# 2. CSS - O visual exato que você pediu
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    
    /* Grade do Calendário */
    .dia-celula {
        background: #161a23;
        border: 1px solid #3c096c;
        border-radius: 12px;
        height: 110px;
        padding: 12px;
        position: relative;
        transition: 0.3s;
    }
    .dia-celula:hover { border-color: #ff00ff; background: #1e1e2e; }
    
    .num-dia { font-size: 1.4rem; font-weight: bold; color: #9d4edd; }
    .label-tarefa { font-size: 0.7rem; color: #aaa; display: block; margin-top: 5px; height: 30px; }
    .event-dot {
        height: 6px; width: 6px;
        background-color: #ff00ff;
        border-radius: 50%;
        display: inline-block;
        margin-top: 8px;
    }

    /* Botão invisível para detectar o clique no quadrado */
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
    </style>
    """, unsafe_allow_html=True)

# 3. Lista de 31 Tarefas Reais (Uma diferente para cada dia)
tarefas_31 = {
    1: ["Limpeza Dupla", "Beber 3L Água", "Trocar Fronha"],
    2: ["Esfoliação Química", "Chá de Camomila", "Meditação"],
    3: ["Máscara de Argila", "Caminhada 20min", "Hidratar Cutículas"],
    4: ["Vitamina C", "Comer Fruta", "Organizar Skincare"],
    5: ["Massagem Gua Sha", "Alongamento", "Sem Açúcar"],
    6: ["Ácido Hialurônico", "Dormir 8h", "Hidratar Pescoço"],
    7: ["Spa Capilar", "Banho Relaxante", "Fazer Unhas"],
    8: ["Máscara de Tecido", "Ler 10 Páginas", "Lavar Pincéis"],
    9: ["Patch de Olhos", "Chá Verde", "Postura Reta"],
    10: ["Peeling Enzimático", "Sem Telas à Noite", "Massagem Pés"],
    11: ["Niacinamida", "Comer Salada", "Creme Corporal"],
    12: ["Bálsamo Labial", "Organizar Looks", "Chá Hortelã"],
    13: ["Vapor Facial", "Treino 30min", "Drenagem Manual"],
    14: ["Retinol (Noite)", "Beber 2L Água", "Ouvir Música"],
    15: ["Máscara Nutritiva", "Dia sem Make", "Definir Metas"],
    16: ["Creme Ceramidas", "Cuidar Plantas", "Passar Fio Dental"],
    17: ["FPS 50 Reaplicado", "Menos Café", "Agradecer 3 coisas"],
    18: ["Ice Roller (Gelo)", "Comer Nozes", "Limpar Celular"],
    19: ["Argila Branca", "Yoga / Pilates", "Hidratar Mãos"],
    20: ["Esfoliação Labial", "Dormir Cedo", "Banho Gelado"],
    21: ["Peptídeos", "Água com Limão", "Planejar Semana"],
    22: ["Detox de Pele", "15min de Sol", "Usar Perfume"],
    23: ["Tônico Facial", "Proteína Manhã", "Arrumar Gaveta"],
    24: ["Máscara Noturna", "Chá de Melissa", "Afirmações"],
    25: ["Limpeza Profunda", "Treino Intenso", "Esfoliar Pés"],
    26: ["Antioxidante", "Água de Coco", "Ligar para Amigo"],
    27: ["Hidratação Boca", "Chocolate Amargo", "Escrever Diário"],
    28: ["Revitalização", "Massagem Ombros", "Validade Produtos"],
    29: ["Máscara Calmante", "Offline 1 hora", "Limpar Espelhos"],
    30: ["Banho com Sais", "Beber 3L Água", "Metas Próximo Mês"],
    31: ["Ritual Completo", "Auto-elogio", "Planejar Amanhã"]
}

st.markdown("<h1 style='text-align: center; color: #9d4edd;'>Autocuidado Diário</h1>", unsafe_allow_html=True)

# 4. Gerar Grade
hoje = datetime.now()
cal = calendar.monthcalendar(hoje.year, hoje.month)

# Header Dias da Semana
dias_header = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SÁB"]
cols_h = st.columns(7)
for i, d in enumerate(dias_header):
    cols_h[i].markdown(f"<p style='text-align:center; color:#7b2cbf; font-weight:bold;'>{d}</p>", unsafe_allow_html=True)

# Linhas do Calendário
for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia != 0:
            missao = tarefas_31.get(dia, ["-", "-", "-"])
            with cols[i]:
                # Visual da Célula
                st.markdown(f"""
                    <div class="dia-celula">
                        <span class="num-dia">{dia}</span><br>
                        <span class="label-tarefa">{missao[0]}</span><br>
                        <span class="event-dot"></span>
                    </div>
                """, unsafe_allow_html=True)
                # Clique
                if st.button("", key=f"btn_{dia}"):
                    st.session_state['dia_clicado'] = dia

# 5. Painel de Informação (Aparece ao clicar no dia)
if 'dia_clicado' in st.session_state:
    d = st.session_state['dia_clicado']
    m = tarefas_31[d]
    st.markdown(f"""
        <div style="background: #161a23; padding: 25px; border-radius: 15px; border-left: 5px solid #ff00ff; margin-top: 20px;">
            <h2 style='color:#9d4edd; margin:0;'>📅 O que fazer no Dia {d}</h2>
            <hr style='border-color: #3c096c;'>
            <p style='font-size: 1.2rem;'><b>🧖 Pele:</b> {m[0]}</p>
            <p style='font-size: 1.2rem;'><b>🍎 Saúde:</b> {m[1]}</p>
            <p style='font-size: 1.2rem;'><b>🌟 Bem-estar:</b> {m[2]}</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("👆 Clique em um dia para ver sua tarefa exclusiva.")
