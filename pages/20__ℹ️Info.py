import streamlit as st

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
</h2> """)



# Segunda info
st.info("""
As capas e detalhes completos estão salvos na rede, incluindo meses anteriores.  
  O objetivo do desenvolvimento dessa página é proporcionar acesso rápido e facilitar a visualização das informações.""")

("""
 

📂 Caminho para acesso:  

`Y:\DEPTO CONTÁBIL\BR02\CONCILIAÇÕES\Conciliações Renata`

""")









