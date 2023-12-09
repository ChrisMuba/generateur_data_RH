import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from datetime import datetime, timedelta
import numpy as np

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
    return start + timedelta(seconds=np.random.randint(0, int((end - start).total_seconds())))

# Function to generate a single row of data
def generate_row(id):
    gender = choices(["Homme", "Femme"], weights=[55, 45], k=1)[0]
    start_date = datetime(2013, 1, 1)
    end_date = datetime(2013, 12, 31)
    recruitment_date = random_date(start_date, end_date)
    leaving_date = random_date(recruitment_date, recruitment_date + timedelta(days=365 * 2))  # Assuming a max of 2 years after recruitment
    reason_weights = [0.44, 0.20, 0.11, 0.02, 0.14, 0.06, 0.03]  # Weights for Dismissal, Resignation, Conventional termination
    reason_for_departure = choices(["Démission", "Fin_Période_Essai", "Rupture_conventionnelle", "Licenciement_économique", "Licenciement", "Retraite", "Autres"], weights=reason_weights, k=1)[0]
    department = fake.random_element(elements=("RH", "Ventes", "Marketing", "Informatique", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    return {
        "ID": id,
        "Last Name": fake.last_name(),
        "First Name": fake.first_name(),
        "Gender": gender,
        "Recruitment Date": recruitment_date.strftime('%d/%m/%Y'),
        "Date of Leaving": leaving_date.strftime('%d/%m/%Y'),
        "Reason for Departure": reason_for_departure,
        "Department": department,
        "Job Title": job_title
    }

# Function to generate the fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
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


