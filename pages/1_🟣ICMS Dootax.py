import streamlit as st
import pandas as pd

st.set_page_config(page_title="ICMS DOOTAX", page_icon="🟣")

st.image('teste.svg', width=300)
st.title('ICMS DOOTAX')
("""**`ICMS a RECOLHER - 2300391`** """)
st.markdown("""
Esta página apresenta as **demonstrações das conciliações entre o ICMS Difal (Dootax) e o Razão Contábil.**

### 📌 Origem dos Dados
- **Fonte Fiscal:** Planilha DOOTAX retirada do site Dootax (Filtro: Tipo de Tributo: ICMS)
- **Fonte Contábil:** Conta 2300391 (ICMS a recolher) do razão extraída do SAP  

### 🔍 Ocorrência Identificada
Valores lançados no razão com multa, **necessário reclassificar**.

---
""")

# Dados
data = {
    "Pagador": ["BRADESCO"]*6,
    "Tipo de Tributo": ["ICMS"]*6,
    "Data Vencimento": ["01/09/2025","02/09/2025","04/09/2025","09/09/2025","15/09/2025","17/09/2025"],
    "vlr_total": [493.62,195.22,25.01,103.21,39.52,19.06],
    "vlr_dootax": [493.54,195.21,25.00,103.20,39.49,19.03],
    "vlr_multa": [0.08,0.01,0.01,0.01,0.03,0.03],
    "dif": [-0.08,-0.01,-0.01,-0.01,-0.03,-0.03],
    "vlr_razao_40": [493.62,195.22,25.01,103.21,39.52,19.06],
    "Nº documento": [100279767,100280550,100281243,100282614,100285347,100286317],
    "Tipo doc": ["SA"]*6,
    "Data lançamento": ["01/09/2025","02/09/2025","04/09/2025","09/09/2025","15/09/2025","17/09/2025"],
    "Chave": [40]*6
}

df = pd.DataFrame(data)

# Função para destacar apenas vlr_multa em roxo
def highlight_multa(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Exibir tabela
st.subheader("📊 Diferenças DOOTAX vs RAZÃO")
st.dataframe(df.style.format(precision=2).applymap(highlight_multa, subset=['vlr_multa']))

# Objetivo no final
st.markdown("""
---
> **Objetivo:** Garantir que os saldos fiscais e contábeis estejam alinhados.
""")