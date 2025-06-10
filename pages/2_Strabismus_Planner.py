import streamlit as st
from logic.strabismus_logic import plan_unilateral

st.set_page_config(page_title="Strabismus Surgery Planner", layout="centered")

st.title("Strabismus Surgery Planner")

st.markdown("""
This app calculates the recommended strabismus surgery plan based on patient data,
including deviation type and measurements, following the latest clinical guidelines.
""")

# --- Input Section ---
st.header("Patient Data Input")

deviation_type = st.selectbox("Select deviation type:", ["Exotropia", "Esotropia", "Hypertropia", "Hypotropia"])

# Use number_input instead of selectbox for PD
amount_pd = st.number_input("Deviation amount (PD):", min_value=15, max_value=100, step=5, value=15)

approach = st.radio("Preferred approach:", ["Unilateral", "Bilateral"])

# Custom CSS for centered white button
st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
        height: 3.5em;
        width: 50%;
        font-size: 1.3em;
        font-weight: bold;
        background-color: white;
        color: black;
        border-radius: 8px;
        border: 2px solid #ccc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Surgical Plan"):
    plan = None
    switched = False

    if approach == "Unilateral":
        plan = plan_unilateral(deviation_type, amount_pd)
        if plan["approach"] == "Bilateral":
            switched = True
    else:
        from logic.strabismus_logic import plan_bilateral
        plan = plan_bilateral(deviation_type, amount_pd)

    if switched:
        st.warning("⚠️ Unilateral correction not sufficient — switched to bilateral plan.")

    st.subheader(f"{plan['approach']} Surgical Plan")
    for key, value in plan.items():
        if key != "approach":
            st.write(f"- **{key}**: {value} mm")


    st.markdown("""
    ---
    **Notes:**
    - Recommendations are based on current clinical guidelines.
    - Always correlate with clinical examination and patient-specific factors.
    """)

else:
    st.markdown("*_Enter patient data and click 'Surgical Plan' to see the results._*")
