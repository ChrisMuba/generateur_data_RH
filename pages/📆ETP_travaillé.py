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
        "Matricule": emp_id,
        "Nom": last_name,
        "Prénom": first_name,
        "Nombre_heures_par_semaine": num_hours_per_week,
        "Nombre_heures_rémunérées_par_mois": num_paid_hours_per_month,
        "Equivalent_temps_plein": fte,
        "Nombre_de_mois_de_présence": num_months_presence,
        "Equivalent_temps_plein_travaillé": fte_worked,
    }

# Generate fake HR data
def generate_hr_data(num_entries):
    data = [generate_row(i) for i in range(1, num_entries + 1)]
    df = pd.DataFrame(data)
    return df

# Streamlit app
def main():
    st.title("Générateur ETP & ETP travaillé")

    num_entries = st.number_input("Entrez le nombre de données à générer (max 1000)", min_value=1, max_value=1000, value=50, step=1, format="%d")

    if st.button("Générer les données"):
        df = generate_hr_data(num_entries)
        df["Nombre d'heures rémunérées par mois"] = df["Nombre d'heures rémunérées par mois"].map("{:.2f}".format)
        df["Equivalent temps plein"] = df["Equivalent temps plein"].map("{:.2f}".format)
        df["Equivalent temps plein travaillé"] = df["Equivalent temps plein travaillé"].map("{:.2f}".format)
        st.dataframe(df.head(50))

        # Export data as CSV
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="hr_data.csv">Télécharger le fichier CSV</a>'
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
