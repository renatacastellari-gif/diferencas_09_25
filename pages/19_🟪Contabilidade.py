import streamlit as st
import pandas as pd
from io import BytesIO

st.image('teste.svg', width=200) 
# Título principal

st.markdown("""
<h3 style="
    color:#EEE4EF;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
💻Lançamentos Manuais - Contabilidade
</h3>
""", unsafe_allow_html=True)


st.write("**`Competência: 09/2025`**")
st.write("`ICMS a recolher- 2300391`")
# ------------------- TABELA 1 -------------------
data1 = {
    "COD_ESTAB": ["0016", "0010", "0015", "0009", "0006", "0005", "0002", "0002", "0002"],
    "NF_FISCAL": ["000080030-016", "000114374-010", "000130146-015", "000155770-009", "000203304-002",
                  "000246432-004", "000389456-005", "000389481-005", "000389482-005"],
    "VLR_ICMS": [40.97, 35.55, 27.88, 37.18, 39.43, 65.28, 166.55, 51.77, 78.76],
    "DATA_FISCAL": ["10/09/2025", "12/09/2025", "12/09/2025", "12/09/2025", "12/09/2025",
                    "12/09/2025", "11/09/2025", "12/09/2025", "12/09/2025"],
    "DATA_EMISSAO": ["10/09/2025", "12/09/2025", "12/09/2025", "12/09/2025", "12/09/2025",
                     "12/09/2025", "11/09/2025", "12/09/2025", "12/09/2025"],
    "CFOP_FISCAL": [5949]*9,
    "razao_social_cliente": [
        "OMNILIFE BRASIL COMERCIO DE PRODUCTNUTRICIONAIS LTDA",
        "CEDIS MARABA OMNILIFE BRASIL CPN LTDA",
        "CEDIS CURITIBA OMNILIFE BRASIL CPN LTDA",
        "CEDIS BELO HORIZONTE OMNILIFE BRASIL CPN LTDA",
        "CEDIS SAO LUIS OMNILIFE BRASIL CPN LTDA",
        "CEDIS GOIANIA OMNILIFE BRASIL CPN LTDA",
        "CEDIS TATUAPE OMNILIFE BRASIL CPN LTDA",
        "CEDIS TATUAPE OMNILIFE BRASIL CPN LTDA",
        "CEDIS TATUAPE OMNILIFE BRASIL CPN LTDA"
    ]
}
df1 = pd.DataFrame(data1)

st.markdown("<p style='font-size:14px; font-weight:bold;'> 📌Notas de consumo próprio</p>", unsafe_allow_html=True)
st.dataframe(df1.style.format({"VLR_ICMS": "R$ {:.2f}"}))

# Totalizador tabela 1
total_icms = df1["VLR_ICMS"].sum()
st.markdown(f"<p style='font-size:14px; color:#2E86C1;'>💰 Total ICMS: <b>R$ {total_icms:.2f}</b></p>", unsafe_allow_html=True)

st.write("")
# ------------------- TABELA 2 -------------------
st.write("`ICMS a recuperar - 1280345`")
st.markdown("<h6>📌  Frete </h5>", unsafe_allow_html=True)

data2 = {
    "FILIAL": ["0002", "0004", "0010", "0012", "0019"],
    "VLR_ICMS": [646.42, 2598.20, 3933.92, 7135.98, 2338.83]
}
df2 = pd.DataFrame(data2)

st.dataframe(df2.style.format({"VLR_ICMS": "R$ {:.2f}"}))

# Totalizador tabela 2
total_frete = df2["VLR_ICMS"].sum()



st.markdown(f"<p style='font-size:14px; color:#2E86C1;'>🚚 Total: R$ 16.653,35 ", unsafe_allow_html=True)
# ------------------- EXPORTAR PARA EXCEL -------------------
def to_excel(df1, df2):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df1.to_excel(writer, index=False, sheet_name='Notas Consumo Próprio')
        df2.to_excel(writer, index=False, sheet_name='Frete ICMS a Recuperar')
    return output.getvalue()

excel_file = to_excel(df1, df2)

st.download_button(
    label="📥 Baixar Excel",
    data=excel_file,
    file_name="lancamentos_contabilidade.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

)




