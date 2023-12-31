import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint
from datetime import datetime, timedelta
import numpy as np  # Import numpy for random choice

# Instantiate a faker object
fake = Faker()

# Function to generate a random date within a range
def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

# Function to generate a single row of data for a specific year
def generate_row_for_year(id, year, prob_leaving=None):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    recruitment_date = random_date(start_date, end_date)
    leaving_date = None  # Initialize leaving_date as None
    reason_for_departure = None  # Initialize reason_for_departure as None
    # Determine if the employee leaves based on the probability
    if prob_leaving is not None and np.random.rand() < prob_leaving:
        leaving_date = random_date(recruitment_date, end_date)
        #reason_for_departure = fake.random_element(elements=("Mise à pied", "Démission", "Résiliation", "Retraite"))
        reason_weights = [0.44, 0.20, 0.11, 0.02, 0.14, 0.06, 0.03]  # Weights for Dismissal, Resignation, Conventional termination
        reason_for_departure = choices(["Démission", "Fin_Période_Essai", "Rupture_conventionnelle", "Licenciement_économique", "Licenciement", "Retraite", "Autres"], weights=reason_weights, k=1)[0]
    #department = fake.random_element(elements=("RH", "Ventes", "Marketing", "Informatique", "Finance"))
    #job_title = fake.random_element(elements=job_titles[department])
    service_weights = [0.03, 0.05, 0.10, 0.10, 0.15, 0.15, 0.18, 0.24]  # Weights for RH, Ventes, Marketing, etc... 
    service = choices(["Communication", "RH", "Marketing", "Finance", "Informatique", "R&D", "Ventes", "Services_techniques"], weights=service_weights, k=1)[0]

    if service == "Communication":
        sub_elements = ('Chargé de communication', 'Community manager')
        
    elif service == "RH":
        sub_elements = ('Assistant RH', 'Gestionnaire paie', 'Contrôleur de gestion sociale')
        
    elif service == "Marketing":
        sub_elements = ('Assistant marketing', 'Category manager', 'Chef de projet marketing',
                        'Ingénieur packaging')
        
    elif service == "Finance":
        sub_elements = ('Assistant de gestion', 'Analyste financier', 'Comptable', 'Contrôleur de gestion')
        
    elif service == "Informatique":
        sub_elements = ('Administrateur système', 'Administrateur réseaux', 'Administrateur Bases de données',
                        'Responsable cybersécurité', 'Webmaster', 'Data engineer')
        
    elif service == "R&D":
        sub_elements = ('Chef de projet R&D', 'Ingénieur généraliste', 'Ingénieur tests et essais', 
                        'Statisticien', 'Chargé d\'intelligence économique', 'Ingénieur d\'études environnement')
        
    elif service == "Ventes":
        sub_elements = ('Animateur SAV', 'Assistant commercial', 'Chargé d’affaires', 'Animateur des ventes',
                        'Gestionnaire CRM', 'Responsable commercial', 'Business developer', 'Ingénieur avant-vente')
        
    elif service == "Services_techniques":
        sub_elements = ('Acheteur', 'Chargé de la qualité', 'Contrôleur des coûts', 'Gestionnaire Supply Chain', 
                        'Responsable Entrepôt', 'Ingénieur planification', 'Ingénieur amélioration continue', 
                        'Chargé Affaires Réglementaires', 'Responsable matériel', 'Gestionnaire Flux Logistiques')
    else:
        sub_elements = ()
        
    return {
        "Matricule": id,
        "Nom": fake.last_name(),
        "Prénom": fake.first_name(),
        #"Genre": fake.random_element(elements=("Homme", "Femme")),
        "Genre": choices(["Homme", "Femme"], weights=[55, 45], k=1)[0],
        "Date_de_recrutement": recruitment_date.strftime('%d/%m/%Y'),
        "Date_de_départ": leaving_date.strftime('%d/%m/%Y') if leaving_date else "",
        "Raison_du_départ": reason_for_departure if reason_for_departure else "",
        "Service": service,
        "Poste_occupé": fake.random_element(elements=sub_elements)
    }

# Function to generate the fake HR data for a specific year
def generate_hr_data_for_year(num_entries, year):
    prob_leaving = np.random.uniform(0.03, 0.20)
    data = [generate_row_for_year(i, year, prob_leaving) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Function to generate the fake HR data
def generate_hr_data(num_entries):
    prob_leaving = np.random.uniform(0.03, 0.20)
    data = [generate_row_for_year(i, datetime.now().year, prob_leaving) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Generate HR data based on user input
st.title("Turnover Data Generator")
st.markdown("🔄 Générez des données pour comprendre la dynamique du turnover des employés et identifiez les modèles qui pourraient aider à améliorer les stratégies de rétention.")
st.markdown("")

num_entries = st.number_input("Entrer le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
year_selection = st.checkbox("Generer les données pour une année spécifique")

if year_selection:
    selected_year = st.number_input("Enter the year", min_value=1900, max_value=datetime.now().year, value=datetime.now().year, step=1, format="%d")
    if st.button("Generate Turnover Data"):
        df = generate_hr_data_for_year(num_entries, selected_year)
        st.dataframe(df.head(50))
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data_{selected_year}.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
else:
    if st.button("Generer"):
        df = generate_hr_data(num_entries)
        st.dataframe(df.head(50))
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

with st.sidebar:
    st.image('gif/Robot_Emoji.gif')

# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


