import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint, uniform

# Instantiate a faker object
fake = Faker()

# Department job titles

# Generate a single row of data
def generate_row(id):
    genre_weights = [55, 45] # Weights for Homme, Femme
    genre = choices(["Homme", "Femme"], weights=genre_weights, k=1)[0],
    
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
        "ID": id,
        "Last_Name": fake.last_name(),
        "First_Name": fake.first_name(),
        "Gender": genre,
        "Age": randint(18, 57),
        "Years_of_Service": randint(1, 10),
        "Annual_Salary_€": randint(23000, 65000),
        "Reason_for_Leaving": reason_for_departure,
        "Promotion": fake.random_element(elements=("Yes", "No")),
        "Training_Times": randint(1, 20),
        "Performance_Rating": round(uniform(1, 10), 2),
        "Department": service,
        "Job_Title": fake.random_element(elements=sub_elements)
    }

# Generate fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    st.title("Attrition Data Generator")

    st.markdown("🚪🚶Analysez les facteurs contribuant à l'attrition et explorez les caractéristiques de ceux qui quittent l'entreprise.")
    
    num_entries = st.number_input("Entrer le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
    
    if st.button("Generate Attrition Data"):
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
