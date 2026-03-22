import streamlit as st
import pickle
import pandas as pd

st.title("Deploying our model")
st.write("Logistic Regression")

age=st.number_input("Enter the Age",min_value=20,max_value=60,step=2)
gender=st.selectbox("Gender",[0,1])
cp = st.number_input("Chest Pain Type",min_value=0, max_value=3,value=0)
trestbps= st.number_input("Resting blood pressure",min_value=0,max_value=3)
chol=st.number_input("cholestrol", min_value=100,max_value=600,value=200)
fbs=st.selectbox("Fasting Blood pressure",[0,1])
restecg= st.number_input("Resting ECG",min_value=0,max_value=2,value=0)
thalach= st.number_input("Max heart rate achieved",min_value=60,max_value=250,value=150)
exang=st.selectbox("Exercise Induced Angina",[0,1])
oldpeak= st.number_input("Old Peak",min_value=0,max_value=10,value=1,step=1)
slope= st.number_input("Slope",min_value=0,max_value=2,value=0)

ca= st.number_input("Number of major vessels",min_value=0,max_value=3,step=1)
thal= st.number_input("Thal",min_value=1,max_value=3,value=3)


if st.button("Predict"):
    with open("lr_model.pkl", "rb") as f:
        model = pickle.load(f)
        columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", 
           "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
        sample_input = pd.DataFrame([[age, gender, cp, trestbps, chol, fbs, 
           restecg, thalach, exang, oldpeak, slope, ca, thal]], 
                            columns=columns)
        prediction = model.predict(sample_input)
        if prediction[0] == 1:
             st.markdown(
             "<h4 style='color:red;'> Heart disease detected</h3>",
            unsafe_allow_html=True
            )
        else:
            st.markdown(
            "<h4 style='color:green;'> No heart disease detected</h3>",
             unsafe_allow_html=True
    )