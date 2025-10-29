import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="PIS", page_icon="🟣")

# Cabeçalho
st.image('teste.svg', width=300)
st.title('PIS')
st.markdown("**`PIS a Recuperar - 1280343`**")

st.markdown("""
Esta página apresenta as demonstrações das conciliações do PIS a recuperar.

### 📌 Origem dos Dados
- Fonte Fiscal: Apuração Fiscal
- Fonte Contábil: Conta 1280343 do razão extraída do SAP
""")





st.markdown("---")




st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade </p>", unsafe_allow_html=True)


# Dados
data = {
    "Nota_Fiscal": ["000881877"],
    "RAZAO_SOCIAL": ["STILE COMERCIAL LTDA"],
    "vlr_razão": [12716.05],
    "vlr_fiscal": [12308.44]
}

# Converter para DataFrame
df = pd.DataFrame(data)

# Exibir no Streamlit
st.dataframe(df.style.format({"vlr_razão": "{:,.2f}", "vlr_fiscal": "{:,.2f}"}))



st.markdown(
    "<p style='font-size:15px; font-weight:bold; color:#9B4DCC;'> Diferença de R$ 407,61</p>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença de Valor entre fiscal e contabilidade </p>", unsafe_allow_html=True)
st.markdown("""
- No razão contábil, a NF 882191 foi registrada com valor de PIS de R$ 1.590,08, enquanto na apuração fiscal consta com alíquota zero, sem valor informado.
""")

# Dados detalhados
data = {
    "referencia": [
        "882192","882191"
    ],
    "NUM_DOCFIS": [
        "000129567","000203701","000203468","000212587",
        "000245624","000246830","000389017","000389299","000390046"
    ],
    "VLR_RAZÃO": [8552.00,1590.08],
    "VLR_FISCAL": [
        "8552.00","0.00"
    ]
}

import streamlit as st
import pandas as pd

# Dados
data = {
    "referencia": ["882192", "882191"],
    "NUM_DOCFIS": [
        "000129567","000203701","000203468","000212587",
        "000245624","000246830","000389017","000389299","000390046"
    ],
    "VLR_RAZÃO": [8552.00, 1590.08],
    "VLR_FISCAL": [8552.00, 0.00]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Adicionar coluna de diferença
df["Dif_PIS"] = df["VLR_RAZÃO"] - df["VLR_FISCAL"]

# Função para destacar diferença
def highlight_dif(val):
    return 'background-color: #9b59b6; color: white;' if val > 0 else ''

# Título estilizado
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#9B4DCC;'>📊 Diferenças PIS</p>",
    unsafe_allow_html=True
)

# Exibir tabela com destaque
st.dataframe(
    df.style.format({"VLR_RAZÃO": "{:,.2f}", "VLR_FISCAL": "{:,.2f}", "Dif_PIS": "{:,.2f}"})
      .applymap(highlight_dif, subset=["Dif_PIS"])
)




st.write("")
st.write("")

st.markdown("---")
st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ 77 Notas com valor fiscal sem razão</p>", unsafe_allow_html=True)
# Texto explicativo em Markdown
st.markdown("""


- **Razão (Nota Fiscal):** Sem tributação
- **Apuração:** Tributado 
""")


# TESTETE

import streamlit as st
import pandas as pd

# Dados completos
data_pis = {
    "VLR_PIS": [
        9.50,10.38,6.54,2.58,1.24,3.82,10.64,0.20,17.31,4.52,17.89,3.36,3.73,23.39,24.79,1.00,2.35,24.77,
        47.80,20.64,9.75,5.78,6.05,3.38,15.09,14.63,8.99,8.92,2.00,1.81,11.00,15.83,27.80,16.50,16.83,33.33,
        6.06,23.93,0.72,6.61,3.97,7.48,4.34,3.52,9.79,39.22,2.99,29.30,2.92,5.02,4.35,6.29,5.32,0.27,
        7.21,0.59,18.50,2.92,2.92,12.78,1.64,2.87,2.78,0.67,13.72,16.02,3.99,22.85,2.72,31.00,37.22,5.74,
        17.46,13.04,3.41,5.80
    ],
    "NF_FISCAL": [
        "000114153-010","000114352-010","000129577-015","000130035-015","000130038-015","000130311-015","000156124-009","000203081-002",
        "000388867-005","000388906-005","000388927-005","000389013-005","000389084-005","000389088-005","000389093-005","000389187-005",
        "000389199-005","000389202-005","000389280-005","000389282-005","000389284-005","000389287-005","000389288-005","000389291-005",
        "000389335-005","000389339-005","000389352-005","000389369-005","000389370-005","000389424-005","000389436-005","000389452-005",
        "000389484-005","000389491-005","000389493-005","000389514-005","000389530-005","000389534-005","000389537-005","000389585-005",
        "000389591-005","000389602-005","000389607-005","000389638-005","000389764-005","000389766-005","000389789-005","000389802-005",
        "000389809-005","000389835-005","000389839-005","000389868-005","000389891-005","000389899-005","000389932-005","000389933-005",
        "000389969-005","000389971-005","000389972-005","000389982-005","000389984-005","000389992-005","000390033-005","000390034-005",
        "000390051-005","000390053-005","000390092-005","000390104-005","000390110-005","000390125-005","000390136-005","000390170-005",
        "000390212-005","000390234-005","000390263-005","000390306-005"
    ],
    "COD_ESTAB": ["0010","0010","0015","0015","0015","0015","0009","0002"] + ["0002"]*68,
    "DATA_EMISSAO": [
        "02/09/2025","11/09/2025","01/09/2025","10/09/2025","10/09/2025","17/09/2025","26/09/2025","04/09/2025",
        "01/09/2025","01/09/2025","01/09/2025","02/09/2025","04/09/2025","04/09/2025","04/09/2025","06/09/2025",
        "06/09/2025","06/09/2025","08/09/2025","08/09/2025","08/09/2025","08/09/2025","08/09/2025","08/09/2025",
        "09/09/2025","09/09/2025","10/09/2025","10/09/2025","10/09/2025","11/09/2025","11/09/2025","11/09/2025",
        "12/09/2025","12/09/2025","12/09/2025","12/09/2025","13/09/2025","13/09/2025","13/09/2025","15/09/2025",
        "15/09/2025","15/09/2025","15/09/2025","16/09/2025","18/09/2025","18/09/2025","19/09/2025","19/09/2025",
        "19/09/2025","20/09/2025","20/09/2025","22/09/2025","22/09/2025","22/09/2025","23/09/2025","23/09/2025",
        "24/09/2025","24/09/2025","24/09/2025","24/09/2025","24/09/2025","24/09/2025","25/09/2025","25/09/2025",
        "25/09/2025","25/09/2025","26/09/2025","26/09/2025","26/09/2025","27/09/2025","27/09/2025","29/09/2025",
        "29/09/2025","30/09/2025","30/09/2025","30/09/2025"
    ],
    "CFOP": ["5102","5102","5102","5102","5102","5102","5102","5403"] + ["5102"]*68
}

# Garantir que todas as listas tenham mesmo tamanho
min_len = min(len(v) for v in data_pis.values())
for key in data_pis:
    data_pis[key] = data_pis[key][:min_len]

# Criar DataFrame
df_pis = pd.DataFrame(data_pis)

# Exibir no Streamlit
st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#9B4DCC;'> 📊</p>",
    unsafe_allow_html=True
)
st.dataframe(df_pis.style.format({"VLR_PIS": "{:,.2f}"}))

# TESTE


st.markdown("---")
st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Diferença NF de serviço NF 000022686-002</p>", unsafe_allow_html=True)
st.markdown("""
 
- **Razão:** Valor: **0,38**
- **Prefeitura:** Não localizado
""")

st.write("")

st.markdown("---")

st.markdown(
    "<p style='font-size:23px; font-weight:bold; color:#9B4DCC;'> ↩️ DEVOLUÇÕES</p>",
    unsafe_allow_html=True
)
# Texto explicativo em Markdown
st.markdown("<p style='font-size:18px; font-weight:bold; color:#FFA500;'>⚠️ Tem valor fiscal sem razão</p>", unsafe_allow_html=True)
st.markdown("""


 
- **Descrição CFOP: Devolução de venda de mercadoria adquirida ou recebida de terceiros**

""")

# Dados fornecidos
data = {
    "NF_FISCAL": [
        "000388905-005",
        "000389364-005",
        "000389464-005",
        "000389600-005"
    ],
    "VLR_PIS": [4.52, 5.78, 15.09, 16.50],
    "DATA_FISCAL": [
        "01/09/2025",
        "10/09/2025",
        "11/09/2025",
        "15/09/2025"
    ],
    "CFOP": ["1202"]*4
}

# Criar DataFrame
df = pd.DataFrame(data)

# Exibir tabela formatada (sem roxo)



st.markdown(
    "<p style='font-size:18px; font-weight:bold; color:#9B4DCC;'> 📊</p>",
    unsafe_allow_html=True
)
st.dataframe(df.style.format(precision=2))

# ADD

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

st.markdown("---")

st.image("Screenshot_4.png", width=1600)
