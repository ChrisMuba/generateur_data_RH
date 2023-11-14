import streamlit as st
import pandas as pd
from faker import Faker
from random import randint

st.title('Fake HR Data Generator')

num_rows = st.number_input('Number of rows', min_value=1, max_value=1000, value=100)

if num_rows > 1000:
    st.error('Maximum number of rows is 1000')
    num_rows = 1000

fake = Faker()

data = []
for i in range(num_rows):

    id = i+1
    
    department = fake.random_element(elements=("HR", "Sales", "Marketing", "IT", "Finance"))
    
    if department == "HR":
        job_title = fake.random_element(elements=("Assistant RH", "Gestionnaire paie", "Contrôleur de gestion sociale", "Responsable SIRH", "Responsable GPEC GEPP"))
    elif department == "Sales":
        job_title = fake.random_element(elements=("Animateur SAV", "Assistant commercial", "Chargé d’affaires", "Gestionnaire CRM", "Responsable commercial"))
    elif department == "Marketing":
        job_title = fake.random_element(elements=("Assistant marketing", "Category manager", "Chef de projet marketing", "Responsable marketing", "Ingénieur packaging"))
    elif department == "IT":
        job_title = fake.random_element(elements=("Administrateur système", "Administrateur réseaux", "Responsable sécurité informatique", "Webmaster", "Data engineer"))
    elif department == "Finance":
        job_title = fake.random_element(elements=("Assistant de gestion", "Analyste financier", "Auditeur interne", "Comptable", "Contrôleur de gestion"))

    gender = fake.random_element(elements=('Male','Female'))
    
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
    
    bonus_pct = fake.random_element(elements=('0%', '5%', '10%', '15%', '20%'))
    bonus_pct = int(bonus_pct.replace('%', ''))
    bonus_value = round(int(salary.replace('€', '')) * (bonus_pct / 100))
    
    benefits = fake.random_elements(elements=('Health','Dental','Vision'), length=randint(1,3), unique=True)
    benefits_str = '/'.join(benefits)
    num_benefits = len(benefits)
    if num_benefits == 1:
        benefits_value = 500
    elif num_benefits == 2:
        benefits_value = 1000
    else:
        benefits_value = 1500
        
    data.append([id, department, job_title, gender, age, years_at_company, education_level, salary, bonus_pct, bonus_value, benefits_str, benefits_value])
    
df = pd.DataFrame(data, columns=['ID', 'Department', 'Job Title', 'Gender', 'Age', 'Years at Company', 'Education Level', 'Salary', 'Bonus %', 'Bonus Value', 'Benefits Package', 'Benefits Value'])

st.dataframe(df.head(50))

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button("Press to Download", csv, "fake_hr_data.csv", "text/csv", key='download-csv')