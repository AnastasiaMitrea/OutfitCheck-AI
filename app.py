import streamlit as st
import random
from transformers import pipeline
import torch

st.set_page_config(page_title="OutfitCheck AI", page_icon="👗", layout="wide")

# Initialize models (caching to avoid reloading)
@st.cache_resource
def load_models():
    # Using a very small model for local execution as requested
    # flan-t5-small is small enough to run locally and follows instructions
    generator = pipeline("text2text-generation", model="google/flan-t5-small")
    return generator

st.title("👗 OutfitCheck AI")
st.markdown("Your digital stylist bridging the gap between *having clothes* and *having an outfit*.")

mock_closet = [
    "Black elegant dress", "White t-shirt", "Blue denim jacket", 
    "High-waisted wide-leg jeans", "Red sneakers", "Beige trench coat", "Black leather boots"
]

try:
    with st.spinner("Loading AI Models locally..."):
        llm = load_models()
    models_loaded = True
except Exception as e:
    st.error(f"Error loading models: {e}")
    models_loaded = False

st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to:", ["My Virtual Closet", "🤖 AI Stylist Agent", "🧠 Fashion Critic Agent"])

if menu == "My Virtual Closet":
    st.header("👕 My Virtual Closet")
    col1, col2, col3 = st.columns(3)
    for i, item in enumerate(mock_closet):
        if i % 3 == 0: col1.info(item)
        elif i % 3 == 1: col2.info(item)
        else: col3.info(item)

elif menu == "🤖 AI Stylist Agent":
    st.header("🤖 AI Contextual Stylist")
    st.markdown("This agent considers the weather and occasion to suggest the best outfit from your closet.")
    context = st.text_input("Occasion/Weather (e.g., 'Casual coffee date, sunny 20°C'):")
    
    if st.button("Generate Outfit") and context and models_loaded:
        with st.spinner("Agent is thinking..."):
            prompt = f"Suggest an outfit from this list: {', '.join(mock_closet)} for this occasion: {context}."
            response = llm(prompt, max_length=50)[0]['generated_text']
            
            st.success("Here is your suggested outfit!")
            st.write(f"**Agent says:** {response}")
            st.markdown("### Recommended Items")
            # Mock visualization mapping
            st.write(f"Top: {random.choice(mock_closet[:3])}")
            st.write(f"Bottom: {random.choice(mock_closet[3:5])}")
            st.write(f"Shoes: {mock_closet[-1]}")

elif menu == "🧠 Fashion Critic Agent":
    st.header("🧠 Fashion Critic Agent")
    st.markdown("This agent provides stylistic feedback on your chosen outfit.")
    outfit_to_review = st.text_input("Outfit to review (e.g., 'Red sneakers with a black elegant dress'):")
    
    if st.button("Review Outfit") and outfit_to_review and models_loaded:
        with st.spinner("Critic is evaluating..."):
            prompt = f"Provide a short fashion critique for this outfit: {outfit_to_review}."
            response = llm(prompt, max_length=50)[0]['generated_text']
            
            st.info("Critic Feedback:")
            st.write(f"**Critic says:** {response}")
