import streamlit as st
import pandas as pd
import joblib
st.markdown("""
<style>
.stApp {
    background-image: url("https://imgs.search.brave.com/fn4ab4wk258FkWE5YkBPaM90g3DvcxMsUzX8feLcoGM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cHJpbWVib29rLmlu/L3VwbG9hZHMvaW1h/Z2VzLzE3NTc2NzQ3/MTlfMWNmMWE1MDQ3/YWMyZjhiYTRjODIu/cG5n");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

st.title("💻 Laptop Price Prediction App")
st.write("Enter laptop details to predict the price")

# ---- User Inputs ----
discount = st.selectbox(
    "Discount",
    ["No Discount", "10%", "20%", "30%", "40%"]
)

brand = st.selectbox(
    "Brand",
    ["HP", "Dell", "Lenovo", "Asus", "Acer", "Apple", "MSI"]
)

processor = st.selectbox(
    "Processor",
    ["i3", "i5", "i7", "Ryzen 3", "Ryzen 5", "Ryzen 7", "M1", "M2"]
)

ratings = st.slider("Ratings", 1.0, 5.0, 4.0)
original_price = st.number_input("Original Price", min_value=10000, step=1000)
num_ratings = st.number_input("Number of Ratings", min_value=0, step=10)
num_reviews = st.number_input("Number of Reviews", min_value=0, step=10)
ram = st.selectbox("RAM (GB)", [4, 8, 16, 32])
storage = st.selectbox("Storage (GB)", [128, 256, 512, 1024])

# ---- Prediction ----
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "Discount": [discount],
        "Brands": [brand],
        "processor": [processor],
        "ratings": [ratings],
        "Original_price": [original_price],
        "number_of_ratings": [num_ratings],
        "number_of_reviews": [num_reviews],
        "RAM": [ram],
        "Storage": [storage]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Laptop Price: ₹ {int(prediction):,}")

