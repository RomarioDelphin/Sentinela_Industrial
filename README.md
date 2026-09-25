<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=SENTINELA%20INDUSTRIAL&fontSize=60&fontAlignY=35&desc=Ind%C3%BAstria%204.0%20|%20Manuten%C3%A7%C3%A3o%20Preditiva%20com%20IA&descAlignY=55&descSize=18&fontColor=ffffff&customColorList=06b6d4,000205&animation=fadeIn" width="100%"/>
</div>

<div align="center">
  <br />
  
  <a href="https://github.com/RomarioDelphin">
    <img src="https://img.shields.io/badge/DEV-ROMARIO%20DELPHIN-000205?style=for-the-badge&logo=github&logoColor=06b6d4&labelColor=000205&color=06b6d4" />
  </a>
  <img src="https://img.shields.io/badge/ML-SCIKIT%20LEARN-000205?style=for-the-badge&logo=scikitlearn&logoColor=F7931E&labelColor=000205&color=F7931E" />
  <img src="https://img.shields.io/badge/APP-STREAMLIT-000205?style=for-the-badge&logo=streamlit&logoColor=FF4B4B&labelColor=000205&color=FF4B4B" />

</div>

<br />

## ⚡ Sobre o Projeto

O **Sentinela Industrial** é uma demonstração em Streamlit de classificação de falhas com dados de sensores. O repositório inclui um conjunto de dados, um modelo serializado e a interface de inferência.

O usuário ajusta temperatura, rotação, torque e desgaste da ferramenta na interface para consultar o modelo. O repositório não documenta instalação em equipamentos reais, coleta contínua de sensores nem redução de paradas ou custos.

### 🎯 Funcionalidades Core
* **🧠 Inferência com modelo serializado:** Classificação e probabilidade exibidas a partir de arquivos `.pkl`. O código de treinamento, a divisão dos dados e o relatório de avaliação não estão neste repositório; a acurácia não pode ser verificada aqui.
* **📊 Dashboard interativo:** Interface construída com **Streamlit**, com ajuste manual de parâmetros operacionais.
* **🚨 Sistema de Alerta Visual:** Classificação binária instantânea:
    * 🟢 **Operação Normal:** Equipamento seguro.
    * 🔴 **ALERTA DE FALHA:** Risco iminente detectado com probabilidade percentual.
* **⚙️ Dados de entrada:** Cinco variáveis de sensores são enviadas ao modelo. Um arquivo de scaler é incluído, mas a aplicação não o carrega separadamente; o pré-processamento deve ser verificado antes de usar o resultado fora desta demonstração.

---

## 🛠️ Stack Tecnológica

O projeto combina Ciência de Dados robusta com uma interface web ágil.

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,sklearn,pandas,vscode&perline=10" />
</div>

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Linguagem** | `Python 3.10+` | Core do processamento de dados. |
| **Modelagem** | `Scikit-learn` | Treinamento do modelo RandomForest e métricas. |
| **Frontend** | `Streamlit` | Interface web interativa para operadores. |
| **Dados** | `Pandas / Joblib` | Manipulação de datasets e persistência do modelo (`.pkl`). |

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar a aplicação de monitoramento em seu ambiente local.

### 📋 Pré-requisitos
* Python 3.10 ou superior.
* Git instalado.

### 1. Instalação e Configuração

```bash
# Clone o repositório
git clone https://github.com/RomarioDelphin/Sentinela_Industrial.git

# Entre na pasta
cd Sentinela_Industrial

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente:
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
# source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

```

### 2. Execução (Dashboard)

Com o ambiente ativo, inicie a interface do Streamlit:

```bash
streamlit run app.py

```

*O navegador abrirá automaticamente exibindo o Painel de Controle do Sentinela.*

---

## 📂 Estrutura de Arquivos

* `app.py`: Código principal da interface e lógica de inferência.
* `modelo_manutencao_preditiva.pkl`: O "cérebro" da IA (modelo treinado).
* `scaler_manutencao_preditiva.pkl`: Arquivo de normalização incluído; não é carregado diretamente pela interface.
* `requirements.txt`: Lista de bibliotecas necessárias.

## Limites da demonstração

O modelo recebe valores inseridos manualmente e foi disponibilizado sem script de treinamento, validação temporal, matriz de confusão ou descrição de uso em ambiente industrial. A saída é uma demonstração técnica e não deve orientar decisões de manutenção sem avaliação independente com dados do equipamento e supervisão técnica.

---

<div align="center">
<p>Desenvolvido por <strong>Romário Delphin</strong> como parte do portfólio <strong>RAM.IO Holdings</strong>.</p>
</div>
