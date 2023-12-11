

import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint, uniform

# Instantiate a faker object
fake = Faker()

# Generate a single row of data
def generate_row(job_id):
    
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
    
    num_vacancies = randint(2, 20)
    num_hires = randint(0, num_vacancies)  # Number of Hires should be less than or equal to Number of Vacancies
    
    return {
        "Job_ID": job_id,
        "Department": service,
        "Job Title": fake.random_element(elements=sub_elements),
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

with st.sidebar:
    st.image('gif/Robot_Emoji.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


st.markdown("")

# Run the app
if __name__ == "__main__":
    main()
