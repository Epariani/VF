import streamlit as st
import pandas as pd

df = pd.read_csv("./sito_vf/domande.csv")

st.title("Padre Nostro VERO - FALSO")
st.write("ISTRUZIONI: ad ogni domanda sostituite VERO o FALSO con la risposta giusta scritta tutta in MAIUSCOLO, poi cliccate su correggi")
risposta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
for i in range(13):
    st.write(i + 1)
    st.write(df.loc[i][0])
    risposta[i] = st.text_input("RISPOSTA " + str(i + 1), "VERO o FALSO")
    if st.button("CORREGGI " + str(i + 1)):
        if risposta[i] == df.loc[i][1]:
            st.write("Esatto")
        else:
            st.write("Sbagliato")
