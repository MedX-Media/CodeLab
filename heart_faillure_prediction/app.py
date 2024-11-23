import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

df= df.drop('DEATH_EVENT', axis=1)
columns= df.columns.to_list()



model = joblib.load('svc.joblib')

def preprocessor(df2):
    sc = StandardScaler()
    df2= sc.fit_transform(df2)
    return df2


st.title('Prediction of heart failure based on patient data :heart:')

age = st.slider("Choose age",0,100)
anaemia = st.selectbox('Does the patient have anameia? 0: No     1: yes', [0,1])
creatinine_phosphokinase = st.number_input("Enter creatinine_phosphokinase level")
diabetes = st.selectbox('Does the patient have diabetes? 0: No     1: yes', [0,1])
ejection_fraction= st.number_input("Enter ejection_fraction")
high_blood_pressure= st.selectbox('Does the patient have high blood pressure? 0: No     1: yes', [0,1])
platelets= st.number_input("Enter platelets level")
serum_creatinine= st.number_input("Enter serum_creatinine level")
serum_sodium= st.number_input("Enter serum_sodium level")
sex= st.selectbox('Choose sex  0: Female     1: Male', [0,1])
smoking= st.selectbox('Does the patient smoke? 0: No     1: yes', [0,1])
time= st.number_input('Follow-up period (days)')

def predict(): 
    row = np.array([age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking, time]) 
    X = pd.DataFrame([row], columns = columns)
    p_x= preprocessor(X)
    prediction = model.predict(p_x)
    if prediction[0] == 1: 
        st.error('The patient is more likely not to survive :thumbsdown:')
    elif prediction[0] == 0:
        st.success('The patient is more likely to survive :thumbsup:') 
        

trigger = st.button('Predict', on_click=predict)