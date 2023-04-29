# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:16:04 2021

@author: Debosmita
"""

def hd():
    import streamlit as st
    import pandas as pd
    
    
    cardio_data = pd.read_csv('cardio2.csv')
    cardio_data.drop(['id'],axis=1,inplace=True)
    
    x = cardio_data.drop('cardio',axis=1)
    y = cardio_data['cardio']
    from sklearn.model_selection import train_test_split
    x_tarin,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
    from sklearn.linear_model import LogisticRegression
    logmodel = LogisticRegression()
    logmodel.fit(x_tarin,y_train)
    
    
    st.title("Heart Disease Predictor")
    st.image("Heart.jpg",width = 700)
    st.header("Know your Health Condition")
    i1 = st.slider('Age', 0, 150, 1)
    i2 = st.selectbox("Gender:",["Female","Male"])
    if(i2=="Male"):
        i2=2
    if(i2=="Female"):
        i2=1
    i3 = st.number_input("Height in centimeter: ",0.00,500.00,step = 0.01)
    i4 = st.number_input("Weight in kg: ",0.00,500.00,step = 0.01)
    i5 = st.number_input("Systolic Blood Pressure: ",0,500,step = 1)
    i6 = st.number_input("Diastolic Blood Pressure: ",0,500,step = 1)
    i7 = st.selectbox("Cholestrol: ",['Normal','Above Normal','Well Above Normal'])
    if(i7=="Normal"):
        i7=1
    if(i7=="Above Normal"):
        i7=2
    if(i7=="Well Above Normal"):
        i7=3
    i8 = st.selectbox("Glucose: ",['Normal','Above Normal','Well Above Normal'])
    if(i8=="Normal"):
        i8=1
    if(i8=="Above Normal"):
        i8=2
    if(i8=="Well Above Normal"):
        i8=3
    i9 = st.selectbox("Do you smoke?",['No',"Yes"])
    if(i9=="Yes"):
        i9=1
    if(i9=="No"):
        i9=0
    i10 = st.selectbox("Do you Intake alcohol?",["No","Yes"])
    if(i10=="Yes"):
        i10=1
    if(i10=="No"):
        i10=0
    i11 = st.selectbox("Are you Physically active?",["No","Yes"])
    if(i11=="Yes"):
        i11=1
    if(i11=="No"):
        i11=0
    
    Out=logmodel.predict([[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11]])
    
    if st.button("Predict"):
        if Out==1:
            st.error(f"High Chances of having Heart Disease! Consult a doctor soon to be assured about your heart conditions. Do not worry and Take care!")
        elif Out==0:
            st.success(f"Wow! You are fine! Let's take a walk and keep our heart healthy all the time!")
            st.balloons()
