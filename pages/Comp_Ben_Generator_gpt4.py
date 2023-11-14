import streamlit as st
import pandas as pd
import random
from faker import Faker
from random import randint

fake = Faker()

def generate_data(n):
    data = []
    for _ in range(n):
        department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
        if department == "HR":
            job_title = fake.random_element(elements=('Assistant RH', 'Gestionnaire paie', 'Contrôleur de gestion sociale', 'Responsable SIRH', 'Responsable GPEC GEPP'))
        elif department == "Sales":
            job_title = fake.random_element(elements=('Animateur SAV', 'Assistant commercial', 'Chargé d’affaires', 'Gestionnaire CRM', 'Responsable commercial'))
        elif department == "Marketing":
            job_title = fake.random_element(elements=('Assistant marketing', 'Category manager', 'Chef de projet marketing', 'Responsable marketing', 'Ingénieur packaging'))
        elif department == "IT":
            job_title = fake.random_element(elements=('Administrateur système', 'Administrateur réseaux', 'Responsable sécurité informatique', 'Webmaster', 'Data engineer'))
        else:
            job_title = fake.random_element(elements=('Assistant de gestion', 'Analyste financier', 'Auditeur interne', 'Comptable', 'Contrôleur de gestion'))

        gender = fake.random_element(elements=("Male", "Female"))
        age = randint(28, 52)
        years_at_company = randint(1, 12)
        education_level = fake.random_element(elements=("BTS", "Licence", "Bachelor", "Master", "Ingenieur"))
        if education_level == "BTS":
            min_salary = 23000
            max_salary = 30999
        elif education_level in ["Licence", "Bachelor"]:
            min_salary = 31000
            max_salary = 34999
        elif education_level in ["Master", "Ingenieur"]:
            min_salary = 35000
            max_salary = 65000
        else:
            min_salary = 0
            max_salary = 0
        salary = f"{randint(min_salary, max_salary)}€"
        bonus_percent = fake.random_element(elements=("0%", "5%", "10%", "15%", "20%"))
        bonus_value = f"{int(salary[:-1]) * int(bonus_percent[:-1]) / 100}€"
        benefits_package = fake.random_element(elements=("Health", "Dental", "Vision", "Health/Dental", "Health/Vision", "Dental/Vision", "Health/Dental/Vision"))
        if benefits_package.count("/") == 0:
            benefits_package_value = "€500"
        elif benefits_package.count("/") == 1:
            benefits_package_value = "€1000"
        else:
            benefits_package_value = "€1500"

        data.append([_, department, job_title, gender, age, years_at_company, education_level, salary, bonus_percent, bonus_value, benefits_package, benefits_package_value])

    return pd.DataFrame(data, columns=["ID", "Department", "Job Title", "Gender", "Age", "Years at Company", "Education Level", "Salary", "Bonus %", "Bonus Value", "Benefits Package", "Benefits Package Value"])

st.title('Fake Data Generator')

n = st.number_input('Enter the number of data you want to generate (max 1000)', min_value=1, max_value=1000, value=1)

if st.button('Generate Data'):
    df = generate_data(n)
    st.write(df.head(50))

    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="fake_data.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)