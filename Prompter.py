#Importing required libraries
import streamlit as st
import transformers
from transformers import pipeline
import webbrowser
import datetime

model_name = "gpt2"

#Function to load the pre-trained model & handle potential errors
def load_model():
    try:
        generator = pipeline("text-generation", model=model_name)
        return generator
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

generator = load_model()

#Sidebar
with st.sidebar:
    st.title("Dashboard")

    timer = st.checkbox("Display time")
    if timer:
        now = datetime.datetime.now()
        st.write("Current Time:")
        st.write(now.strftime("%H:%M:%S %p"))

    st.subheader("Developed by Aditee Kashyap")
    st.markdown("<p style='font-size: 14px'>My socials</p>", unsafe_allow_html=True)
    if st.button("Instagram"):
        webbrowser.open("https://www.instagram.com/_.i_am_too_lazy._")
    if st.button("GitHub"):
        webbrowser.open("github.com/aditee-k")
    if st.button("LinkedIn"):
        webbrowser.open("https://www.linkedin.com/in/aditee-kashyap")    
    
    if st.button("Click me for fun!"):
        st.balloons()  # Fun animation on button click

st.title("Hi, I'm Prompter...")
st.header("Create Art With Your Prompts!")
st.header("")
# User input for text format and prompt
text_format = st.selectbox("Choose Text Format", ["Prose", "Script"])
prompt = st.text_input("Enter your prompt:")

# Generate text if model is loaded and prompt is provided
if generator and prompt:
    try:
        if text_format == "Prose":
            #Adjust parameters for prose generation (e.g., top_k, do_sample)
            generation = generator(prompt, max_length=200, top_k=70, do_sample=True)
        elif text_format == "Script":
            #Adjust parameters for script generation (e.g., num_return_sequences)
            generation = generator(prompt, max_length=500, num_return_sequences=2)
        else:
            st.warning("Invalid text format selected.")
            generation = None

        if generation:
            generated_text = generation[0]["generated_text"]
            st.success("Generated Text:")
            st.write(generated_text)
        else:
            st.warning("Generation failed.")
    except Exception as e:
        st.error(f"Error during generation: {e}")
else:
    st.info("Please provide a prompt.")