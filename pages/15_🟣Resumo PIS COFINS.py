import streamlit as st
import pandas as pd

# Configuração padrão (sem wide global)
st.set_page_config(page_title="Resumo PIS COFINS", page_icon="🟣")

st.title("RESUMO PIS COFINS")

# CSS para simular wide apenas nesta página
st.markdown(
    """
    <style>
    /* Remove limite de largura do container principal */
    .main {
        max-width: 100%;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo
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

# Imagem ocupando largura total
st.image("Screenshot_3.png", use_container_width=True)
