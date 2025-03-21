import streamlit as st
import requests

st.title("Project 3 - Orchestrator (Minimal)")

st.write("Ce projet appelle l'API de Project 1 et Project 2.")

if st.button("Appeler Project 1"):
    try:
        # Si vous utilisez Docker Compose, vous pouvez pointer vers "project1:8000"
        # En local hors compose, utilisez "http://localhost:8001" par exemple
        response = requests.get("http://project1:8000/")
        st.write(response.json())
    except Exception as e:
        st.error(f"Erreur : {e}")

if st.button("Appeler Project 2 (predict)"):
    try:
        # Idem, ajustez l'URL selon votre mapping de ports
        response = requests.get("http://project2:8000/predict")
        st.write(response.json())
    except Exception as e:
        st.error(f"Erreur : {e}")