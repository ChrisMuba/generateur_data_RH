


import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
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
    gender_weights = [55, 45] # Weights for Homme, Femme
    gender = choices(["Homme", "Femme"], weights=gender_weights, k=1)[0]
    min_recruitment_date = dob + timedelta(days=16 * 365)  # Minimum recruitment date is 16 years after date of birth
    recruitment_date = random_date(min_recruitment_date, datetime.now())
    leaving_date = random_date(recruitment_date, datetime.now())
    reason_weights = [0.44, 0.20, 0.11, 0.02, 0.14, 0.06, 0.03]  # Weights for Dismissal, Resignation, Conventional termination
    reason_for_departure = choices(["Démission", "Fin_Période_Essai", "Rupture_conventionnelle", "Licenciement_économique", "Licenciement", "Retraite", "Autres"], weights=reason_weights, k=1)[0]

    service_weights = [0.03, 0.05, 0.10, 0.10, 0.15, 0.15, 0.18, 0.24]  # Weights for RH, Ventes, Marketing, etc... 
    #service = fake.random_element(elements=("RH", "Ventes", "Marketing", "Informatique", "Finance"))
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
        "Date_de_naissance": dob.strftime('%d/%m/%Y'),
        "Lieu_de_naissance": fake.city(),
        "Genre": gender,
        "Adresse": fake.address(),
        "Date_de_recrutement": recruitment_date.strftime('%d/%m/%Y'),
        "Date_de_fin_de_contrat": leaving_date.strftime('%d/%m/%Y'),
        "Reason_for_Departure": reason_for_departure,
        "Service": service,
        "Poste_occupé": fake.random_element(elements=sub_elements),
        "Diplôme": diplome,
        "Salaire_annuel_brut": salary
    }



# set the title of the app
st.title("🤖 Générateur de data RH")

st.markdown("")

st.markdown("Chosissez le nombre de salariés à générer à l'aide du :red[curseur] ⤵️")

st.markdown("")

# create a slider for the number of rows to generate
num_rows = st.slider("Nombre de salariés", min_value=1, max_value=1000, value=1)

st.markdown("Cliquez sur **Générer** ⤵️")

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


with st.sidebar:
    st.image('gif/Robot_Emoji.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


st.markdown("")

