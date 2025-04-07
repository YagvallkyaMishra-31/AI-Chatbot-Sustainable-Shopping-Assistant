import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro")

st.set_page_config(page_title="Eco Advisor 🌱", page_icon="♻️")
st.markdown("<h1 style='text-align: center;'> Sustainable Shopping Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Created by 12308148 Yagvallkya</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>12318394 Geetanajli</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>12308401 Balaji</h3>", unsafe_allow_html=True)
st.write("Get eco-friendly product recommendations 🌿")
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Reset Chat"):
    st.session_state.messages = []
    if "query" in st.session_state:
        del st.session_state["query"]
    st.rerun()

common_products = [
    "Plastic bottles", "Shampoo", "Toothbrush", "Detergent",
    "Shoes", "Clothing", "Food storage", "Tissue paper"
]

st.markdown("### Choose from a product below:")
col1, col2 = st.columns(2)
for i in range(0, len(common_products), 2):
    with col1:
        if st.button(common_products[i]):
            st.session_state.query = common_products[i]
    if i + 1 < len(common_products):
        with col2:
            if st.button(common_products[i + 1]):
                st.session_state.query = common_products[i + 1]
user_input = st.text_input("Or type your own product:", key="input")
final_input = st.session_state.get("query") or user_input

if st.button("Go Green") and final_input:
    try:
        with st.spinner("Finding Eco alternatives... 🌿"):
            prompt = f"Suggest 3 eco-friendly alternatives to the product: {final_input}. Add short reasons."
            response = model.generate_content(prompt)
            reply = response.text

            st.session_state.messages.append(("You", final_input))
            st.session_state.messages.append(("EcoBot", reply))

        if "query" in st.session_state:
            del st.session_state["query"]

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.markdown("### Chat History:")
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(
            f"<div style='background-color:#DCF8C6;color:#000000;padding:10px;border-radius:10px;margin:5px 0;text-align:right'><b>You:</b> {msg}</div>",
            unsafe_allow_html=True)
    else:

        st.markdown(
            f"<div style='background-color:#E0F7FA;color:#00796B;padding:10px;border-radius:10px;margin:5px 0'><b>EcoBot:</b> {msg}</div>",
            unsafe_allow_html=True)


