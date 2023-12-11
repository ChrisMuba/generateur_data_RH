

import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint
from datetime import datetime, timedelta

# Instantiate a faker object
fake = Faker()

# Function to generate a random date within a range
def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

# Function to generate a single row of data
def generate_row(id):
    recruitment_date = random_date(datetime(2013, 1, 1), datetime.now())
    leaving_date = random_date(recruitment_date, datetime.now())
    
    #reason_for_departure = fake.random_element(elements=("Mise à pied", "Démission", "Résiliation", "Retraite"))
    reason_weights = [0.44, 0.20, 0.11, 0.02, 0.14, 0.06, 0.03]  # Weights for Dismissal, Resignation, Conventional termination
    reason_for_departure = choices(["Démission", "Fin_Période_Essai", "Rupture_conventionnelle", "Licenciement_économique", "Licenciement", "Retraite", "Autres"], weights=reason_weights, k=1)[0]
    
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
        #"Genre": fake.random_element(elements=("Male", "Female")),
        "Genre": choices(["Homme", "Femme"], weights=[55, 45], k=1)[0],
        "Date_de_recrutement": recruitment_date.strftime('%d/%m/%Y'),
        "Date_de_départ": leaving_date.strftime('%d/%m/%Y'),
        "Raison_du_départ": reason_for_departure,
        "Service": service,
        "Poste_occupé": fake.random_element(elements=sub_elements)
    }

# Function to generate the fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Generate HR data based on user input
st.title("Turnover Data Generator")

st.markdown("Données générées sur plusieurs années aléatoires")

num_entries = st.number_input("Entrer le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")

if st.button("Generate HR Data"):
    df = generate_hr_data(num_entries)
    st.dataframe(df.head(50))

    # Export data as CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)


with st.sidebar:
    st.image('gif/Robot_Emoji.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


st.markdown("")
