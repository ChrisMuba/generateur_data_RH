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
def generate_row(id):
    department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    
    return {
        "ID": id,
        "Last Name": fake.last_name(),
        "First Name": fake.first_name(),
        "Gender": fake.random_element(elements=("Male", "Female")),
        "Age": randint(18, 57),
        "Years of Service": randint(1, 10),
        "Annual Salary (€)": randint(23000, 65000),
        "Reason for Leaving": fake.random_element(elements=(
            "Job Dissatisfaction", "Personal Reasons", "Lack of Career Growth",
            "Better Opportunity Elsewhere", "Inadequate Compensation",
            "Work-Life Balance Issues", "Poor Management", "Organizational Change",
            "Retirement", "Resignation")),
        "Promotion": fake.random_element(elements=("Yes", "No")),
        "Training Times": randint(1, 20),
        "Performance Rating": round(uniform(1, 10), 2),
        "Department": department,
        "Job Title": job_title
    }

# Generate fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    st.title("Attrition Data Generator")

    st.markdown("🔄 Analysez les facteurs contribuant à l'attrition et explorez les caractéristiques de ceux qui quittent l'entreprise.")
    
    num_entries = st.number_input("Entrer le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
    
    if st.button("Generate Attrition Data"):
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
