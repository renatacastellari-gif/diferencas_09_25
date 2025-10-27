import streamlit as st
import pandas as pd
import io
from io import BytesIO


# Configuração da página
st.set_page_config(page_title="PIS e COFINS", page_icon="🟣")


# Cabeçalho
st.image('teste.svg', width=300)
st.title('PIS e COFINS')
("""**`Processo de conciliação em andamento`** """)



# Carregar o arquivo Excel
df = pd.read_excel("CODE.xlsx", sheet_name="dif", engine="openpyxl", header=25)
df.dropna(how='all', inplace=True)
df.columns = [str(col).strip() for col in df.columns]

# Filtros na barra lateral
st.sidebar.header("Filtros")
produtos = st.sidebar.multiselect("Produto", options=df["DESCRICAO_COMPL"].dropna().unique())
cfops = st.sidebar.multiselect("CFOP", options=df["COD_CFO"].dropna().unique())
datas = st.sidebar.date_input("Data de Emissão", [])

# Aplicar filtros
filtered_df = df.copy()
if produtos:
    filtered_df = filtered_df[filtered_df["DESCRICAO_COMPL"].isin(produtos)]
if cfops:
    filtered_df = filtered_df[filtered_df["COD_CFO"].isin(cfops)]
if datas:
    filtered_df["DATA_EMISSAO"] = pd.to_datetime(filtered_df["DATA_EMISSAO"], errors='coerce')
    filtered_df = filtered_df[filtered_df["DATA_EMISSAO"].isin(datas)]

# Função para destacar diferenças
def highlight_differences(row):
    styles = []
    if row.get("VLR_ALIQ_ICMS") != row.get("VLR_ICMS -Proprio"):
        styles.append("background-color: #ffcccc")
    else:
        styles.append("")
    if row.get("VLR_ALIQ_PIS") != row.get("VLR_PIS"):
        styles.append("background-color: #ccffcc")
    else:
        styles.append("")
    if row.get("VLR_ALIQ_COFINS") != row.get("VLR_COFINS"):
        styles.append("background-color: #ccccff")
    else:
        styles.append("")
    return styles + [""] * (len(row) - 3)

# Exibir dados
st.title("Análise de Tributação - CODE.xlsx")
st.dataframe(filtered_df.style.apply(highlight_differences, axis=1))

# Exportar dados
st.markdown("### Exportar Dados Filtrados")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", data=csv, file_name="dados_filtrados.csv", mime="text/csv")

excel_buffer = BytesIO()
with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
    filtered_df.to_excel(writer, index=False, sheet_name="Filtrado")
st.download_button("Download Excel", data=excel_buffer.getvalue(), file_name="dados_filtrados.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")









