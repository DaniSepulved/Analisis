import streamlit as st
import pandas as pd

st.title("Vista previa de datos CSV")

archivos = {
    "Profesores": "profesores.csv",
    "Cuestionarios": "cuestionarios.csv",
    "Preguntas": "preguntas.csv",
    "Estudiantes": "estudiantes.csv",
    "Respuestas": "respuestas.csv"
}

seleccion = st.selectbox("Selecciona un archivo para ver los datos", list(archivos.keys()))

df = pd.read_csv(archivos[seleccion])
st.dataframe(df.head(10))
