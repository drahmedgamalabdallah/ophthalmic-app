import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Ophthalmic AI Planner",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar by default
)

# Main title
st.title("👁️ Ophthalmic AI Planner")
st.markdown("#### A smart assistant for surgical decision-making in ophthalmology")

# Description
st.markdown("""
Welcome to the **Ophthalmic AI Planner**, a clinical decision-support tool designed for ophthalmologists and refractive surgeons.

This platform provides:
- 📈 **Refractive surgery analysis** to assist in selecting LASIK, PRK, Phakic or Pseudophakic IOLs.
- 🎯 **Strabismus surgery planning** using intelligent nomograms based on deviation types and amounts.
- 💡 Educational insight into the logic behind planning algorithms.

Feel free to explore the tools:
""")

# Divider
st.divider()

# Page links
st.page_link("pages/1_Refractive_Planner.py", label="🔍 Refractive Planner", icon="📈")
st.page_link("pages/2_Strabismus_Planner.py", label="🎯 Strabismus Planner", icon="🧠")
st.page_link("pages/3_About.py", label="ℹ️ About This App", icon="ℹ️")

# Footer spacing
st.markdown(" ")
st.caption("Developed by Dr. Ahmed Gamal Abdallah, Consultant Ophthalmologist")
