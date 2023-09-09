import streamlit as st
import requests
import random
import time
from PIL import Image

# FIX ME: use environmental variables
#URL_DA_API_DO_MODELO = 'http://127.0.0.1:8000/predict'

#URL_DA_API_DO_MODELO ='https://breast-cancer-image-baseline-test-jgvharqxta-uc.a.run.app/predict'

# modelo inicial
# URL_DA_API_DO_MODELO = 'https://breast-cancer-image-baseline-app-state-http-jgvharqxta-uc.a.run.app/predict'

URL_DA_API_DO_MODELO = 'https://breast-cancer-image-lewagon-model-jgvharqxta-uc.a.run.app/predict'


model_api_url = URL_DA_API_DO_MODELO
query_api_url = URL_DA_API_DO_MODELO
#result = None


# Lógica de chamada à API do modelo
def call_api(api_url):
    files = {'file': (uploaded_image.name, uploaded_image.getvalue(),'multipart/form-data')}
    response = requests.post(api_url, files = files )
    prediction = None

    if response.status_code == 200: #response_status_code==200:
        prediction = response.json()
        cancer_probability = prediction["Cancer probability"]

        if cancer_probability > 0.70:
            st.error("Resultado da análise: Alta probabilidade de ter câncer")
        elif cancer_probability > 0.40:
            st.warning("Resultado da análise: Média probabilidade de ter câncer")
        else:
            st.success("Resultado da análise: Baixa probabilidade de ter câncer")

        st.warning(f"A probabilidade de câncer detectado é: {cancer_probability:.0%}")
    else:
        st.error("Ocorreu um erro ao processar a imagem.")

    # FIX ME: read with pydicom if dcm
    # If dicom, process
    # st.image(uploaded_image, caption='Imagem de Mamografia', use_column_width=True)

    return prediction

image = Image.open("dataset-cover.png")


def sending_image():
    with st.spinner('Aguarde por favor ...'):
        time.sleep(3)
        st.success("Imagem enviada",  icon="✅")


def process_form():
    patient_data = f"Paciente de {age} anos de idade, "
    patient_data += f"com {motherhood_status} filho(s), {weight} kg, " if motherhood_status else f"sem filhos, {weight} kg, "
    patient_data += "ingere álcool, " if alcohol_consumption else "não ingere álcool, "
    patient_data += "fumante, " if smoker else  "não fumante, "
    patient_data += "possui implante e " if implant else "não possui implante e "
    patient_data += "com histórico familiar com câncer." if history else "sem histórico familiar com câncer."
    print(patient_data)

# Configuração de cores e estilo do front-end
st.set_page_config(page_title="Detecção de Câncer de Mama", page_icon="🎗️")
# st.markdown(
#     """
#     <style>
#     .stAlert {
#         padding: 10px;
#         background-color: #f8d7da;
#         color: #721c24;
#         border: 1px solid #f5c6cb;
#         border-radius: 4px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# Título e cabeçalho
st.title("Detecção de Câncer de Mama em Mamografias")
st.write("Bem-vinda à nossa plataforma de detecção de câncer de mama em mamografias.")

# Disclaimer
st.warning("Este é um exemplo simplificado e não substitui a avaliação médica profissional. "
           "Os resultados são gerados apenas para fins de demonstração.")

# Formulário de Dados
st.subheader("Dados da Paciente")

with st.form("my_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        #age = st.number_input("Idade", min_value=15, value=30)
        age = st.slider("Idade", min_value=10, max_value=100, value=35)
        weight = st.number_input("Peso (kg)", min_value=20, max_value=180, value=60)
        smoker = st.checkbox("É fumante?")
        alcohol_consumption = st.checkbox("Ingere álcool?")

    with col2:
        #motherhood_status = st.selectbox("Estado de Maternidade", ["Tem filhos", "Não tem filhos"])
        motherhood_status = st.slider("Número de filhos", min_value=0, max_value=10, value=0)
        ethnicity = st.selectbox("Auto-Identificação Étnica", ["Caucasiano", "Afrodescendente", "Asiático", "Outro"])
        implant = st.checkbox("Tem implante?")
        history = st.checkbox("Tem histórico familiar com câncer de mama?")

    # Área de Upload
    uploaded_image = st.file_uploader("Faça o upload da sua imagem de mamografia (jpg, png, dicom)", type=["jpg", "png","dcm"])
    st.markdown("---")

    submitted = st.form_submit_button("Enviar imagem")

    if submitted:
        if uploaded_image is None:
            st.error("Falta escolher uma imagem", icon="❌")
        else:
            sending_image()
            process_form()
            call_api(query_api_url)

# Contribuição para Pesquisa
st.subheader("Contribuição para Pesquisa")
st.write("Os dados fornecidos serão usados de forma anônima para melhorar nosso modelo.")
st.markdown("---")

# Suporte ao Usuário
st.subheader("Contato e Suporte")
st.write("Para qualquer dúvida ou assistência, entre em contato conosco em contato@exemplo.com")

st.image(image, caption="LeWagon")


# Exibição de Resultados
# if (uploaded_image is not None) & (result is not None):
#     st.subheader("Resultado da Avaliação")
#     if result:
#         # 1: cancer detected
#         st.warning("Resultado da análise: Alta probabilidade de ter câncer")
#     else:
#         # 0: cancer not detected
#         st.warning("Resultado da análise: Baixa probabilidade de ter câncer")
#     result = None

# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
# for percent_complete in range(100):
#     time.sleep(0.025)
#     my_bar.progress(percent_complete + 1, text=progress_text)


# Lógica de chamada à API do modelo - BACKUP

# def call_api(api_url):
#     files = {'file': (uploaded_image.name, uploaded_image.getvalue(),'multipart/form-data')}
#     response = requests.post(api_url, files = files )
#     prediction = None

#     if response.status_code == 200: #response_status_code==200:
#         prediction = response.json()
#         cancer_probability = prediction["Cancer probability"]
#         if cancer_probability > 0.65:
#             st.warning("Resultado da análise: Alta probabilidade de ter câncer")
#         else:
#             st.success("Resultado da análise: Baixa probabilidade de ter câncer")
#         st.warning(f"A probabilidade de câncer detectado é: {cancer_probability:.2%}")
#     else:
#         st.error("Ocorreu um erro ao processar a imagem.")

#     # FIX ME: read with pydicom if dcm
#     # If dicom, process
#     # st.image(uploaded_image, caption='Imagem de Mamografia', use_column_width=True)

#     return prediction
