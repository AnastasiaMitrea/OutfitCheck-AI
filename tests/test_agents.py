import pytest
from transformers import pipeline

# We use a fixture to load the model only once for the tests
@pytest.fixture(scope="module")
def llm_pipeline():
    # Load the same small model as in app.py
    generator = pipeline("text2text-generation", model="google/flan-t5-small")
    return generator

def test_stylist_agent_eval(llm_pipeline):
    """
    Eval for the AI Stylist Agent.
    It checks if the model can generate a non-empty outfit suggestion based on weather.
    """
    context = "Sunny 25 degrees, going to the beach"
    mock_closet = ["Swimsuit", "Sunglasses", "Flip flops", "Winter Coat", "Boots"]
    prompt = f"Suggest an outfit from this list: {', '.join(mock_closet)} for this occasion: {context}."
    
    response = llm_pipeline(prompt, max_length=50)[0]['generated_text']
    
    # Assert that the response is a string and not empty
    assert isinstance(response, str)
    assert len(response) > 0

def test_fashion_critic_agent_eval(llm_pipeline):
    """
    Eval for the Fashion Critic Agent.
    It checks if the model generates feedback for a given outfit.
    """
    outfit = "Red sneakers, green pants, and a purple shirt."
    prompt = f"Provide a short fashion critique for this outfit: {outfit}."
    
    response = llm_pipeline(prompt, max_length=50)[0]['generated_text']
    
    # Assert that the response is a string and not empty
    assert isinstance(response, str)
    assert len(response) > 0
