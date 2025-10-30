
import streamlit as st
import pandas as pd
import io



# Configuração da página
st.set_page_config(page_title="Resumo PIS COFINS", page_icon="🟣")


# Cabeçalho
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
RESUMO PIS-COFINS
</h2>
""", unsafe_allow_html=True)
("""**`PIS 2300395`** """)
("""**`COFINS 2300394`** """)


st.markdown("---")

st.markdown(
    "<p style='font-size:23px; font-weight:bold; color:#9B4DCC;'> 📝 RESUMO</p>",
    unsafe_allow_html=True
)

# Texto explicativo
st.markdown("""
A base de cálculo utilizada nas notas fiscais — que também é refletida no razão contábil — considera o valor dos produtos somado ao frete, sem dedução do ICMS destacado.
Já na apuração fiscal, aplica-se o abatimento do ICMS, reduzindo a base de cálculo para PIS e COFINS.
""")

st.markdown("---")
st.markdown("<p style='font-size:28px; font-weight:bold; color:#FFA500;'>PIS</p>", unsafe_allow_html=True)

# Seção 1: Comparativo Apuração vs Razão
st.markdown(
    "<p style='font-size:22px; font-weight:bold; color:#9B4DCC;'> ☑️ Comparativo Apuração vs Razão</p>",
    unsafe_allow_html=True
)


dados_comparativo = {
    "Descrição": [
        "Valor PIS com abatimento do ICMS na base de cálculo (Apuração)",
        "(+) ICMS Próprio sobre as vendas (1,65% e 7,60%)",
        "(+) ICMS Próprio vendas Aliquota diferenciada (2,20% e 10,30%) Monofásico",
        "Valor Razão"
    ],
    "Valor (R$)": [57483.84, 6352.23, 23.51, 63859.58]
}

df_comparativo = pd.DataFrame(dados_comparativo)
st.dataframe(df_comparativo.style.format({"Valor (R$)": "{:,.2f}"}))

st.image("Screenshot_4.png", width=1600)


st.markdown("---")
# cofins
st.markdown("<p style='font-size:28px; font-weight:bold; color:#FFA500;'>COFINS</p>", unsafe_allow_html=True)




# Seção 1: Comparativo Apuração vs Razão
st.markdown(
    "<p style='font-size:22px; font-weight:bold; color:#9B4DCC;'> ☑️ Comparativo Apuração vs Razão</p>",
    unsafe_allow_html=True
)


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

st.image("Screenshot_3.png", width=1600)








