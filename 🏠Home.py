
import streamlit as st

st.snow()

st.snow()

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.write("# 🤖 Générateur de data RH")

st.markdown("")

st.markdown(
    """ 
    ### Bienvenu ! 👋🏿
"""
)

st.sidebar.success("Sélectionnez un item ci-dessus.")

st.markdown(
    """
    Cette application a été créée pour fournir des exemples de données RH pouvant être utilisées à des fins d'analyse et de modélisation.📊

    En tant qu'analyste data RH, avoir accès à des exemples de données réalistes est inestimable pour développer des compétences dans des domaines tels que la visualisation des données, l'analyse statistique et la modelisation. 
    Cependant, les données RH réelles contiennent souvent des informations sensibles et ne peuvent pas être partagées publiquement.🙅🏿‍♂️
    
    Notre application vise à résoudre ce problème en générant automatiquement des données RH fictives aux propriétés réalistes, et qui peuvent être utilisées pour des projets personnels, des tutoriels et autres analyses en contrôle de gestion sociale et GPEC / GEPP.💡
    
   
    ### Vous voulez en savoir plus ?
    Le 🤖 Générateur de data RH comporte plusieurs pages, chacune axée sur la production de données à analyser pour une thématique RH différente :
    - [Données générales](https://data-rh.streamlit.app/generateur_data_rh)
    - [Turnover](https://data-rh.streamlit.app/%F0%9F%8F%83%F0%9F%8F%BC%E2%80%8D%E2%99%80%EF%B8%8FTurnover)
    - [Attrition](https://data-rh.streamlit.app/Attrition)
    - [Rémunérations & avantages sociaux](https://data-rh.streamlit.app/Compensation_Benefits)
    - [Coût du recrutement](https://data-rh.streamlit.app/Cost_per_Hire)
    - [Masse salariale](https://data-rh.streamlit.app/Masse_Salariale)
    - [Equivalent temps plein](https://data-rh.streamlit.app/Masse_Salariale)
    

     ### Comment ça marche 🛠️
     **👈🏿 Sélectionnez un item dans la barre latérale** et, d'un simple clic, vous disposerez d'un ensemble de données prêt à être téléchargé et exploré. 📥 !
    
    Toutes les données sont exportables au format CSV pour une analyse plus approfondie dans vos outils préférés comme Excel, Tableau, Power BI ou Python. 
    La randomisation garantit que chaque nouvel ensemble de données est unique, tout en conservant des distributions réalistes. 📊

    J'espère que vous trouverez 🤖 Générateur de data RH utile dans vos propres projets. N'hésitez pas à nous faire part de vos commentaires. 
    Je cherche toujours à améliorer l'outil en fonction des besoins des utilisateurs. Bonne analyse ! 🧠
    
"""
)

with st.sidebar:
    st.image('gif/Robot_Emoji.gif')


st.markdown("")


st.markdown("")


# Add the "made with ❤️ by ..." text in the sidebar
with st.sidebar:
    st.write("Made with ❤️ by Chris MUBA")


st.markdown("")
