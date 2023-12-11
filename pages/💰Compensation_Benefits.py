import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint, choice

# Initialize Faker
fake = Faker()

# Define benefits package values
benefits_values = {
    1: 500,
    2: 1000,
    3: 1500
}

# Function to generate a single row of fake data
def generate_fake_data(id):
    #department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
    #job_title = fake.random_element(elements=job_titles[department])
    #gender = fake.random_element(elements=("Male", "Female"))
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

    gender_weights = [55, 45] # Weights for Homme, Femme
    gender = choices(["Homme", "Femme"], weights=gender_weights, k=1)[0]
    age = randint(28, 52)
    years_at_company = randint(1, 12)
    education_level = fake.random_element(elements=("BTS", "Licence", "Bachelor", "Master", "Ingenieur"))
    salary_ranges = {
        "BTS": (23000, 30999),
        "Licence": (31000, 34999),
        "Bachelor": (31000, 34999),
        "Master": (35000, 65000),
        "Ingenieur": (35000, 65000)
    }
    min_salary, max_salary = salary_ranges.get(education_level, (0, 0))
    salary = f"{randint(min_salary, max_salary)}€"
    bonus_percent = choice([0, 5, 10, 15, 20])
    bonus_value = f"{int(salary[:-1]) * bonus_percent / 100}€"
    benefits_package = '/'.join(fake.random_elements(elements=("Health", "Dental", "Vision"), unique=True, length=randint(1, 3)))
    benefits_package_value = f"{benefits_values[len(benefits_package.split('/'))]}€"

    return {
        "ID": id,
        "Department": service,
        "Job Title": fake.random_element(elements=sub_elements),
        "Gender": gender,
        "Age": age,
        "Years at Company": years_at_company,
        "Education Level": education_level,
        "Salary": salary,
        "Bonus %": f"{bonus_percent}%",
        "Bonus Value": bonus_value,
        "Benefits Package": benefits_package,
        "Benefits Package Value": benefits_package_value
    }

# Streamlit app
st.title('Comp & Ben Data Generator')

st.markdown("💰 Produisez des données sur les salaires, les primes, les coûts des avantages sociaux. Pratiquez la modélisation et la prévision de la rémunération.")

# User input for the number of data entries
num_entries = st.number_input('Entrer le nombre de données à générer (max 1000)', min_value=1, max_value=1000, value=50)

# Generate data button
if st.button('Generate Comp & Ben Data'):
    data = [generate_fake_data(i+1) for i in range(num_entries)]
    df = pd.DataFrame(data)

    # Show the first 50 rows in the app
    st.write(df.head(50))

    # Export to CSV button
    if st.button('Export to CSV'):
        df.to_csv('fake_hr_data.csv', index=False)
        st.success('Data exported successfully!')
        
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

