import streamlit as st

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

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Le générateur de données RH est une application gratuite spécialement conçue pour les projets d'études de données 
    en **contrôle de gestion sociale, GPEC / GEPP et autres analyses** de données RH.  
    **👈🏿 Sélectionnez un item dans la barre latérale** pour voir quelques exemples
    de ce que le générateur de data RH peut produire !
    ### Vous voulez en savoir plus ?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
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
