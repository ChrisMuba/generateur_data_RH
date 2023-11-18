


import streamlit as st
import pandas as pd
import base64
from faker import Faker
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

# Function to generate a single row of data for a specific year
def generate_row_for_year(id, year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    recruitment_date = random_date(start_date, end_date)
    leaving_date = random_date(recruitment_date, end_date)
    
    reason_for_departure = fake.random_element(elements=("Mise à pied", "Démission", "Résiliation", "Retraite"))
    
    department = fake.random_element(elements=("RH", "Ventes", "Marketing", "Informatique", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    
    return {
        "Matricule": id,
        "Nom": fake.last_name(),
        "Prénom": fake.first_name(),
        "Genre": fake.random_element(elements=("Homme", "Femme")),
        "Date de recrutement": recruitment_date.strftime('%d/%m/%Y'),
        "Date de départ": leaving_date.strftime('%d/%m/%Y'),
        "Raison du départ": reason_for_departure,
        "Service": department,
        "Poste occupé": job_title
    }

# Function to generate the fake HR data for a specific year
def generate_hr_data_for_year(num_entries, year):
    data = [generate_row_for_year(i, year) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Function to generate the fake HR data
def generate_hr_data(num_entries):
    data = [generate_row_for_year(i, datetime.now().year) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Generate HR data based on user input
st.title("Turnover Data Generator")

st.markdown("🔄 Générez des données pour comprendre la vitesse à laquelle les employés quittent l'entreprise et identifier les causes et solutions potentielles.")

num_entries = st.number_input("Entrer le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
year_selection = st.checkbox("Generer les données pour une année spécifique")

if year_selection:
    selected_year = st.number_input("Enter the year", min_value=1900, max_value=datetime.now().year, value=datetime.now().year, step=1, format="%d")
    
    if st.button("Generate HR Data"):
        df = generate_hr_data_for_year(num_entries, selected_year)
        st.dataframe(df.head(50))
        
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
else:
    if st.button("Generate HR Data"):
        df = generate_hr_data(num_entries)
        st.dataframe(df.head(50))
        
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
