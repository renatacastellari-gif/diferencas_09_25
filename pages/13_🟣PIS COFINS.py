

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


st.write("")
st.write("")




# Texto explicativo em Markdown
st.markdown("""
⚠️ Diferença no Item **LB APONTADOR**
- **Razão (Nota Fiscal):** Não tributou
- **Apuração:** Tributou normalmente (COFINS informado)
""")

# Dados corretos extraídos da tabela
data = {
    "referencia": [
        "000129567-015","000203701-002","000203468-002","000212587-003",
        "000245624-004","000246830-004","000389017-005","000389299-005","000390046-005"
    ],
    "NUM_DOCFIS": [
        "000129567","000203701","000203468","000212587",
        "000245624","000246830","000389017","000389299","000390046"
    ],
    "VLR_COFINS": [1.00,0.94,0.94,0.96,1.21,1.21,1.09,2.06,1.03],
    "NUM_CONTROLE_DOCTO": [
        "0001916255","0001924937","0001922090","0001919108",
        "0001916696","0001922581","0001917137","0001919059","0001924521"
    ],
    "DATA_EMISSAO": [
        "01/09/2025","26/09/2025","17/09/2025","08/09/2025",
        "01/09/2025","18/09/2025","02/09/2025","08/09/2025","25/09/2025"
    ],
    "COD_PRODUTO": ["908920001BR"]*9,
    "DESCRICAO_COMPL": ["LB APONTADOR DUO"]*9
}

# Criar DataFrame
df = pd.DataFrame(data)

# Adicionar coluna de diferença (Razão não tributou, então diferença = VLR_COFINS)
df["Dif_COFINS"] = df["VLR_COFINS"]  # porque Razão = 0

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Exibir no Streamlit
st.subheader("📊 Diferença de tributação (Razão vs Apuração)")
st.dataframe(df.style.format(precision=2).applymap(highlight_dif, subset=['Dif_COFINS']))


