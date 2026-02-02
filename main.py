import streamlit as st
import pandas as pd
import calendar
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Luna Care Pro", layout="wide", page_icon="🌙")

# --- CSS PERSONALIZADO (DARK & PURPLE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: #e0aaff; }
    h1, h2, h3 { color: #9d4edd !important; font-family: 'Segoe UI', sans-serif; }
    
    /* Calendário Grid */
    .cal-container { display: grid; grid-template-columns: repeat(7, 1fr); gap: 10px; }
    .dia-box {
        background: #161a23;
        border: 1px solid #3c096c;
        border-radius: 10px;
        padding: 15px;
        min-height: 140px;
        transition: 0.3s;
    }
    .dia-box:hover { border-color: #9d4edd; background: #1e1e2e; }
    .hoje { border: 2px solid #ff00ff !important; box-shadow: 0 0 10px #ff00ff; }
    
    .num-dia { font-size: 1.2rem; font-weight: bold; color: #ffffff; }
    .fase-tag { font-size: 0.7rem; color: #7b2cbf; font-weight: bold; }
    .skincare-item { font-size: 0.75rem; color: #b79ced; margin-top: 5px; list-style-type: none; }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #3c096c; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DADOS ---
def definir_rotina(dia_ciclo):
    if 1 <= dia_ciclo <= 5:
        return "🩸 Menstrual", "Foco: Hidratação e Calma", ["Limpador suave", "Ácido Hialurônico", "Creme Reparador"]
    elif 6 <= dia_ciclo <= 13:
        return "🌱 Folicular", "Foco: Brilho e Renovação", ["Vitamina C", "Esfoliante AHA", "Protetor Solar"]
    elif 14 <= dia_ciclo <= 16:
        return "✨ Ovulação", "Foco: Proteção Profunda", ["Niacinamida", "Máscara de Argila", "Antioxidante"]
    else:
        return "🌑 Lútea", "Foco: Controle de Oleosidade", ["Ácido Salicílico", "Tônico Matte", "Adesivo Secativo"]

# --- SIDEBAR (CONFIGURAÇÕES) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3663/3663363.png", width=80)
    st.title("Configurações")
    data_ref = st.date_input("Início da última menstruação", datetime.now() - timedelta(days=14))
    ciclo_medio = st.number_input("Média do Ciclo (dias)", 21, 40, 28)
    st.divider()
    st.write("🌙 **Dica do Dia:** Evite cafeína na fase lútea para reduzir cólicas.")

# --- SELEÇÃO DE MÊS ---
col_m1, col_m2 = st.columns([2, 1])
with col_m1:
    st.title("Calendário de Autocuidado")
with col_m2:
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes_selecionado = st.selectbox("Selecione o Mês", meses, index=datetime.now().month - 1)
    mes_idx = meses.index(mes_selecionado) + 1

# --- GERAR CALENDÁRIO ---
ano_atual = datetime.now().year
cal = calendar.monthcalendar(ano_atual, mes_idx)
dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

# Header dos dias da semana
cols_header = st.columns(7)
for i, d in enumerate(dias_semana):
    cols_header[i].markdown(f"<p style='text-align:center; font-weight:bold;'>{d}</p>", unsafe_allow_html=True)

# Corpo do Calendário
for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia != 0:
            data_atual = datetime(ano_atual, mes_idx, dia).date()
            # Cálculo do dia do ciclo
            diff = (data_atual - data_ref).days
            dia_ciclo = (diff % ciclo_medio) + 1
            
            nome_fase, foco, produtos = definir_rotina(dia_ciclo)
            
            # Classe CSS se for hoje
            classe_hoje = "hoje" if data_atual == datetime.now().date() else ""
            
            # Montar o Card HTML
            card_html = f"""
            <div class="dia-box {classe_hoje}">
                <div class="num-dia">{dia}</div>
                <div class="fase-tag">{nome_fase}</div>
                <div style="font-size: 0.7rem; color: #9d4edd; margin-bottom: 5px;">{foco}</div>
                <ul style="padding-left: 0; margin-top: 5px;">
                    {''.join([f'<li class="skincare-item">• {p}</li>' for p in produtos])}
                </ul>
            </div>
            """
            cols[i].markdown(card_html, unsafe_allow_html=True)

# --- PAINEL DE SINTOMAS ---
st.divider()
st.subheader("📝 Registro de Sintomas de Hoje")
c1, c2, c3 = st.columns(3)
with c1:
    st.select_slider("Energia", ["Exausta", "Baixa", "Normal", "Alta", "Incrível"])
with c2:
    st.multiselect("Sintomas", ["Cólica", "Dor de cabeça", "Inchaço", "Espinhas", "Sensibilidade nos seios"])
with c3:
    st.text_input("Nota pessoal", placeholder="Como você se sente hoje?")

if st.button("Salvar Diário"):
    st.toast("Dados salvos com sucesso!", icon="💜")
