# Code generated using AI (Gemini) for MDS Project MVP
import streamlit as st
import random

st.set_page_config(page_title="OutfitCheck AI", page_icon="??", layout="wide")

st.title("? OutfitCheck AI")
st.markdown("Your digital stylist bridging the gap between *having clothes* and *having an outfit*.")

mock_closet = [
    "Black elegant dress", "White t-shirt", "Blue denim jacket", 
    "High-waisted wide-leg jeans", "Red sneakers", "Beige trench coat", "Black leather boots"
]

st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to:", ["My Virtual Closet", "?? AI Stylist Agent", "Outfit Visualization"])

if menu == "My Virtual Closet":
    st.header("?? My Virtual Closet")
    col1, col2, col3 = st.columns(3)
    for i, item in enumerate(mock_closet):
        if i % 3 == 0: col1.info(item)
        elif i % 3 == 1: col2.info(item)
        else: col3.info(item)

elif menu == "?? AI Stylist Agent":
    st.header("?? AI Contextual Stylist")
    context = st.text_input("Occasion/Weather (e.g., 'Casual coffee date, sunny 20øC'):")
    if st.button("Generate Outfit") and context:
        with st.spinner("Agent is thinking..."):
            st.success("Here is your suggested outfit!")
            st.markdown(f"""
            **Based on your closet and the occasion '{context}', I suggest:**
            *   **Top/Main:** {random.choice(mock_closet[:3])}
            *   **Bottom/Layer:** {random.choice(mock_closet[3:5])}
            *   **Shoes:** {mock_closet[-1]}
            """)

elif menu == "Outfit Visualization":
    st.header("?? Outfit Visualization")
    st.info("AI Outfit Visualization Coming Soon!")
