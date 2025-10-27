import streamlit as st
import pandas as pd
import io



import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="ICMS DOOTAX", page_icon="🟣")

# Título e descrição
st.title('ICMS DOOTAX')
st.markdown("**`ICMS a RECOLHER - 2300391`**")

st.markdown("""
Esta página apresenta as **demonstrações das conciliações entre o ICMS Difal (Dootax) e o Razão Contábil.**

### 📌 Origem dos Dados
- **Fonte Fiscal:** Planilha DOOTAX retirada do site Dootax (Filtro: Tipo de Tributo: ICMS)
- **Fonte Contábil:** Conta 2300391 (ICMS a recolher) do razão extraída do SAP  

### 🔍 Ocorrência Identificada
Valores lançados no razão com multa, **necessário reclassificar**.

---
""")

# Carregar os dados
df = pd.read_excel("CODE.xlsx", sheet_name="dif", engine="openpyxl", skiprows=6)

# Selecionar e renomear colunas
df = df[["DESCRICAO_COMPL", "montante_moeda_interna", "VLR_COFINS", "VLR_FRETE_ITEM", "NUM_DOCFIS"]].copy()
df.columns = ["Produto", "Valor Total", "Valor ICMS", "Valor Multa", "Nº Documento"]

# Calcular diferença
df["Diferença"] = df["Valor ICMS"] - df["Valor Total"]

# Função para destacar valores de multa positivos
def highlight_multa(val):
    return 'background-color: #9b59b6; color: white;' if pd.notnull(val) and val > 0 else ''

# Exibir tabela
st.subheader("📊 Diferenças DOOTAX vs RAZÃO")
st.dataframe(df.style.format(precision=2).applymap(highlight_multa, subset=['Valor Multa']))

# Objetivo final
st.markdown("""
---
> **Objetivo:** Garantir que os saldos fiscais e contábeis estejam alinhados.
""")
