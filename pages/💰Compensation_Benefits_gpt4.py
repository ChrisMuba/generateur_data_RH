import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import randint, choice

# Initialize Faker
fake = Faker()

# Define job titles for each department
job_titles = {
    "HR": ('Assistant RH', 'Gestionnaire paie', 'Contrôleur de gestion sociale', 'Responsable SIRH', 'Responsable GPEC GEPP'),
    "Sales": ('Animateur SAV', 'Assistant commercial', 'Chargé d’affaires', 'Gestionnaire CRM', 'Responsable commercial'),
    "Marketing": ('Assistant marketing', 'Category manager', 'Chef de projet marketing', 'Responsable marketing', 'Ingénieur packaging'),
    "IT": ('Administrateur système', 'Administrateur réseaux', 'Responsable sécurité informatique', 'Webmaster', 'Data engineer'),
    "Finance": ('Assistant de gestion', 'Analyste financier', 'Auditeur interne', 'Comptable', 'Contrôleur de gestion')
}

# Define benefits package values
benefits_values = {
    1: 500,
    2: 1000,
    3: 1500
}

# Function to generate a single row of fake data
def generate_fake_data(id):
    department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
    job_title = fake.random_element(elements=job_titles[department])
    gender = fake.random_element(elements=("Male", "Female"))
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
        "Department": department,
        "Job Title": job_title,
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

# Initialize an empty DataFrame
df = pd.DataFrame()

# Generate data button
if st.button('Generate Comp & Ben Data'):
    data = [generate_fake_data(i+1) for i in range(num_entries)]
    df = pd.DataFrame(data)

    # Show the first 50 rows in the app
    st.write(df.head(50))

# Check if DataFrame is not empty, then show 'Export to CSV' button
if not df.empty:
    if st.button('Export to CSV'):
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success('Data exported successfully!')

with st.sidebar:
    st.image('gif/Robot_Emoji.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


st.markdown("")

