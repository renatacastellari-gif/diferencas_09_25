import streamlit as st

# Configuração da página
st.set_page_config(page_title="Conciliações dos Impostos", page_icon="🟪")

# Senha fixa
PASSWORD = "minhasenha123"

# Inicializa estado de login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 🔒 Esconde a barra lateral com CSS se não estiver logado
if not st.session_state.logged_in:
    hide_sidebar = """
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# Se não estiver logado, pede senha
if not st.session_state.logged_in:
    st.title("Acesso Restrito")
    senha = st.text_input("Digite a senha:", type="password")
    if st.button("Entrar"):
        if senha == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso liberado! Agora você pode navegar pelas páginas.")
            st.rerun() # Recarrega a página para mostrar o menu
        else:
            st.error("Senha incorreta.")
else:
    # 🔒 Conteúdo protegido
    st.image('teste.svg', width=400) 
    st.title('Conciliações dos Impostos')
    ("""**`Competência: 09/2025`** """)

    
st.success("**`FATURAMENTO - 4000000`**")
st.success("**`ICMS a RECOLHER - 2300391`**")
st.success("**`IPI a RECOLHER - 2300390`**")
st.success("**`ICMS a Recuperar - 1280345`**")
st.success("**`IPI a Recuperar - 1280345`**")
st.success("**`COFINS a Recolher - 2300394`**")
st.success("**`PIS a Recolher - 2300395`**")
st.success("**`PIS a Recuperar - 1280343`**")
st.success("**`COFINS a Recuperar - 12803434`**")






    st.markdown("""
    ## Seja bem vindo(a)
    
Esta aplicação apresenta as **demonstrações das conciliações entre os saldos fiscais e contábeis (Razão)**, destacando as **diferenças identificadas** e seus respectivos detalhes.

O objetivo é oferecer uma visão clara e organizada para apoiar:
- **Apuração dos impostos** (ICMS, IPI, PIS, COFINS)
- **Validação dos lançamentos contábeis**
- **Identificação de ajustes necessários**


                

✅ Navegue pelas abas para consultar as diferenças do mês.






                

---

> **Objetivo:** Garantir o alinhamento entre os saldos fiscais e contábeis, prevenindo divergências nos registros.              
 
""")







