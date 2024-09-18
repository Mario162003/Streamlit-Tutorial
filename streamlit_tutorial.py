import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('Bienvenido al portal predictivo de la empresa AMH')
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')
    
    opcion = st.radio('Seleccione el servicio:', 
                      ('¿Como te encuentras?'), 
                      index=0, 
                      key='option')
    
    if st.button('Empezar!'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == '¿Como te encuentras?':
        switch_page("pred_emociones.py")

if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2