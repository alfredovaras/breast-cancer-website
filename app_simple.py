import streamlit as st
import pandas as pd
import requests


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(uploaded_file.name)
    response = requests.get('http://127.0.0.1:8000/')
    st.write('API status:')
    st.write(response.json())

    files = {'file': (uploaded_file.name, uploaded_file.getvalue(),'multipart/form-data')}
    response = requests.post('http://127.0.0.1:8000/predict', files = files )
    st.write('API cancer prediction value:')
    st.write(response.json())
