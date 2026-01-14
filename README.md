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

O **Sentinela Industrial** é uma aplicação de **Inteligência Artificial** voltada para a Indústria 4.0, desenhada para prever falhas em maquinário pesado antes que elas ocorram (Manutenção Preditiva).

Utilizando um modelo treinado de **Machine Learning**, o sistema analisa dados brutos de sensores (temperatura, vibração, rotação) e fornece um diagnóstico em tempo real, permitindo que gestores de fábrica evitem paradas não planejadas (Downtime) e otimizem custos operacionais.

### 🎯 Funcionalidades Core
* **🧠 Modelo Preditivo de Alta Precisão:** Utiliza o algoritmo **RandomForestClassifier**, alcançando acurácia superior a **99%** na detecção de padrões de falha.
* **📊 Dashboard em Tempo Real:** Interface construída com **Streamlit**, permitindo input dinâmico de parâmetros operacionais.
* **🚨 Sistema de Alerta Visual:** Classificação binária instantânea:
    * 🟢 **Operação Normal:** Equipamento seguro.
    * 🔴 **ALERTA DE FALHA:** Risco iminente detectado com probabilidade percentual.
* **⚙️ Engenharia de Recursos:** Pipeline robusto com `StandardScaler` para normalização de dados sensoriais.

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
git clone [https://github.com/RomarioDelphin/Sentinela_Industrial.git](https://github.com/RomarioDelphin/Sentinela_Industrial.git)

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
pip install -r requisitos.txt

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
* `scaler_manutencao_preditiva.pkl`: Normalizador de dados (garante a precisão matemática).
* `requisitos.txt`: Lista de bibliotecas necessárias.

---

<div align="center">
<p>Desenvolvido por <strong>Romário Delphin</strong> como parte do portfólio <strong>RAM.IO Holdings</strong>.</p>
</div>
