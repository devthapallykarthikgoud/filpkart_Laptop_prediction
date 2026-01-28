import streamlit as st
import pandas as pd
import joblib
st.markdown("""
<style>
.stApp {
    background-image: url("https://imgs.search.brave.com/6qOydwnpzrFodqQ-mBLvafwMus-aNs7Us2TjwqleLC0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTIz/NDE2MDY2Mi9waG90/by9mbGlwa2FydC1s/b2dvLWRpc3BsYXll/ZC1vbi1hLXBob25l/LXNjcmVlbi1hbmQt/ZmxpcGthcnQtd2Vi/c2l0ZS1kaXNwbGF5/ZWQtb24tYS1sYXB0/b3Atc2NyZWVuLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1K/TnVNaGJDWi1aQXpO/VFdzY3FnOXoxNTBD/S1RveUNPdEhUQ19R/Q19nN1I4PQ");
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


