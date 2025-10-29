import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="PIS", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
st.title('PIS')
st.markdown("**`PIS a Recuperar - 1280343`**")

st.markdown("""
Esta página apresenta as demonstrações das conciliações do PIS a recuperar.

### 📌 Origem dos Dados
- Fonte Fiscal: Apuração Fiscal
- Fonte Contábil: Conta 1280343 do razão extraída do SAP
""")

st.markdown("---")

# Título estilizado
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade</p>",
    unsafe_allow_html=True
)

# Dados exemplo
data = {
    "Nota_Fiscal": ["000881877"],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA"],
    "vlr_razão": [12716.05],
    "vlr_fiscal": [12308.44]
}

df = pd.DataFrame(data)

# Exibir primeira tabela
st.dataframe(df.style.format({"vlr_razão": "{:,.2f}", "vlr_fiscal": "{:,.2f}"}))

# Texto da diferença
st.markdown(
    "<p style='font-size:15px; font-weight:bold; color:#9B4DCC;'>Diferença de R$ 407,61</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# Segunda diferença
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade</p>",
    unsafe_allow_html=True
)
st.markdown("""
- No razão contábil, a NF 882191 foi registrada com valor de PIS de R$ 1.590,08, enquanto na apuração fiscal consta com alíquota zero, sem valor informado.
""")

# Dados detalhados
data2 = {
    "referencia": ["882192", "882191"],
    "NUM_DOCFIS": ["000129567", "000203701"],
    "VLR_RAZÃO": [8552.00, 1590.08],
    "VLR_FISCAL": [8552.00, 0.00]
}

df2 = pd.DataFrame(data2)

# Adicionar coluna de diferença
df2["Dif_PIS"] = df2["VLR_RAZÃO"] - df2["VLR_FISCAL"]

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''



st.dataframe(
    df2.style.format({"VLR_RAZÃO": "{:,.2f}", "VLR_FISCAL": "{:,.2f}", "Dif_PIS": "{:,.2f}"})
       .applymap(highlight_dif, subset=["Dif_PIS"])
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

# TABELA

# Dados
data = {
    "NUM_DOCFIS": ["882192"] * 9 + [""],
    "VLR_PIS": [228.96, 161.84, 72.57, 36.28, 25.44, 190.80, 12.09, 50.88, 76.32, 855.18],
    "Base Conferencia (tipo de tributação)": ["Tributado Anteriormente (Monofásico)"] * 9 + [""],
    "VLR_BASE_PIS": [6504.54, 4597.73, 2061.65, 1030.68, 722.73, 5420.45, 343.47, 1445.45, 2168.18, 24294.88]
}

df = pd.DataFrame(data)

# Exibir tabela formatada
# Texto da diferença
st.markdown(
    "<p style='font-size:15px; font-weight:bold; color:#9B4DCC;'>Detalhe diferença</p>",
    unsafe_allow_html=True
)

st.dataframe(df.style.format({"VLR_PIS": "{:,.2f}", "VLR_BASE_PIS": "{:,.2f}"}))
