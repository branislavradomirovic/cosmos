import streamlit as st

from components import render_landing_page
from styles import apply_global_styles


st.set_page_config(
    page_title="COSMOS Platforma | Inteligencija odlučivanja",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "COSMOS Platforma inteligencije odlučivanja",
    },
)

apply_global_styles()
render_landing_page()
