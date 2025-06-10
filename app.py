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
- 💡 Educational insights
""")

# Divider
st.divider()

# Navigation using buttons
st.markdown("### Navigate to Tools")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Refractive Planner"):
        st.switch_page("pages/1_Refractive_Planner.py")
with col2:
    if st.button("Strabismus Planner"):
        st.switch_page("pages/2_Strabismus_Planner.py")
with col3:
    if st.button("About This App"):
        st.switch_page("pages/3_About.py")


# Footer spacing
st.markdown(" ")
st.caption("Developed by Dr. Ahmed Gamal Abdallah, Consultant Ophthalmologist")
