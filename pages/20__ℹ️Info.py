import streamlit as st

# Centraliza a imagem
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("teste.svg", width=300)

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
    Informações Adicionais
</h2>
""", unsafe_allow_html=True)

# ====== BOX DE INFORMAÇÃO ======
st.markdown("""
<div class='info-box'>
As capas e detalhes completos estão salvos na rede, incluindo meses anteriores.  
O objetivo desta página é proporcionar acesso rápido e facilitar a visualização das informações.
</div>
""", unsafe_allow_html=True)

# ====== CAMINHO ======
st.markdown("""
<p class="folder">📁 <b>Caminho para acesso:</b></p>
<div class='path-box'>
Y:\\DEPTO CONTÁBIL\\BR02\\CONCILIAÇÕES\\Conciliações Renata
</div>
""", unsafe_allow_html=True)
