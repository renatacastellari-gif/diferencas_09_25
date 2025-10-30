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
            st.rerun()
        else:
            st.error("Senha incorreta.")
else:
    # 🔒 Conteúdo protegido
    st.image('teste.svg', width=400) 
    st.title('Conciliações dos Impostos')
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
Conciliações dos Impostos
</h2>
""", unsafe_allow_html=True)
    
 




    # Competência em verde
    st.markdown("""**`Competência: 09/2025`**""")

    # Dados como strings (códigos de contas), alinhados
    dados = [
        ("IPI a Recolher", "2300390"),
        ("ICMS a Recolher", "2300391"),
        ("COFINS a Recolher", "2300394"),
        ("PIS a Recolher", "2300395"),
        ("IPI a Recuperar", "1280342"),
        ("PIS a Recuperar", "1280343"),
        ("COFINS a Recuperar", "1280344"),
        ("ICMS a Recuperar", "1280345"),
        ("VENDAS", "4000000"),
    ]

    linhas_formatadas = [f"{nome:<25} {codigo:>10}" for nome, codigo in dados]
    st.code("\n".join(linhas_formatadas))

    st.markdown("<p style='font-size:28px; font-weight:bold; color:#FFA500;'>Seja bem vindo(a)!</p>", unsafe_allow_html=True)
    # Texto explicativo
    st.markdown("""
   

    Esta aplicação apresenta as **demonstrações das conciliações entre os saldos fiscais e contábeis (Razão)**, destacando as **diferenças identificadas** e seus respectivos detalhes.

    O objetivo é oferecer uma visão clara e organizada para apoiar os departamentos fiscal e contábil. 
    - **Conciliação dos impostos** 
    - **Validação dos lançamentos contábeis**
    - **Identificação de ajustes necessários**

   


    ✅ Navegue pelas abas para consultar as diferenças do mês.

    ---

    > **Objetivo:** Garantir o alinhamento entre os saldos fiscais e contábeis, prevenindo divergências nos registros.
   O objetivo do desenvolvimento dessa página é proporcionar acesso rápido e facilitar a visualização das informações.

    """)
































