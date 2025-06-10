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

# Styled subpage links
st.markdown("### 🔗 Navigate to Tools")
st.markdown(
    """
    <ul style='font-size: 20px; line-height: 2; list-style-type: none; padding-left: 0;'>
        <li>👉 <a href='/1_Refractive_Planner' target='_self'>📈 Refractive Planner</a></li>
        <li>👉 <a href='/2_Strabismus_Planner' target='_self'>🧠 Strabismus Planner</a></li>
        <li>👉 <a href='/3_About' target='_self'>ℹ️ About This App</a></li>
    </ul>
    """,
    unsafe_allow_html=True
)

# Footer spacing
st.markdown(" ")
st.caption("Developed by Dr. Ahmed Gamal Abdallah, Consultant Ophthalmologist")
