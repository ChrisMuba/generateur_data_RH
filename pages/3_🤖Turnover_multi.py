

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
    "HR": ('Assistant RH', 'Gestionnaire paie', 'Contrôleur de gestion sociale',
           'Responsable SIRH', 'Responsable GPEC GEPP'),
    "Sales": ('Animateur SAV', 'Assistant commercial', 'Chargé d’affaires',
              'Gestionnaire CRM', 'Responsable commercial'),
    "Marketing": ('Assistant marketing', 'Category manager', 'Chef de projet marketing',
                  'Responsable marketing', 'Ingénieur packaging'),
    "IT": ('Administrateur système', 'Administrateur réseaux',
           'Responsable sécurité informatique', 'Webmaster', 'Data engineer'),
    "Finance": ('Assistant de gestion', 'Analyste financier', 'Auditeur interne',
                'Comptable', 'Contrôleur de gestion')
}

# Function to generate a random date within a range
def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

# Function to generate a single row of data
def generate_row(id):
    recruitment_date = random_date(datetime(2000, 1, 1), datetime.now())
    leaving_date = random_date(recruitment_date, datetime.now())
    
    reason_for_departure = fake.random_element(elements=("Layoff", "Resignation", "Termination", "Retirement"))
    
    department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    
    return {
        "ID": id,
        "Last Name": fake.last_name(),
        "First Name": fake.first_name(),
        "Gender": fake.random_element(elements=("Male", "Female")),
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
st.title("Fake HR Data Generator")

num_entries = st.number_input("Enter the number of data entries to generate (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")

if st.button("Generate HR Data"):
    df = generate_hr_data(num_entries)
    st.dataframe(df.head(50))

    # Export data as CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
