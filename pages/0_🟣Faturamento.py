import streamlit as st

st.set_page_config(
    page_title="FATURAMENTO",
    page_icon="🟣",
)

st.image('teste.svg', width=300)
# Título principal
st.markdown("""
<h2 style="
    color:#9B4DCC;
    font-family:'Montserrat',sans-serif;
    font-weight:700;
    text-align:center;
    border-bottom:2px solid #FFA500;
    padding-bottom:8px;
    margin-bottom:20px;">
Faturamento
</h2>
""", unsafe_allow_html=True)

("""**`Vendas - 4000000`** """)

st.markdown("""

Esta página apresenta as **demonstrações das conciliações entre o Livro Fiscal e o Razão Contábil**
### 📌 Origem dos Dados
- **Fonte Fiscal:** Livro retirado do TaxOne  
- **Fonte Contábil:** Conta 4000000 (Vendas) do razão extraída do SAP  """)

st.markdown("---")

st.markdown("<p style='font-size:25px; font-weight:bold; color:#FFA500;'>🔍 Ocorrência Identificada</p>", unsafe_allow_html=True)


st.markdown("""
- **Nota Fiscal:** `245368-004` – **Filial:** `0005` - **Valor:** `1.790,80`  
  Não localizada nos meses de **agosto** e **setembro**.  
  Situação reportada à área fiscal dia 20/10/2025 (responsável: Thais).

### Observações
As seguintes notas fiscais foram **removidas de agosto** e **incluídas em setembro**:
- `000245490-004`
- `000245493-004`
- `000245496-004`

---

> **Objetivo:** Garantir que os saldos fiscais e contábeis estejam alinhados.
""")




