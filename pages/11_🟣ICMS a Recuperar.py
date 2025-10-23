import streamlit as st
import pandas as pd
import io


# Configuração da página
st.set_page_config(page_title="ICMS recuperar", page_icon="🟣")


# Cabeçalho
st.image('teste.svg', width=300)
st.title('ICMS a Recuperar')
("""**`ICMS a Recuperar - 1280345`** """)

st.markdown("""
Esta página apresenta as **demonstrações das conciliações entre o ICMS e o Razão Contábil.**

### 📌 Origem dos Dados
- **Fonte Fiscal:** Livro retirado do TaxOne
- **Fonte Contábil:** Conta 1280345 (ICMS a recuperar) do razão extraída do SAP  """)

# Texto explicativo
st.write("")  # Adiciona uma linha em branco
st.write("")  # Adiciona uma linha em branco


st.markdown("<h5>📌 Diferença de valor entre fiscal e contabilidade no crédito da STILE</h4>", unsafe_allow_html=True)

# Valor da diferença
diferenca = 1016.92
st.markdown(f"<p style='font-size:14px; color:#C0392B;'>⚠ Diferença: <b>R$ {diferenca:,.2f}</b></p>", unsafe_allow_html=True)

# ------------------- TABELA RAZÃO -------------------
data_razao = {
    "conta": ["1280345"],
    "documento": ["5100003926"],
    "data_documento": ["29/08/2025"],
    "data_lancamento": ["04/09/2025"],
    "chave_lancamento": [40],
    "montante_moeda_interna": [36103.27],
    "referencia": ["881877 - 1"],
    "texto": ["Saldo a favor Stile OML 01825 nf 881877 - 1/881876"]
}
df_razao = pd.DataFrame(data_razao)

st.markdown("<p style='font-size:14px; font-weight:bold;'>📒 Razão</p>", unsafe_allow_html=True)
st.dataframe(df_razao.style.format({"montante_moeda_interna": "R$ {:.2f}"}))

# ------------------- TABELA FISCAL -------------------
data_fiscal = {
    "NUM_DOCFIS": ["000881876", "000881877"],
    "SERIE_DOCFIS": [1, 1],
    "VLR_ICMS_FISCAL": [5221.20, 29865.15],
    "DATA_FISCAL": ["30/09/2025", "30/09/2025"],
    "DSC_CFO": ["COMPRAS PARA COMERCIALIZACAO", "COMPRAS PARA COMERCIALIZACAO"],
    "CFOP": [1102, 1102],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA", "STILE COMERCIAL LTDA"],
    "NF_FISCAL_S": ["000881876-1", "000881877-1"]
}
df_fiscal = pd.DataFrame(data_fiscal)

st.markdown("<p style='font-size:14px; font-weight:bold;'>📑 Fiscal</p>", unsafe_allow_html=True)
st.dataframe(df_fiscal.style.format({"VLR_ICMS_FISCAL": "R$ {:.2f}"}))

# ------------------- EXPORTAR PARA EXCEL -------------------
def to_excel(df1, df2, df_razao, df_fiscal):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df1.to_excel(writer, index=False, sheet_name='Notas Consumo Próprio')
        df2.to_excel(writer, index=False, sheet_name='Frete ICMS a Recuperar')
        df_razao.to_excel(writer, index=False, sheet_name='Razão')
        df_fiscal.to_excel(writer, index=False, sheet_name='Fiscal')
    return output.getvalue()






