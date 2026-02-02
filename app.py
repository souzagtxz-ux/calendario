import streamlit as st
import calendar
from datetime import datetime

# 1. Configuração de Tela Cheia
st.set_page_config(page_title="Calendário de Autocuidado", layout="wide")

# 2. Estilo CSS para a Tabela Roxo e Preto
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    
    /* Tabela de Calendário */
    .calendar-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 10px;
        table-layout: fixed;
    }
    
    .dia-celula {
        background: #161a23;
        border: 1px solid #3c096c;
        border-radius: 12px;
        height: 100px;
        padding: 10px;
        text-align: left;
        position: relative;
    }

    .num-dia { font-size: 1.4rem; font-weight: bold; color: #9d4edd; }
    .label-tarefa { font-size: 0.75rem; color: #aaa; display: block; margin-top: 5px; }
    .event-dot {
        height: 6px; width: 6px;
        background-color: #ff00ff;
        border-radius: 50%;
        display: inline-block;
        margin-top: 8px;
    }

    /* Estilizando os botões do Streamlit para ficarem invisíveis sobre a célula */
    .stButton > button {
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        height: 100px !important;
        width: 100% !important;
        position: absolute;
        top: 0; left: 0; z-index: 10;
    }
    
    .stButton > button:hover {
        background: rgba(157, 78, 221, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Base de Dados das Tarefas (O que aparece ao clicar)
tarefas_detalhadas = {
    0: {"label": "🧘 Detox", "itens": ["Limpeza dupla", "Chá de hibisco", "Máscara de argila"]},
    1: {"label": "✨ Brilho", "itens": ["Vitamina C", "Esfoliante suave", "Sérum iluminador"]},
    2: {"label": "💧 Hidratação", "itens": ["Ácido Hialurônico", "Máscara de tecido", "Beber 3L de água"]},
    3: {"label": "🛡️ Proteção", "itens": ["FPS 50", "Niacinamida", "Caminhada matinal"]},
    4: {"label": "🍷 Reparo", "itens": ["Retinol ou Peptídeos", "Creme nutritivo", "Óleo facial"]},
    5: {"label": "🛀 Spa Day", "itens": ["Banho longo", "Esfoliação corporal", "Hidratar o cabelo"]},
    6: {"label": "💤 Descanso", "itens": ["Dormir 8h", "Bálsamo labial", "Sem telas à noite"]}
}

st.markdown("<h1 style='text-align: center; color: #9d4edd;'>Meu Calendário</h1>", unsafe_allow_html=True)

# 4. Construção do Calendário
hoje = datetime.now()
ano, mes = hoje.year, hoje.month
cal = calendar.monthcalendar(ano, mes)
dias_nome = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

# Header dos dias
cols_header = st.columns(7)
for i, d in enumerate(dias_semana := ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SÁB"]):
    cols_header[i].markdown(f"<p style='text-align:center; color:#7b2cbf; font-weight:bold;'>{d}</p>", unsafe_allow_html=True)

# Grade do Calendário
for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia != 0:
            data_atual = datetime(ano, mes, dia)
            info = tarefas_detalhadas[data_atual.weekday()]
            
            with cols[i]:
                # Criamos a célula visual
                st.markdown(f"""
                    <div class="dia-celula">
                        <span class="num-dia">{dia}</span><br>
                        <span class="label-tarefa">{info['label']}</span><br>
                        <span class="event-dot"></span>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão invisível por cima para detectar o clique
                if st.button("", key=f"btn_{dia}"):
                    st.session_state['clicado'] = dia
                    st.session_state['detalhes'] = info

# 5. Painel de Detalhes (Aparece quando clica no quadrado)
if 'clicado' in st.session_state:
    st.divider()
    dia = st.session_state['clicado']
    info = st.session_state['detalhes']
    
    st.markdown(f"""
        <div style="background: #161a23; padding: 20px; border-radius: 15px; border-left: 5px solid #ff00ff;">
            <h2 style='color:#9d4edd; margin:0;'>📅 Dia {dia}: {info['label']}</h2>
            <p style='color:#aaa;'>Aqui está o que você precisa fazer hoje:</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### ✅ Lista de Uso:")
        for item in info['itens']:
            st.checkbox(item, key=f"check_{dia}_{item}")
    with col_b:
        st.write("### 📝 Notas:")
        st.text_area("Como está sua pele?", key=f"nota_{dia}")
