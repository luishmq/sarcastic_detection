import numpy as np
import json
import pandas as pd
import re
import string
import pickle
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from PIL                  import Image

# Carregar o modelo treinado e o tokenizer
MODEL_PATH = 'src/model/lstm_model.h5'
TOKENIZER_PATH = 'src/model/tokenizer.pickle'

model = load_model(MODEL_PATH)
with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict_sentiment(text):
    sequence_text = tokenizer.texts_to_sequences([text])

    X_text = pad_sequences(sequence_text, maxlen=512)
    y_pred = model.predict(X_text)

    sentiment = "Sarcástica" if y_pred > 0.5 else "Não Sarcástica"

    return sentiment

# Configuração da página Streamlit

st.set_page_config(layout='wide')
st.title("Detecção de Manchetes de Notícias Sarcásticas 📰")

image = Image.open('imgs/sentiment.jpeg') 
st.sidebar.image(image)

# Interface de entrada do usuário
user_input = st.text_input("Digite a manchete de notícia (em inglês) para a detecção:")

if st.button("Detectar"):
    result = predict_sentiment(user_input)
    st.write(f"Manchete {result}")