import streamlit as st
import pandas as pd
import base64
from faker import Faker
from random import choice

# Instantiate a faker object
fake = Faker()

# Generate a single row of data
def generate_row(emp_id):
    last_name = fake.last_name()
    first_name = fake.first_name()
    num_hours_per_week = choice([35, 28, 24, 17.5])
    num_paid_hours_per_month = round(num_hours_per_week * 52 / 12, 2)
    fte = round(num_paid_hours_per_month / 151.67, 2)
    num_months_presence = choice(range(1, 13))
    fte_worked = round(fte * num_months_presence / 12, 2)

    return {
        "ID": emp_id,
        "Last Name": last_name,
        "First Name": first_name,
        "Number of Hours per Week": num_hours_per_week,
        "Number of Paid Hours per Month": num_paid_hours_per_month,
        "Full-time Equivalent (FTE)": fte,
        "Number of Months of Presence": num_months_presence,
        "Full-time Equivalent Worked": fte_worked,
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
        df["Number of Paid Hours per Month"] = df["Number of Paid Hours per Month"].map("{:.2f}".format)
        df["Full-time Equivalent (FTE)"] = df["Full-time Equivalent (FTE)"].map("{:.2f}".format)
        df["Full-time Equivalent Worked"] = df["Full-time Equivalent Worked"].map("{:.2f}".format)
        st.dataframe(df.head(50))

        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
