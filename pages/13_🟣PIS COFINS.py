

import streamlit as st
import pandas as pd
import io


# Configuração da página
st.set_page_config(page_title="COFINS", page_icon="🟣")


# Cabeçalho
st.image('teste.svg', width=300)
st.title('COFINS')
("""**`COFINS a Recolher - 2300394`** """)

st.markdown("""
Esta página apresenta as demonstrações das conciliações do COFINS a recolher.

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
- **Apuração:** Tributou normalmente
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




st.write("")
st.write("")

# Texto explicativo em Markdown
st.markdown("""
⚠️ 77 Notas com valor fiscal sem razão
- **Razão (Nota Fiscal):** Sem tributação
- **Apuração:** Tributado 
""")


# Dados (sem DATA_EMISSAO)
data = {
    "VLR_COFINS": [
        43.77,47.82,30.14,11.89,5.73,17.61,48.99,0.94,79.71,20.83,82.38,15.48,17.19,107.72,114.20,4.62,10.81,114.09,
        220.18,95.06,44.92,26.65,27.85,15.58,69.50,67.40,41.42,41.10,9.23,8.35,50.67,72.89,128.04,76.00,77.50,153.53,
        27.92,110.20,3.32,30.47,18.29,34.45,19.99,16.21,45.08,180.65,13.79,134.94,13.47,23.12,20.04,28.98,24.51,1.26,
        33.19,2.70,85.19,13.47,13.47,58.87,7.54,13.21,12.80,3.09,63.17,73.79,18.38,105.27,12.54,142.78,171.46,26.42,
        80.44,60.08,15.69,26.72
    ],
    "NF_FISCAL": [
        "000114153-010","000114352-010","000129577-015","000130035-015","000130038-015","000130311-015","000156124-009","000203081-002",
        "000388867-005","000388906-005","000388927-005","000389013-005","000389084-005","000389088-005","000389093-005","000389187-005",
        "000389199-005","000389202-005","000389280-005","000389282-005","000389284-005","000389287-005","000389288-005","000389291-005",
        "000389335-005","000389339-005","000389352-005","000389369-005","000389370-005","000389424-005","000389436-005","000389452-005",
        "000389484-005","000389491-005","000389493-005","000389514-005","000389530-005","000389534-005","000389537-005","000389585-005",
        "000389591-005","000389602-005","000389607-005","000389638-005","000389764-005","000389766-005","000389789-005","000389802-005",
        "000389809-005","000389835-005","000389839-005","000389868-005","000389891-005","000389899-005","000389932-005","000389933-005",
        "000389969-005","000389971-005","000389972-005","000389982-005","000389984-005","000389992-005","000390033-005","000390034-005",
        "000390051-005","000390053-005","000390092-005","000390104-005","000390110-005","000390125-005","000390136-005","000390170-005",
        "000390212-005","000390234-005","000390263-005","000390306-005"
    ],
    "COD_ESTAB": [
        "0010","0010","0015","0015","0015","0015","0009","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002",
        "0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002",
        "0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002",
        "0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002","0002",
        "0002","0002"
    ],
    "CFOP": ["5102"]*76
}

# Ajustar listas para mesmo tamanho
min_len = min(len(v) for v in data.values())
for key in data:
    data[key] = data[key][:min_len]

# Criar DataFrame
df = pd.DataFrame(data)

# Função para destacar valores altos
def highlight_high(val):
    return 'background-color: #9b59b6; color: white;' if val > 100 else ''

# Exibir tabela estilizada
st.subheader("📊 Valor Fiscal")
st.dataframe(df.style.format(precision=2).applymap(highlight_high, subset=['VLR_COFINS']))
