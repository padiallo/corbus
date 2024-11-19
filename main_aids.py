import streamlit as st
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Use an environment variable or pass the API key directly
OPENAI_API_KEY = "sk-proj-XLrwmj4aDP6yO2w1BfJCT3BlbkFJvEDHUsMJvOFfQOpKqCck"

llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY)
tools = [PythonREPLTool()]
prefix = """En tant qu'expert en science des données avec une expertise approfondie dans la manipulation de données complexes via des fichiers CSV et l'utilisation de la bibliothèque pandas pour l'analyse de données, vous possédez les compétences requises pour mener des analyses détaillées et élaborer des visualisations percutantes sur le traitement antirétroviral du VIH. Voici les directives spécifiques à suivre pour vos visualisations :

1. **Qualité Professionnelle des Graphiques** : Chaque graphique doit présenter un design soigné et utiliser une palette de couleurs engageante et appropriée pour une interprétation facile et une présentation visuelle attrayante.

2. **Affichage des Valeurs** : Pour une transparence totale et une compréhension immédiate, chaque élément visuel, comme les barres dans un diagramme en barres, doit clairement indiquer les valeurs numériques correspondantes au sommet de chaque barre.

3. **Enregistrement des Fichiers** : Tous les graphiques créés doivent être sauvegardés au format .png dans le répertoire spécifié : "/Users/roni/Documents/GitHub/LLMtutorial/tutorial55/". Cette instruction est à respecter rigoureusement.

Les colonnes du jeu de données à votre disposition, à exploiter judicieusement pour vos analyses, sont les suivantes :

- **patient_id** : Identifiant unique du patient.
- **treatment_id** : Identifiant spécifique du traitement.
- **treatment_date** : Date du traitement, formatée en mm-jj-aaaa (ex. : 01-01-2015).
- **treatment_time** : Heure précise du traitement, formatée en hh:mm (ex. : 20:02:57).
- **dosage** : Quantité de médicament prescrit lors du traitement.
- **total_cost** : Coût total du traitement pour un patient donné.

Utilisez ces informations pour construire des requêtes perspicaces, mener des analyses approfondies et élaborer des rapports clairs qui démontrent l'efficacité et les coûts associés aux traitements antirétroviraux. En cas de données insuffisantes pour répondre à une question spécifique, votre réponse doit être "I don't know". Cette approche garantira la précision et la pertinence de vos analyses, renforçant ainsi votre réputation d'analyste rigoureux et compétent.

"""

theme = "traitement vih"

st.title("THREE NINE FIVES")
st.write("Upload one dataset csv format")
file = st.file_uploader("Selectionnez votre fichier", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write(df)

    user_input = st.text_area(f"Posez une question relative à {theme}")
    if user_input:
        agent = create_pandas_dataframe_agent(
            llm, df, verbose=True, prefix=prefix, agent_type=AgentType.OPENAI_FUNCTIONS, extra_tools=tools
        )
        response = agent.invoke(user_input)
        st.write(response["output"])


        #c'est ici que je me suis arrêté ce matin 
