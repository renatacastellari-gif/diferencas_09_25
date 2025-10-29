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




st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade </p>", unsafe_allow_html=True)


# Dados
data = {
    "Nota_Fiscal": ["000881877"],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA"],
    "vlr_razão": [12716.05],
    "vlr_fiscal": [12308.44]
}

# Converter para DataFrame
df = pd.DataFrame(data)

# Exibir no Streamlit
st.dataframe(df.style.format({"vlr_razão": "{:,.2f}", "vlr_fiscal": "{:,.2f}"}))



st.markdown(
    "<p style='font-size:15px; font-weight:bold; color:#9B4DCC;'> Diferença de R$ 407,61</p>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade </p>", unsafe_allow_html=True)
st.markdown("""
- No razão contábil, a NF 882191 foi registrada com valor de PIS de R$ 1.590,08, enquanto na apuração fiscal consta com alíquota zero, sem valor informado.
""")

# Dados detalhados
data = {
    "referencia": [
        "882192","882191"
    ],
    "NUM_DOCFIS": [
        "000129567","000203701","000203468","000212587",
        "000245624","000246830","000389017","000389299","000390046"
    ],
    "VLR_RAZÃO": [8552.00,1590.08],
    "VLR_FISCAL": [
        "8552.00","0.00"
    ]
}

import streamlit as st
import pandas as pd

# Dados
data = {
    "referencia": ["882192", "882191"],
    "NUM_DOCFIS": [
        "000129567","000203701","000203468","000212587",
        "000245624","000246830","000389017","000389299","000390046"
    ],
    "VLR_RAZÃO": [8552.00, 1590.08],
    "VLR_FISCAL": [8552.00, 0.00]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Adicionar coluna de diferença
df["Dif_PIS"] = df["VLR_RAZÃO"] - df["VLR_FISCAL"]

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Título estilizado
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#9B4DCC;'>📊 Diferenças PIS</p>",
    unsafe_allow_html=True
)

# Exibir tabela com destaque
st.dataframe(
    df.style.format({"VLR_RAZÃO": "{:,.2f}", "VLR_FISCAL": "{:,.2f}", "Dif_PIS": "{:,.2f}"})
      .applymap(highlight_dif, subset=["Dif_PIS"])
)




