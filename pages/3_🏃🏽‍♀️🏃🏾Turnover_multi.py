

import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint
from datetime import datetime, timedelta

# Instantiate a faker object
fake = Faker()

# Define the job titles for each department
job_titles = {
    "RH": ('Assistant RH', 'Gestionnaire paie', 'Contrôleur de gestion sociale',
           'Responsable SIRH', 'Responsable GPEC GEPP'),
    "Ventes": ('Animateur SAV', 'Assistant commercial', 'Chargé d’affaires',
              'Gestionnaire CRM', 'Responsable commercial'),
    "Marketing": ('Assistant marketing', 'Category manager', 'Chef de projet marketing',
                  'Responsable marketing', 'Ingénieur packaging'),
    "Informatique": ('Administrateur système', 'Administrateur réseaux',
           'Responsable sécurité informatique', 'Webmaster', 'Data engineer'),
    "Finance": ('Assistant de gestion', 'Analyste financier', 'Auditeur interne',
                'Comptable', 'Contrôleur de gestion')
}

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
    
    department = fake.random_element(elements=("RH", "Ventes", "Marketing", "Informatique", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    
    return {
        "Matricule": id,
        "Nom": fake.last_name(),
        "Prénom": fake.first_name(),
        "Genre": fake.random_element(elements=("Male", "Female")),
        "Date de recrutement": recruitment_date.strftime('%d/%m/%Y'),
        "Date de départ": leaving_date.strftime('%d/%m/%Y'),
        "Raison du départ": reason_for_departure,
        "Service": department,
        "Poste occupé": job_title
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
