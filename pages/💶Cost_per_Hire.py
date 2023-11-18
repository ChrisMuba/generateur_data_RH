

import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import randint, uniform

# Instantiate a faker object
fake = Faker()

# Department job titles
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

# Generate a single row of data
def generate_row(job_id):
    department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    num_vacancies = randint(2, 20)
    num_hires = randint(0, num_vacancies)  # Number of Hires should be less than or equal to Number of Vacancies
    
    return {
        "Job_ID": job_id,
        "Department": department,
        "Job Title": job_title,
        "Number of Vacancies": num_vacancies,
        "Location": fake.city(),
        "Number of Applicants": randint(75, 300),
        "Number of Interviews": randint(5, 60),
        "Number of Hires": num_hires,
        "Cost Type": fake.random_element(elements=("Job Posting", "Agency Fee", "Interview Travel", "Onboarding")),
        "Cost Amount (€)": randint(100, 750)
    }

# Generate fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    st.title("Cost per hire Data Generator")

    st.markdown("💵 calculez l'investissement nécessaire pour attirer et intégrer de nouveaux talents, vous aidant ainsi à optimiser les processus de recrutement.")
    
    num_entries = st.number_input("Enter the number of data entries to generate (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
    
    if st.button("Generate Cost per hire Data"):
        df = generate_hr_data(num_entries)
        st.dataframe(df.head(50))
        
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
