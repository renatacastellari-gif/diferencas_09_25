import streamlit as st
import pandas as pd

# Configuração da página (apenas uma vez e no topo)
st.set_page_config(page_title="Resumo PIS COFINS", page_icon="🟣", layout="wide")

# Cabeçalho
st.image('teste.svg', width=300)
st.title('RESUMO PIS COFINS')
st.markdown("**`PIS 2300395`**")
st.markdown("**`COFINS 2300394`**")

st.markdown("---")

st.markdown("<p style='font-size:28px; font-weight:bold; color:#FFA500;'>COFINS</p>", unsafe_allow_html=True)

# Texto explicativo
st.markdown("""
A base de cálculo utilizada nas notas fiscais — que também é refletida no razão contábil — considera o valor dos produtos somado ao frete, sem dedução do ICMS destacado.
Já na apuração fiscal, aplica-se o abatimento do ICMS, reduzindo a base de cálculo para PIS e COFINS.
""")

# Seção 1: Comparativo Apuração vs Razão
st.markdown("### ✅ Comparativo Apuração vs Razão")

dados_comparativo = {
    "Descrição": [
        "Valor COFINS com abatimento do ICMS na base de cálculo (Apuração)",
        "(+) ICMS Próprio sobre as vendas (1,65% e 7,60%)",
        "(+) ICMS Próprio vendas Aliquota diferenciada (2,20% e 10,30%) Monofásico",
        "Valor Razão"
    ],
    "Valor (R$)": [264792.91, 29258.75, 110.05, 294161.72]
}

df_comparativo = pd.DataFrame(dados_comparativo)
st.dataframe(df_comparativo.style.format({"Valor (R$)": "{:,.2f}"}))

st.markdown("---")

# Imagem wide
st.image("Screenshot_3.png", use_container_width=True)
