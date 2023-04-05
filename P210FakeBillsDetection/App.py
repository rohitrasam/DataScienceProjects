# Import libraries
import pickle
import numpy as np
import streamlit as st



# Load the trained model
load = open('finalized_model_Bagging_KNN.pkl','rb')
model = pickle.load(load)

# Define the function to make predictions
def predict_note_authentication(diagonal, height_left, height_right, margin_low, margin_up, length):
    inputs = np.array([[diagonal, height_left, height_right, margin_low, margin_up, length]]).astype(np.float64)
    prediction = model.predict(inputs)
    return prediction

# Create the Streamlit app
def main():

    
    html_temp = """
    <div style="background-color: dodgerblue; padding:10px">
    <h2 style="color:white;text-align:center;">Fake Bills Detection App💸 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    
    
    st.write('Predicts whether your bill is genuine or fake based on its features')
    st.write('Please enter the following details')
    diagonal = st.number_input("Enter value Diagonal")
    height_left = st.number_input("Enter value Height of the left side")
    height_right = st.number_input("Enter value Height of the right side")
    margin_low = st.number_input("Enter value Lower side margin")
    margin_up = st.number_input("Enter value Upper side margin")
    length = st.number_input("Enter value Length")
    if st.button("Predict"):
        st.write('predicted Result')
        output = predict_note_authentication(diagonal, height_left, height_right, margin_low, margin_up, length)
        if output == 1:
            st.success("This is a genuine bill")
        else:
            st.warning("This is a fake bill")
        
if __name__=='__main__':
    main()
