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

st.markdown(""")

st.markdown(""" Nas operações de venda com CFOP 6.403, o ICMS-ST é recolhido antecipadamente. 
No entanto, quando há devolução dessas mercadorias por meio do CFOP 2.411, e a empresa — como é o caso da Omnifile — não possui inscrição 
estadual no estado remetente, ela não pode se creditar do ICMS-ST destacado na nota original.""")


st.info("Diante disso, poderia nos confirmar se há intenção de solicitar a restituição desses valores de ICMS-ST junto ao estado de origem ou se
devemos considerar esses valores como perda definitiva para fins de contabilização?")

