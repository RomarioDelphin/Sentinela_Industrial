import streamlit as st
import pandas as pd
import joblib

# --- CONFIGURAÇÃO DA PÁGINA ---
# Este deve ser o PRIMEIRO comando do Streamlit no seu script.
st.set_page_config(page_title="Sentinela Industrial", page_icon="🤖", layout="wide")


# --- Carregamento do Modelo ---
# O @st.cache_resource garante que o modelo seja carregado apenas uma vez.
@st.cache_resource
def load_model():
    """Função para carregar o modelo salvo."""
    try:
        return joblib.load('modelo_manutencao_preditiva.pkl')
    except FileNotFoundError:
        return None

model = load_model()

# --- Interface do Usuário (UI) ---
st.title('🤖 Sentinela Industrial: Manutenção Preditiva com IA')
st.write("""
Esta aplicação utiliza um modelo de Machine Learning para prever a probabilidade de falha de um equipamento industrial com base nos dados de seus sensores. Insira os valores abaixo para obter uma análise em tempo real.
""")

# Verifica se o modelo foi carregado com sucesso
if model is None:
    st.error("Erro: Arquivo do modelo ('modelo_manutencao_preditiva.pkl') não encontrado. Certifique-se de que o modelo foi salvo na mesma pasta que este script.")
else:
    # --- Seção de Input do Usuário ---
    st.sidebar.header('Insira os Dados dos Sensores:')

    def user_input_features():
        """Função para coletar os inputs do usuário na barra lateral."""
        air_temp = st.sidebar.slider('Temperatura do Ar [K]', 295.0, 305.0, 300.1, 0.1)
        process_temp = st.sidebar.slider('Temperatura do Processo [K]', 305.0, 315.0, 310.1, 0.1)
        rotational_speed = st.sidebar.slider('Velocidade Rotacional [rpm]', 1100, 3000, 1538)
        torque = st.sidebar.slider('Torque [Nm]', 3.0, 80.0, 39.5, 0.1)
        tool_wear = st.sidebar.slider('Desgaste da Ferramenta [min]', 0, 260, 107)

        data = {
            'Air temperature [K]': air_temp,
            'Process temperature [K]': process_temp,
            'Rotational speed [rpm]': rotational_speed,
            'Torque [Nm]': torque,
            'Tool wear [min]': tool_wear
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # --- Exibição dos Dados de Entrada e Previsão ---
    st.subheader('Parâmetros Atuais da Máquina:')
    st.write(input_df)

    # Botão para fazer a previsão
    if st.button('Analisar Condição da Máquina'):
        # Fazer a previsão
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)
        
        # Exibir o resultado
        st.subheader('Diagnóstico da IA:')

        if prediction[0] == 1:
            st.error('ALERTA: Falha iminente detectada!', icon="🚨")
            st.write(f"O modelo indica uma alta probabilidade de falha. Ações de manutenção são recomendadas.")
        else:
            st.success('Status: Operação Normal', icon="✅")
            st.write(f"O modelo indica que a máquina está operando em condições normais.")
        
        # Exibindo a probabilidade
        probabilidade_falha = prediction_proba[0][1] * 100
        # Usando st.progress para uma barra visual
        st.progress(int(probabilidade_falha))
        st.write(f"**Probabilidade de Falha: {probabilidade_falha:.2f}%**")