import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import randint, uniform

# Instantiate a faker object
fake = Faker()

# Department job titles
departments = ["HR", "Sales", "Marketing", "IT", "Finance"]

# Generate a single row of data
def generate_row(emp_id):
    department = fake.random_element(elements=departments)
    gender = fake.random_element(elements=("Male", "Female"))
    gross_monthly_salary = randint(1917, 5417)
    avg_employer_contributions = round(gross_monthly_salary * 0.33, 2)
    monthly_cost = gross_monthly_salary + avg_employer_contributions
    num_months_presence = randint(1, 12)
    annual_cost = monthly_cost * num_months_presence
    
    return {
        "ID": emp_id,
        "Last Name": fake.last_name(),
        "First Name": fake.first_name(),
        "Gender": gender,
        "Department": department,
        "Gross Monthly Salary (€)": gross_monthly_salary,
        "Average Employer Contributions (€)": avg_employer_contributions,
        "Monthly Cost (€)": monthly_cost,
        "Number of Months of Presence": num_months_presence,
        "Annual Cost (€)": annual_cost
    }

# Generate fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    st.title("Fake HR Data Generator")
    
    num_entries = st.number_input("Enter the number of data entries to generate (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")
    
    if st.button("Generate HR Data"):
        df = generate_hr_data(num_entries)
        st.dataframe(df.head(50))
        
        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()