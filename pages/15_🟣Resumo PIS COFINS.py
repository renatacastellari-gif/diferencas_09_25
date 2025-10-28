import streamlit as st
import pandas as pd

# NÃO usar layout="wide" aqui, para não afetar tudo
st.set_page_config(page_title="Resumo PIS COFINS", page_icon="🟣")

st.title("RESUMO PIS COFINS")

# CSS para imagem ocupar largura total da tela
st.markdown(
    """
    <style>
    .wide-img img {
        width: 100vw; /* largura total da viewport */
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir imagem wide
st.markdown('<div class="wide-img">Screenshot_3.png</div>', unsafe_allow_html=True)
