import streamlit as st
import pandas as pd
from io import BytesIO

# Configuração da página
st.set_page_config(page_title="IPI a Recuperar", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
st.title('IPI a Recuperar')
("""**`IPI a Recuperar - 1280345`** """)

st.markdown("""
Esta página apresenta as demonstrações das conciliações entre o ICMS e o Razão Contábil.

### 📌 Origem dos Dados
- Fonte Fiscal: Livro retirado do TaxOne
- Fonte Contábil: Conta 1280342 (IPI a recuperar) do razão extraída do SAP
""")

# Diferença
diferenca = 2033.84
st.markdown("<p style='font-size:25px; font-weight:bold; color:#FFA500;'>🔎 Diferença entre Fiscal e Contabilidade</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:14px; color:#C0392B;'>⚠ Diferença: <b>R$ {diferenca:,.2f}</b></p>", unsafe_allow_html=True)

("""**`Filial 12, não há saldo devedor`** """)

# ------------------- TABELA RAZÃO -------------------
data_razao = {
    "conta": ["1280342"],
    "documento": ["5100003926"],
    "tipo_documento": ["RE"],
    "data_documento": ["29/08/2025"],
    "data_lancamento": ["04/09/2025"],
    "doc_compensacao": [""],
    "chave_lancamento": [40],
    "codigo_imposto": ["I9"],
    "nome": ["Omnilife Manufactura SA DE CV"],
    "texto": ["Saldo a favor Stile OML 01825 nf 881877 - 1/881876"],
    "referencia": ["881877 - 1"],
    "montante_moeda_interna": [59224.57]
}
df_razao = pd.DataFrame(data_razao)

st.markdown("<p style='font-size:14px; font-weight:bold;'>📒 Razão</p>", unsafe_allow_html=True)
st.dataframe(df_razao.style.format({"montante_moeda_interna": "R$ {:.2f}"}))

# ------------------- TABELA FISCAL -------------------
data_fiscal = {
    "NUM_DOCFIS": ["000881876", "000881877"],
    "SERIE_DOCFIS": [1, 1],
    "VLR_IPI_FISCAL": ['0.00', '57.190,73'],
    "DATA_FISCAL": ["30/09/2025", "30/09/2025"],
    "DSC_CFO": ["COMPRAS PARA COMERCIALIZACAO", "COMPRAS PARA COMERCIALIZACAO"],
    "CFOP": [1102, 1102],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA", "STILE COMERCIAL LTDA"],
    "NF_FISCAL_S": ["000881876-1", "000881877-1"]
}
df_fiscal = pd.DataFrame(data_fiscal)

st.markdown("<p style='font-size:14px; font-weight:bold;'>📑 Fiscal</p>", unsafe_allow_html=True)
st.dataframe(df_fiscal.style.format({"VLR_ICMS_FISCAL": "R$ {:.2f}"}))

