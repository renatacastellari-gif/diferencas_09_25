

import streamlit as st
import pandas as pd
import io


# Configuração da página
st.set_page_config(page_title="ICMS Recuperar", page_icon="🟣")


# Cabeçalho
st.image('teste.svg', width=300)
st.title('COFINS')
("""**`COFINS a Recolher - 2300394`** """)

st.markdown("""
Esta página apresenta as demonstrações das conciliações entre o ICMS e o Razão Contábil.

### 📌 Origem dos Dados
- Fonte Fiscal: Apuração Fiscal
- Fonte Contábil: Conta 23000394 do razão extraída do SAP
""")
st.write("")
st.write("")

st.markdown("""
 ⚠️ Diferença no Item **BASE LIQ FACIAL UP FPS 15 SOFT HONEY**
- **Razão (Nota Fiscal):** Tributando em **7,60%**
- **Apuração:** Tributando em **10,30%**
""")
	


# Dados extraídos da tabela fornecida
data = {
    "referencia": ["000059786-018","000079835-016","000080293-016","000114108-010","000129528-015","000155650-009","000245555-004","000246215-004","000389947-005"],
    "NUM_DOCFIS": ["000059786","000079835","000080293","000114108","000129528","000155650","000245555","000246215","000389947"],
    "DATA_EMISSAO": ["14/09/2025","02/09/2025","24/09/2025","01/09/2025","01/09/2025","08/09/2025","01/09/2025","09/09/2025","23/09/2025"],
    "DESCRICAO_COMPL": ["BASE LIQ FACIAL UP FPS 15 SOFT HONEY"]*9,
    "VLR_ALIQ_ICMS_RAZAO": [7.6]*9,  # conforme informado na nota fiscal
    "VLR_ALIQ_ICMS_APURACAO": [10.3]*9,  # conforme apuração
    "VLR_UNIT": [106.1,121.32,121.32,129.83,92,121.32,71.24,80.03,121.32],
    "QUANTIDADE": [1,1,1,5,2,1,5,1,1],
    "TOTAL_ITEM": [106.10,121.32,121.32,649.15,184.00,121.32,356.20,80.03,121.32]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Calcular diferença percentual
df["Dif_Alíquota"] = df["VLR_ALIQ_ICMS_APURACAO"] - df["VLR_ALIQ_ICMS_RAZAO"]

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Exibir no Streamlit
st.subheader("📊 Diferença de Alíquota ICMS (Razão vs Apuração)")
st.dataframe(df.style.format(precision=2).applymap(highlight_dif, subset=['Dif_Alíquota']))









