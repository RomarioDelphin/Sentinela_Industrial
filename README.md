# README

🤖 Sentinela Industrial: Manutenção Preditiva com IA
Este projeto é uma aplicação web completa que utiliza um modelo de Machine Learning para prever falhas em equipamentos industriais em tempo real, com base em dados de sensores. A solução transforma dados brutos em um diagnóstico acionável, permitindo uma manutenção mais inteligente e proativa.

# Execução
![Image](https://github.com/user-attachments/assets/915774f6-c907-4439-ac6a-4c830d728693)


# Funcionalidades Principais ✨

Modelo Preditivo de Alta Performance: Utiliza um modelo RandomForestClassifier treinado para identificar padrões que antecedem falhas, alcançando uma acurácia superior a 99% no dataset de teste.
Análise em Tempo Real: Uma interface interativa construída com Streamlit permite que o usuário insira os dados dos sensores e receba um diagnóstico instantâneo sobre a condição da máquina.
Diagnóstico Claro: A aplicação fornece um status visual e claro (Operação Normal ou ALERTA: Falha iminente detectada!) e a probabilidade percentual de falha.
Engenharia de Features: O projeto inclui um pipeline de pré-processamento robusto que normaliza os dados de entrada (StandardScaler) para garantir a máxima performance do modelo.
🛠️ Tecnologias e Bibliotecas Utilizadas
Linguagem: Python 3
Análise e Modelagem: Pandas, Scikit-learn
Aplicação Web: Streamlit
Manipulação de Arquivos: Joblib
Visualização de Dados: Matplotlib, Seaborn
Ambiente: Jupyter Notebook (para exploração e treinamento)
🚀 Como Rodar o Projeto Localmente
Siga os passos abaixo para executar a aplicação no seu ambiente.

Pré-requisitos
Python 3.10 ou superior
Git
Instalação
Clone este repositório:

Bash

git clone https://github.com/SEU-USUARIO/Sentinela_Industrial.git
Navegue até a pasta do projeto:

Bash

cd Sentinela_Industrial
Crie e ative um ambiente virtual:

Bash

# Criar
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate
Instale as dependências necessárias:

Bash

pip install -r requirements.txt
Execução
Com o ambiente virtual ativo, inicie a aplicação Streamlit:

Bash

streamlit run app.py
A aplicação abrirá automaticamente no seu navegador padrão.

Este projeto é uma demonstração prática de como a Inteligência Artificial pode ser aplicada para resolver desafios reais na indústria, otimizando processos e prevenindo perdas.
