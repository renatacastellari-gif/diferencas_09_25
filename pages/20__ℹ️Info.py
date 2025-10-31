import streamlit as st

# ====== ESTILO GLOBAL ======
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
    font-family: 'Montserrat', sans-serif;
}
h2 {
    text-align: center;
}
.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
    margin-bottom: 10px;
}
.title {
    color: #9B4DCC;
    font-weight: 800;
    font-size: 28px;
    text-align: center;
    border-bottom: 2px solid #FFA500;
    display: inline-block;
    padding-bottom: 8px;
    margin-bottom: 25px;
    text-shadow: 1px 1px 6px rgba(155, 77, 204, 0.4);
}
.info-box {
    background: linear-gradient(145deg, #111827, #1f2937);
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0px 2px 10px rgba(255,165,0,0.1);
    font-size: 15px;
    line-height: 1.5;
    color: #d1d5db;
}
.path-box {
    background-color: #1f2937;
    border-left: 4px solid #FFA500;
    padding: 10px 15px;
    margin-top: 10px;
    border-radius: 6px;
    font-family: 'Courier New', monospace;
    color: #10B981;
}
.folder {
    font-size: 20px;
    color: #FFD700;
}
</style>
""", unsafe_allow_html=True)

# ====== LOGO CENTRALIZADA ======
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("teste.svg", width=320)

# ====== TÍTULO ======
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
As capas e detalhes completos estão salvos na rede, incluindo meses anteriores.<br>
<span style="color:#FFA500; font-weight:600;">
O objetivo desta página é proporcionar acesso rápido e facilitar a visualização das informações.
</span>
</div>
""", unsafe_allow_html=True)

st.write("") 
st.write("") 
# ====== CAMINHO ======
st.markdown("""
<p class="folder">📁 <b>Caminho para acesso:</b></p>
<div class='path-box'>
Y:\\DEPTO CONTÁBIL\\BR02\\CONCILIAÇÕES\\Conciliações Renata
</div>
""", unsafe_allow_html=True)



