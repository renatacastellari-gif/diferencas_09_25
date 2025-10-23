import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="CONCILIAÇÕES",
    page_icon="🟪",
)

# Título e introdução
st.title("📌 Dúvidas")
st.markdown("""
Nem todas as notas fiscais são consideradas no mesmo mês pelo fiscal.  
Veja os exemplos abaixo:
""")

# Exibição das notas com destaque
st.markdown("""
### 🔍 Exemplos:
- **000247864-004** → Considerada no mês **09/2025**  
- **000247860-004** → Considerada no mês **10/2025**  
*(Emissão e autorização ocorreram no mês 10/2025)*
""")

# Observação
st.info("Por que algumas notas são consideradas no mês subsequente e outras não?")

