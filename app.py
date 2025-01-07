import streamlit as st
import pickle

# Load the trained model with pipeline
model_path = 'model/model.pkl' 

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Streamlit web app
def main():
    st.title("Spam Message Classifier")
    st.write("This app predicts whether a message is Spam or Not Spam.")

    # Input text
    message = st.text_area("Enter your message here:")

    if st.button("Predict"):
        if message.strip():
            # Predict directly using the pipeline model
            prediction = model.predict([message])
            result = "Spam" if prediction[0] == 1 else "Not Spam"

            st.success(f"The message is classified as: {result}")
        else:
            st.warning("Please enter a valid message.")

if __name__ == "__main__":
    main()