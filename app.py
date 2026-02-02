import streamlit as st
import calendar
from datetime import datetime, date

# Configuração para TELA CHEIA
st.set_page_config(page_title="Luna Care Fullscreen", layout="wide")

# --- ESTILO ROXO E PRETO (TELA CHEIA) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    
    /* Tira as margens padrão do Streamlit */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; max-width: 95%; }
    
    /* Estilo dos Botões de Data */
    div.stButton > button {
        width: 100%;
        height: 100px;
        background-color: #161a23;
        color: #9d4edd;
        border: 1px solid #3c096c;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #7b2cbf;
        color: white;
        border-color: #ff00ff;
    }

    /* Títulos e Textos */
    h1 { color: #9d4edd; text-shadow: 2px 2px #000; }
    .dia-semana { text-align: center; font-weight: bold; color: #7b2cbf; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE CONTEÚDO ---
def obter_detalhes(dia_ciclo):
    if 1 <= dia_ciclo <= 6:
        return "🩸 Fase Menstrual", "Hidratação Máxima", ["Beber 3L de água", "Creme de Ceramidas", "Massagem com óleo morno", "Evitar café"]
    elif 7 <= dia_ciclo <= 13:
        return "🌱 Fase Folicular", "Renovação e Brilho", ["Sérum Vitamina C", "Esfoliação Química", "Protetor Solar FPS 50", "Suco Verde"]
    elif 14 <= dia_ciclo <= 18:
        return "✨ Fase Ovulatória", "Glow e Proteção", ["Niacinamida", "Limpeza com Gel leve", "Caminhada ao ar livre", "Máscara de Argila Rosa"]
    else:
        return "🌑 Fase Lútea", "Controle de Oleosidade", ["Ácido Salicílico", "Drenagem Facial", "Chá de Camomila", "Adesivo secativo nas espinhas"]

# --- SIDEBAR (CONFIGURAÇÃO INVISÍVEL PARA TELA CHEIA) ---
with st.sidebar:
    st.header("Configurações")
    data_inicio = st.date_input("Início da última menstruação", value=date(2026, 1, 20))
    ciclo = st.number_input("Duração do Ciclo", value=28)
    st.divider()
    st.write("O calendário abaixo calcula automaticamente suas fases.")

# --- TELA PRINCIPAL ---
st.title("🌙 Calendário de Autocuidado Luna")

# Navegação de Mês
hoje = datetime.now()
ano, mes = hoje.year, hoje.month
cal = calendar.monthcalendar(ano, mes)
nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

st.subheader(f"{nomes_meses[mes-1]} de {ano}")

# Header dos Dias da Semana
dias_semana = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SÁB"]
cols_h = st.columns(7)
for i, d in enumerate(dias_semana):
    cols_h[i].markdown(f'<div class="dia-semana">{d}</div>', unsafe_allow_html=True)

# Grade do Calendário
for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia == 0:
            cols[i].write("") # Espaço vazio
        else:
            # Calcular dia do ciclo para esta data
            data_clicada = date(ano, mes, dia)
            delta = (data_clicada - data_inicio).days
            dia_ciclo = (delta % ciclo) + 1
            
            # Botão de Data
            if cols[i].button(f"{dia}", key=f"dia_{dia}"):
                # O que aparece quando clica
                fase, foco, lista = obter_detalhes(dia_ciclo)
                st.markdown(f"""
                    <div style="background: #1e1e2e; padding: 20px; border-radius: 15px; border-left: 5px solid #ff00ff; margin-top: 10px;">
                        <h2 style='margin-top:0;'>📅 Dia {dia}: {fase} (Dia {dia_ciclo} do ciclo)</h2>
                        <h3 style='color: #e0aaff;'>🎯 {foco}</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    st.write("### ✅ O que fazer:")
                    for item in lista:
                        st.write(f"🔹 {item}")
                with col_res2:
                    st.write("### 💊 Suplementação/Chás:")
                    st.write("- Magnésio (se houver cólica)")
                    st.write("- Chá específico para a fase")
                st.divider()

st.info("👆 Clique em qualquer número para ver sua rotina detalhada.")
