import streamlit as st
from PIL                  import Image

st.set_page_config(
    page_title="Análise de Sentimentos em Textos: Detecção de Manchetes de Notícias Sarcásticas",
    page_icon="📰",
    layout='wide'
)

st.title("Bem-vindo(a) ao painel do Projeto sobre Detecção de Manchetes de Notícias Sarcásticas ! 🗞️")

image = Image.open('imgs/manchete.jpeg') 
st.sidebar.image(image)

st.markdown(
    """
     #### O que é a Análise de Sentimentos 🔎?

     - A Análise de Sentimentos é uma área bastante relevante nos dias de hoje, principalmente quando se trata de NLP (Natural Language Processing) e Deep Learning. 
     
     - Ela refere-se à aplicação de algoritmos e técnicas computacionais para identificar, extrair e avaliar as emoções, opiniões e atitudes expressas em dados textuais. 
     
     - Essa abordagem é especialmente utilizada em dados provenientes de redes sociais, avaliações de produtos, comentários online e outras fontes de texto, com o objetivo de compreender o sentimento expresso pelos usuários.

     #### Neste projeto, o objetivo é detectar se uma manchete de uma jornal, por exemplo, possui sarcasmo ou não. A partir disso, podemos inferir sobre a confiabilidade daquela notícia e possíveis objetivos por trás daquela manchete.
    """
)