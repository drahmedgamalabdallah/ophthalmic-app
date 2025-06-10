# app.py
import streamlit as st

st.set_page_config(page_title="Ophthalmology App", page_icon="👁️", layout="centered")

st.title("👁️ Vision Planner")
st.markdown("Welcome to the Vision Planner web app.")
st.markdown("Choose a tool from the sidebar to get started:")
st.markdown("""
Use the sidebar to navigate:
- Refractive Surgery Planner
- Strabismus Surgery Planner
- About this App
""")

