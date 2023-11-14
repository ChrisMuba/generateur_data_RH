import streamlit as st
import pandas as pd
from faker import Faker
from random import randint, choice

fake = Faker()

# Define elements for departments
departments = {"HR": ("Assistant RH", "Gestionnaire paie", "Contrôleur de gestion sociale", "Responsable SIRH", "Responsable GPEC GEPP"),
               "Sales": ("Animateur SAV", "Assistant commercial", "Chargé d’affaires", "Gestionnaire CRM", "Responsable commercial"), 
               "Marketing": ("Assistant marketing", "Category manager", "Chef de projet marketing", "Responsable marketing", "Ingénieur packaging"),
               "IT": ("Administrateur système", "Administrateur réseaux", "Responsable sécurité informatique", "Webmaster", "Data engineer"),
               "Finance": ("Assistant de gestion", "Analyste financier", "Auditeur interne", "Comptable", "Contrôleur de gestion")}

# Streamlit app
st.title('Fake HR Data Generator')

# Get number of rows from user
num_rows = st.number_input('Number of rows to generate', 1, 1000) 

# Generate data
data = pd.DataFrame(columns=['ID', 'Department', 'Job Title', 'Gender', 'Age', 'Years_at_Company', 
                              'Education_Level', 'salary', 'Bonus %', 'Bonus_Value', 'Benefits_Package', 'Benefits_Package_Value'])

for i in range(num_rows):
    data.loc[i] = [i+1, 
                   fake.random_element(elements=list(departments.keys())),
                   fake.random_element(elements=departments[data.loc[i,'Department']]), 
                   fake.random_element(elements=['Male','Female']),
                   randint(28,52), 
                   randint(1,12),
                   fake.random_element(elements=["BTS", "Licence", "Bachelor", "Master", "Ingenieur"]),
                   fake_salary(data.loc[i,'Education_Level']),
                   fake.random_element(elements=[0,5,10,15,20]), 
                   fake_bonus(data.loc[i,'salary'], data.loc[i,'Bonus %']),
                   fake_benefits(), 
                   fake_benefits_value(data.loc[i,'Benefits_Package'])]

# Display first 50 rows
st.dataframe(data.head(50))

# Export to CSV button
st.download_button(
   "Press to Download",
   data.to_csv(index=False),
   "fake_data.csv",
   "text/csv",
   key='download-csv'
)

# Helper functions
def fake_salary(education):
    if education == "BTS":
        return f"{randint(23000, 30999)}€"
    elif education in ["Licence", "Bachelor"]:
        return f"{randint(31000, 34999)}€" 
    elif education in ["Master", "Ingenieur"]:
        return f"{randint(35000, 65000)}€"
    else:
        return "0€"

def fake_bonus(salary, bonus):
    return f"{int(float(salary) * bonus/100)}€" 

def fake_benefits():
    return choice(["Health", "Dental", "Vision", "Health/Dental", "Dental/Vision", "Health/Vision"])

def fake_benefits_value(benefits):
    if len(benefits.split("/")) == 1:
        return "500€"
    elif len(benefits.split("/")) == 2: 
        return "1000€"
    else: 
        return "1500€"