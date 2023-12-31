import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choices
from random import randint, uniform

# Instantiate a faker object
fake = Faker()

# Department job titles
#departments = ["RH", "Ventes", "Marketing", "IT", "Finance"]

# Generate a single row of data
def generate_row(emp_id):
    gender_weights = [55, 45] # Weights for Homme, Femme
    gender = choices(["Homme", "Femme"], weights=gender_weights, k=1)[0]
    services_weights = [0.03, 0.05, 0.10, 0.10, 0.15, 0.15, 0.18, 0.24]  # Weights for RH, Ventes, Marketing, etc... 
    services = choices(["Communication", "RH", "Marketing", "Finance", "Informatique", "R&D", "Ventes", "Services_techniques"], weights=services_weights, k=1)[0]
    gross_monthly_salary = randint(1917, 5417)
    avg_employer_contributions = round(gross_monthly_salary * 0.33, 2)
    monthly_cost = round(gross_monthly_salary + avg_employer_contributions, 2)
    num_months_presence = randint(1, 12)
    annual_cost = round(monthly_cost * num_months_presence, 2)
    
    return {
        "Matricule": emp_id,
        "Nom": fake.last_name(),
        "Prénom": fake.first_name(),
        "Genre": gender,
        "Service": services,
        "Salaire mensuel brut (€)": gross_monthly_salary,
        "Charges patronales moyenne (€)": avg_employer_contributions,
        "Coût mensuel (€)": monthly_cost,
        "Nombre de mois de présence": num_months_presence,
        "Coût annuel (€)": annual_cost
    }

# Generate fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    st.title("Payroll costs Data Generator")

    st.markdown("💸 Créez des données sur les coûts de paie, les taxes, les déductions et le suivi du temps. Analyser les opérations et les dépenses de paie.")
    
    num_entries = st.number_input("Entrer le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
    
    if st.button("Generate Payroll costs Data"):
        df = generate_hr_data(num_entries)
        df["Coût mensuel (€)"] = df["Coût mensuel (€)"].map("{:.2f}".format)
        df["Coût annuel (€)"] = df["Coût annuel (€)"].map("{:.2f}".format)
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
