import streamlit as st
import calendar
from datetime import datetime

# Configuração da página para ocupar a tela toda
st.set_page_config(page_title="Luna Beauty Calendar", layout="wide")

# --- ESTILO CSS PARA O LOOK "CALENDÁRIO DE MESA" ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    
    /* Título */
    .titulo { text-align: center; color: #9d4edd; font-family: 'serif'; font-size: 3rem; margin-bottom: 20px; }

    /* Estilo da Tabela do Calendário */
    .calendar-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 10px;
        table-layout: fixed;
    }
    
    .calendar-table th {
        color: #7b2cbf;
        text-align: center;
        font-size: 1.2rem;
        padding-bottom: 10px;
    }

    .dia-celula {
        background: #161a23;
        border: 1px solid #3c096c;
        border-radius: 15px;
        height: 120px;
        padding: 10px;
        transition: 0.3s;
        position: relative;
    }

    .dia-celula:hover {
        border-color: #ff00ff;
        background: #1e1e2e;
        transform: translateY(-5px);
    }

    .num-dia { font-size: 1.5rem; font-weight: bold; color: #9d4edd; }
    .hoje { border: 2px solid #ff00ff !important; box-shadow: 0 0 15px #ff00ff; }
    
    .event-dot {
        height: 8px;
        width: 8px;
        background-color: #ff00ff;
        border-radius: 50%;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE CONTEÚDO ---
def get_skincare(dia):
    # Exemplo de rotina fixa por dia da semana ou fase
    rotinas = {
        0: ("Segunda", "🧘 Detox", ["Limpeza profunda", "Argila Verde"]),
        1: ("Terça", "✨ Brilho", ["Vitamina C", "Esfoliação"]),
        2: ("Quarta", "💧 Hidratação", ["Máscara de Tecido", "Ácido Hialurônico"]),
        3: ("Quinta", "🛡️ Proteção", ["Niacinamida", "Protetor Solar FPS 50"]),
        4: ("Sexta", "🍷 Reparo", ["Retinol", "Creme de Noite"]),
        5: ("Sábado", "🛀 Spa Day", ["Banho relaxante", "Óleos corporais"]),
        6: ("Domingo", "💤 Descanso", ["Bálsamo labial", "Dormir cedo"]),
    }
    return rotinas[dia]

# --- INTERFACE ---
st.markdown("<h1 class='titulo'>🌙 My Beauty Calendar</h1>", unsafe_allow_html=True)

hoje = datetime.now()
ano, mes = hoje.year, hoje.month
nome_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"][mes-1]

# Colunas para organizar o layout
col_cal, col_info = st.columns([3, 1])

with col_cal:
    st.subheader(f"{nome_mes} {ano}")
    
    # Gerar a grade do calendário
    cal = calendar.monthcalendar(ano, mes)
    dias_nome = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
    
    # Criando a tabela em HTML
    html_cal = "<table class='calendar-table'><thead><tr>"
    for d in dias_nome:
        html_cal += f"<th>{d}</th>"
    html_cal += "</tr></thead><tbody>"

    for semana in cal:
        html_cal += "<tr>"
        for i, dia in enumerate(semana):
            if dia == 0:
                html_cal += "<td></td>"
            else:
                classe_hoje = "hoje" if dia == hoje.day else ""
                # Pegar info da rotina
                data_obj = datetime(ano, mes, dia)
                nome_fase, acao, _ = get_skincare(data_obj.weekday())
                
                html_cal += f"""
                <td>
                    <div class="dia-celula {classe_hoje}">
                        <span class="num-dia">{dia}</span><br>
                        <span style="font-size:0.7rem; color:#aaa;">{acao}</span><br>
                        <span class="event-dot"></span>
                    </div>
                </td>
                """
        html_cal += "</tr>"
    html_cal += "</tbody></table>"
    st.markdown(html_cal, unsafe_allow_html=True)

with col_info:
    st.markdown("### 🔍 Detalhes do Dia")
    dia_selecionado = st.number_input("Selecione um dia para ver a rotina:", 1, 31, hoje.day)
    
    try:
        data_sel = datetime(ano, mes, int(dia_selecionado))
        dia_semana, foco, produtos = get_skincare(data_sel.weekday())
        
        st.info(f"**{dia_semana} - {foco}**")
        for p in produtos:
            st.write(f"- [ ] {p}")
    except:
        st.error("Dia inválido para este mês.")

    st.divider()
    st.write("📖 **Diário:**")
    st.text_area("Como está sua pele hoje?", placeholder="Escreva aqui...")
