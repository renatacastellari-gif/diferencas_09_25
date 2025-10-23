import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="IPI", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
st.title('IPI')
st.markdown("**`IPI a RECOLHER - 2300390`**")

st.markdown("""
Esta página apresenta as **demonstrações das conciliações entre o IPI e o Razão Contábil.**

### 📌 Origem dos Dados
- **Fonte Fiscal:** Livro retirado do TaxOne
- **Fonte Contábil:** Conta 2300390 (IPI a recolher) do razão extraída do SAP
""")

# Espaço
st.write("")
st.markdown("<h4>🔍 Diferença Identificada: Pagamento</h4>", unsafe_allow_html=True)
st.markdown("**`Competência: 08/2025`**")
st.markdown("**`Pagamento: 09/2025`**")

# ✅ NOVA SEÇÃO
st.markdown("<h6>Diferença no valor pago versus a apuração fiscal e livro fiscal</h6>", unsafe_allow_html=True)

# CSS geral para tabelas
custom_css = """
<style>
.styled-table {
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
}
.styled-table th {
    background-color: #6A0DAD;
    color: white;
    font-weight: bold;
    text-align: center;
    padding: 6px;
}
.styled-table td {
    padding: 6px;
    text-align: center;
    font-size: 13px;
}
</style>
"""

# ✅ Tabela resumo por filial
dados_filial = {
    "FILIAL": ["0006", "0010"],
    "Valor Apuração": ["22.157,62", "19.583,13"],
    "Valor guia do ECAC": ["20.807,55", "20.739,16"]
}
df_filial = pd.DataFrame(dados_filial)
html_filial = df_filial.to_html(index=False, classes='styled-table')
st.markdown(custom_css + html_filial, unsafe_allow_html=True)

# ✅ Tabela detalhada com cores na coluna DIFERENÇA
dados_detalhe = {
    "FILIAL": ["0002","0004","0005","0006","0009","0010","0015","0016","0018","0019","Total Geral"],
    "Livro Saídas": ["39.682,68","11.570,39","67.764,57","22.388,31","20.830,39","19.597,43","32.367,99","18.943,53","22.051,92","19.596,69","274.793,90"],
    "Livro Entradas": ["443,00","199,54","683,85","230,69","-","14,30","513,05","263,61","611,69","175,03","3.134,76"],
    "Livro Fiscal": ["39.239,68","11.370,85","67.080,72","22.157,62","20.830,39","19.583,13","31.854,94","18.679,92","21.440,23","19.421,66","271.659,14"],
    "Apuração Fiscal": ["39.239,68","11.370,85","67.457,00","22.157,62","20.830,39","19.583,13","31.854,94","18.679,92","21.440,23","19.421,66","271.659,14"],
    "GUIA NO ECAC": ["39.239,68","11.370,85","67.457,00","20.807,55","20.830,39","20.739,16","31.854,94","18.679,92","21.440,23","19.421,66","271.841,38"],
    "DIFERENÇA": ["-","-","376,28  (Livro vs Apuração)","-1.350,07","0,00","1.156,03","-","0,00","-0,00","0,00","182,24"]
}
df_detalhe = pd.DataFrame(dados_detalhe)

# Função para aplicar cor condicional
def color_diff(val):
    try:
        val_float = float(val.replace('.', '').replace(',', '.'))
        if val_float > 0:
            return f'<span style="color:green;">{val}</span>'
        elif val_float < 0:
            return f'<span style="color:red;">{val}</span>'
        else:
            return val
    except:
        return val

df_detalhe["DIFERENÇA"] = df_detalhe["DIFERENÇA"].apply(color_diff)
html_detalhe = df_detalhe.to_html(escape=False, index=False, classes='styled-table')
st.markdown(html_detalhe, unsafe_allow_html=True)

# ✅ Lançamento contábil
st.markdown("<h6>Lançamento pela Contabilidade</h6>", unsafe_allow_html=True)
dados_razao = {
    "RAZÃO": ["MIT DCTF WEB REF 08/2025 (PIS/COFINS/IPI FIL 2 A 19)"],
    "VLR": ["271.841,38"]
}
df_razao = pd.DataFrame(dados_razao)
html_razao = df_razao.to_html(index=False, classes='styled-table')
st.markdown(html_razao, unsafe_allow_html=True)

# Texto original
st.write("")
st.markdown("<h4>🔍 Diferença Identificada: Pagamento</h4>", unsafe_allow_html=True)
st.markdown("""
Houve três notas fiscais que foram retificadas pelo setor fiscal.  
Essas notas foram retiradas do mês **08** e adicionadas ao mês **09**, filial 0005 resultando em um pagamento a maior no valor de `R$ 376,28`, que ficou como **saldo credor**.  
**Resolução fiscal.**
""")

# ✅ Tabela IPI detalhada
data = {
    "NUM_DOCFIS": [245490]*8 + [245493]*4 + [245496]*3,
    "SERIE_DOCFIS": ["004"]*15,
    "VLR_IPI": [9.85, 12.07, 25.59, None, None, 78.84, 66.07, 23.44,
                23.00, 13.18, 22.68, 21.24, 42.77, 19.51, 18.04]
}
df = pd.DataFrame(data)
df.reset_index(drop=True, inplace=True)

html_table = df.to_html(index=False, classes='styled-table')
st.markdown("<h6>Detalhamento das Notas Fiscais (IPI)</h6>", unsafe_allow_html=True)
st.markdown(custom_css + html_table, unsafe_allow_html=True)

# Totalizador
total_ipi = df["VLR_IPI"].sum(skipna=True)

st.markdown(f"<p style='font-size:13px;'>💰 Valor total IPI: <b>R$ {total_ipi:.2f}</b></p>", unsafe_allow_html=True)


