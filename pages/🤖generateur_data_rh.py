


import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import randint
from datetime import datetime, timedelta

# instantiate a faker object
fake = Faker()

# function to generate a random date within a range
def random_date(start, end):
    return start + timedelta(
        seconds=randint(0, int((end - start).total_seconds())))

# function to generate a single row of data
def generate_row(id):
    dob = random_date(datetime(1955, 1, 1), datetime(2007, 1, 1))
    min_recruitment_date = dob + timedelta(days=16 * 365)  # Minimum recruitment date is 16 years after date of birth
    recruitment_date = random_date(min_recruitment_date, datetime.now())
    leaving_date = random_date(recruitment_date, datetime.now())
    
    service = fake.random_element(elements=("RH", "Ventes", "Marketing", "Informatique", "Finance"))
    
    if service == "RH":
        sub_elements = ('Assistant RH', 'Gestionnaire paie', 'Contrôleur de gestion sociale',
                        'Responsable SIRH', 'Responsable GPEC GEPP')
    elif service == "Ventes":
        sub_elements = ('Animateur SAV', 'Assistant commercial', 'Chargé d’affaires',
                        'Gestionnaire CRM', 'Responsable commercial')
    elif service == "Marketing":
        sub_elements = ('Assistant marketing', 'Category manager', 'Chef de projet marketing',
                        'Responsable marketing', 'Ingénieur packaging')
    elif service == "Informatique":
        sub_elements = ('Administrateur système', 'Administrateur réseaux',
                        'Responsable cybersécurité', 'Webmaster', 'Data engineer')
    elif service == "Finance":
        sub_elements = ('Assistant de gestion', 'Analyste financier', 'Auditeur interne',
                        'Comptable', 'Contrôleur de gestion')
    else:
        sub_elements = ()
    
    diplome = fake.random_element(elements=("BTS", "Licence", "Bachelor", "Master", "Ingenieur"))
    
    if diplome == "BTS":
        min_salary = 23000
        max_salary = 30999
    elif diplome in ["Licence", "Bachelor"]:
        min_salary = 31000
        max_salary = 34999
    elif diplome in ["Master", "Ingenieur"]:
        min_salary = 35000
        max_salary = 65000
    else:
        min_salary = 0
        max_salary = 0
    
    salary = f"{randint(min_salary, max_salary)}€"
    
    return {
        "Matricule": id,
        "Nom": fake.last_name(),
        "Prénom": fake.first_name(),
        "Date de naissance": dob.strftime('%d/%m/%Y'),
        "Lieu de naissance": fake.city(),
        "Genre": fake.random_element(elements=("Male", "Female")),
        "Adresse": fake.address(),
        "Date de recrutement": recruitment_date.strftime('%d/%m/%Y'),
        "Date de fin de contrat": leaving_date.strftime('%d/%m/%Y'),
        "Service": service,
        "Poste occupé": fake.random_element(elements=sub_elements),
        "Diplôme": diplome,
        "Salaire annuel brut": salary
    }



# set the title of the app
st.title("🤖 Générateur de data RH")

st.markdown("")

st.markdown("Chosissez le nombre de salariés à générer à l'aide du curseur ⤵️")

st.markdown("")

# create a slider for the number of rows to generate
num_rows = st.slider("Nombre de salariés", min_value=1, max_value=1000, value=1)

st.markdown("Cliquez sur *Générer* ⤵️")

# create a button to generate the data
if st.button("Générer"):
    # generate the data and convert it to a DataFrame
    data = pd.DataFrame([generate_row(id) for id in range(1, num_rows + 1)])

    # display the first 20 rows of the DataFrame
    st.dataframe(data.head(20))
    
    # create a download link for the data in CSV format
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="data_rh_synthetiques.csv">Télécharger le fichier au format CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

