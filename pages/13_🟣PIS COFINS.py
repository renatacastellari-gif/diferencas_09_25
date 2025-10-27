import streamlit as st
import pandas as pd
import io



# Configuração da página
st.set_page_config(page_title="PIS e COFINS", page_icon="🟣")


# Cabeçalho
st.image('teste.svg', width=300)
st.title('PIS e COFINS')
("""**`Processo de conciliação em andamento`** """)





# Carregar dados do Excel
df = pd.read_excel("CODE.xlsx", sheet_name="dif", engine="openpyxl", header=25)
df.dropna(how='all', inplace=True)

# Verificar diferenças de ICMS
dif_icms = df[df["VLR_ALIQ_ICMS"] != df["VLR_ICMS -Proprio"]]

# Exibir mensagem formatada
if not dif_icms.empty:
    produto = dif_icms.iloc[0]["DESCRICAO_COMPL"]
    aliquota_nf = dif_icms.iloc[0]["VLR_ALIQ_ICMS"]
    aliquota_apuracao = dif_icms.iloc[0]["VLR_ICMS -Proprio"]
    st.markdown(f"""
    **`Diferença de ICMS identificada no produto: {produto}`**  
    **`Alíquota na nota fiscal: {aliquota_nf}%`**  
    **`Alíquota na apuração: {aliquota_apuracao}%`**  
    **`Esta conta está sendo conciliada pela colaboradora Gabriela.`**
    """)
else:
    st.markdown("**`Nenhuma diferença de ICMS identificada.`**")
