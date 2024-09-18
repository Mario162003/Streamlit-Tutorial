import streamlit as st
from PIL import Image
import numpy as np
#from utils import predict_imagen
from utils import predict_emocion

# Título de la aplicación
st.title('Predicción de los sentimientos')

# Cargar la imagen
uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

# Si se carga una imagen
if uploaded_file is not None:
    # Mostrar la imagen
    st.write('**Vista Previa de la imagen cargada:**')
    image = Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption='Imagen cargada', use_column_width=True)

    # Convertir la imagen a una matriz de valores de píxeles
    image = np.array(image) / 255.0  # Normalizar los valores de píxeles
    
    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('Descubre tus sentimientos'):
        # Predecirla
        pred = predict_emocion(image)

        # Mostrar los resultados de la predicción
        st.success('Éxito al realizar la predicción!')
        st.write('El sentimiento encontrado es:')
        st.write(pred)