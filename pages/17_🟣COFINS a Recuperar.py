
import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="COFINS", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
# Título principal
st.markdown("""
<h2 style="
    color:#EEE4EF;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
COFINS
</h2>
""", unsafe_allow_html=True)
st.markdown("**`COFINS a Recuperar - 1280344`**")

st.markdown("""
Esta página apresenta as demonstrações das conciliações do COFINS a recuperar.

### 📌 Origem dos Dados
- Fonte Fiscal: Apuração Fiscal
- Fonte Contábil: Conta 1280344 do razão extraída do SAP
""")

st.markdown("---")

# Título estilizado
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade (alíquota)</p>",
    unsafe_allow_html=True
)

# Dados exemplo
data = {
    "Nota_Fiscal": ["000881877"],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA"],
    "vlr_razão": [58449.74],
    "vlr_fiscal": [56560.21]
}

df = pd.DataFrame(data)

# Exibir primeira tabela
st.dataframe(df.style.format({"vlr_razão": "{:,.2f}", "vlr_fiscal": "{:,.2f}"}))

# Texto da diferença
st.markdown(
    "<p style='font-size:15px; font-weight:bold; color:#9B4DCC;'>Diferença de R$ 1.889,53. </p>",
    unsafe_allow_html=True
)

st.markdown("**`Alíquota fiscal: 9,65%. Alíquota razão 7,60%`**")


st.markdown("---")

# Segunda diferença
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade</p>",
    unsafe_allow_html=True
)
st.markdown("""
- No razão contábil, a NF 882191 foi registrada com valor de COFINS de R$ 7.306,79, enquanto na apuração fiscal consta com alíquota zero, sem valor informado.
""")

# Dados detalhados
data2 = {
    "NF_FISCAL": ["882192", "882191"],
    "VLR_RAZÃO": [39394.63, 7306.79],
    "VLR_FISCAL": [39394.64, 0.00]
}

df2 = pd.DataFrame(data2)

# Adicionar coluna de diferença
df2["Dif_COFINS"] = df2["VLR_RAZÃO"] - df2["VLR_FISCAL"]

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''



st.dataframe(
    df2.style.format({"VLR_RAZÃO": "{:,.2f}", "VLR_FISCAL": "{:,.2f}", "Dif_PIS": "{:,.2f}"})
       .applymap(highlight_dif, subset=["Dif_COFINS"])
)

st.markdown("---")


# Nova tabela com resumo PIS/COFINS
data_resumo = {
    "Tributo": ["PIS", "COFINS"],
    "Período": ["09/2025", "09/2025"],
    "Vencimento": ["24/10/2025", "24/10/2025"],
    "Valor Apuração": [19029.95, 89303.88],
    "Valor Pago": [19885.13, 93307.68]
}

df_resumo = pd.DataFrame(data_resumo)

# Adicionar coluna Diferença
df_resumo["Diferença"] = df_resumo["Valor Pago"] - df_resumo["Valor Apuração"]

# Função para destacar diferença positiva
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Título estilizado
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença do Valor pago vs Valor capa apuração</p>",
    unsafe_allow_html=True
)
# Exibir tabela com destaque na coluna Diferença
st.dataframe(
    df_resumo.style.format({
        "Valor Apuração": "{:,.2f}",
        "Valor Pago": "{:,.2f}",
        "Diferença": "{:,.2f}"
    }).applymap(highlight_dif, subset=["Diferença"])
)
st.markdown("<p style='font-size:18px; font-weight:bold; color:#FAFF70;'>O departamento fiscal precisa analisar e corrigir, se necessário.</p>", unsafe_allow_html=True)

#TABELA

# Dados atualizados com VLR_COFINS
data = {
    "NUM_DOCFIS": ["882192"] * 9 + [""],
    "VLR_COFINS": [1071.95, 757.71, 339.76, 169.86, 119.11, 893.29, 56.60, 238.21, 357.32, 4003.80],
    "Base Conferencia (tipo de tributação)": ["Tributado Anteriormente (Monofásico)"] * 9 + [""],
    "VLR_BASE_COFINS": [6504.54, 4597.73, 2061.65, 1030.68, 722.73, 5420.45, 343.47, 1445.45, 2168.18, 24294.88]
}

df = pd.DataFrame(data)

# Exibir título estilizado
st.markdown(
    "<p style='font-size:17px; font-weight:bold; color:#9B4DCC;'>Detalhe diferença:</p>",
    unsafe_allow_html=True
)

# Exibir tabela formatada
st.dataframe(df.style.format({
    "VLR_COFINS": "{:,.2f}",
    "VLR_BASE_PIS": "{:,.2f}"
}))

st.markdown("---")

# uLTIMA
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade</p>",
    unsafe_allow_html=True
)

# Dados detalhados corrigidos
data2 = {
    "NF_FISCAL": ["881880", "881881"],
    "VLR_RAZÃO": [0.00, 49148.10],
    "VLR_FISCAL": [0.00, 49134.54],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA", "STILE COMERCIAL LTDA"]
}

df2 = pd.DataFrame(data2)

# Adicionar coluna de diferença
df2["Dif_COFINS"] = df2["VLR_RAZÃO"] - df2["VLR_FISCAL"]

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Exibir tabela com formatação
st.dataframe(
    df2.style.format({"VLR_RAZÃO": "{:,.2f}", "VLR_FISCAL": "{:,.2f}", "Dif_COFINS": "{:,.2f}"})
       .applymap(highlight_dif, subset=["Dif_COFINS"])
)
