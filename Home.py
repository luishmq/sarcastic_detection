import streamlit as st
from PIL                  import Image

st.set_page_config(
    page_title="Análise de Sentimentos em Textos: Detecção de Frases Sarcásticas",
    page_icon="😏",
    layout='wide'
)

st.title("Bem-vindo(a) ao painel do Projeto sobre Detecção de Frases Sarcásticas em textos! 😏")

image = Image.open('imgs/sentiment.jpeg') 
st.sidebar.image(image)

st.markdown(
    """
     #### O que é a Análise de Sentimentos 🔎?

     - A Análise de Sentimentos é uma área bastante relevante nos dias de hoje, principalmente quando se trata de NLP (Natural Language Processing) e Deep Learning. 
     
     - Ela refere-se à aplicação de algoritmos e técnicas computacionais para identificar, extrair e avaliar as emoções, opiniões e atitudes expressas em dados textuais. 
     
     - Essa abordagem é especialmente utilizada em dados provenientes de redes sociais, avaliações de produtos, comentários online e outras fontes de texto, com o objetivo de compreender o sentimento expresso pelos usuários.

    """
)