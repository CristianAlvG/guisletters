import streamlit as st
from streamlit_option_menu import option_menu



# Setting page layout to wide
st.set_page_config(layout="wide", page_title="Guisella's Letter", page_icon="images/dragon.png")


# Custom CSS to change the color of st.info box
st.markdown("""
    <style>
    /* Change the background color of the st.info box */
    .css-1v0mbdj {  /* The class name might change; inspect your Streamlit app to find the correct class */
        background-color: #e0f7fa; /* Light blue background */
        color: #000000; /* Black text color */
    }
    </style>
""", unsafe_allow_html=True)


selected = option_menu(
    menu_title=None,  # No title for the menu
    options=["Home", "Dragon", "Bixbee"],  # Menu options
    menu_icon="cast",  # Icon for the menu (optional)
    icons=["house", "card-image", "book"],  # Optional icons from Bootstrap
    default_index=0,  # Start with the first option selected
    orientation="horizontal",  # Ensures the menu is horizontal
    styles={
        "container": {"padding": "0!important", "background-color": "#000000", "color": "white"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#8e00bc",
                     "color":"white"},
        "nav-link-selected": {"background-color": "#8e00bc"},
    }
)

if selected == "Home":
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
            <style>
            .romantic-font {
                font-family: 'Great Vibes', cursive;
                font-size: 36px;
                color: #000000;
                text-align: center;
            }
            </style>
            <p class="romantic-font">Guisella's Letter</p>
            """, unsafe_allow_html=True)




        with open("letter.txt", 'r', encoding="utf-8") as file:
            carta = file.read()

        st.warning(carta)



# Menu Select

if selected == "Dragon":
    col3, col4 = st.columns([1, 4])

    with col3:
        st.image("images/dragon.png", caption="El Dragon de Bixbee")

    with col4:
        st.warning("""Este dragon se llama Shenlong, se ve chiquitito verdad, al parecer
        no era tan pegriloso, pero cuidado Guis!! que se puede hacer más grande si le damos de comer,
        le gustan mucho los sandwiches de mermelada, pero... quien es Bixbee""")

        st.warning("Ahora que sabes usar el menú dirigete a la parte de Bixbee")

        st.markdown(
            '<a href="https://www.flaticon.com/free-icons/cute" title="cute icons">Cute icons created by Freepik - Flaticon</a>',
            unsafe_allow_html=True)



if selected == "Bixbee":
    col5, col6 = st.columns(2)

    with col5:
        st.image("images/boy.png", caption="El niño Bixbee")

    with col6:
        with open("bixbee.txt", 'r', encoding="utf-8") as file:
            bixbee = file.read()
            st.warning(bixbee)

        with open("moraleja.txt", 'r', encoding="utf-8") as file:
            moraleja = file.read()
            st.warning(moraleja)

        # Displaying the clickable link with proper credit
        st.markdown(
            '<a href="https://www.flaticon.com/free-icons/child" title="child icons">Child icons created by Freepik - Flaticon</a>',
            unsafe_allow_html=True)



