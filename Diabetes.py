# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:05:08 2021

@author: Debosmita
"""
def dia():
    import streamlit as st
    import pandas as pd 
    
    
    
    diabetes_data = pd.read_csv("diabetes_final.csv")
    x1 = diabetes_data.drop('class',axis=1)
    y1 = diabetes_data['class']
    from sklearn.model_selection import train_test_split
    x1_tarin,x1_test,y1_train,y1_test = train_test_split(x1,y1,test_size=0.3,random_state=0)
    from sklearn.linear_model import LogisticRegression
    logmodel1 = LogisticRegression(solver='liblinear')
    logmodel1.fit(x1_tarin,y1_train)
    
    
    st.title("Diabetes Predictor")
    st.image("Diabetes.jpg",width = 700)
    st.header("Know your Health Condition")
    i1 = st.slider('Age', 0, 150, 1)
    i2 = st.selectbox("Gender:",["Female","Male"])
    if(i2=="Male"):
        i2=2
    if(i2=="Female"):
        i2=3    
    i3 = st.selectbox("Need to Pee more?",["No","Yes"])
    if(i3=="Yes"):
        i3=1
    if(i3=="No"):
        i3=0
    i4 = st.selectbox("Do you feel Extremely Thirsty?",["No","Yes"])
    if(i4=="Yes"):
        i4=1
    if(i4=="No"):
        i4=0
    i5 = st.selectbox("Sudden Weight Loss:",["No","Yes"])
    if(i5=="Yes"):
        i5=1
    if(i5=="No"):
        i5=0
    i6 = st.selectbox("Sudden weakness:",["No","Yes"])
    if(i6=="Yes"):
        i6=1
    if(i6=="No"):
        i6=0
    i7 = st.selectbox("Do you feel Extremely Hungry?",["No","Yes"])
    if(i7=="Yes"):
        i7=1
    if(i7=="No"):
        i7=0
    i8 = st.selectbox("Genital thrush:",["No","Yes"])
    if(i8=="Yes"):
        i8=1
    if(i8=="No"):
        i8=0
    i9 = st.selectbox("Visual Blurring:",["No","Yes"])
    if(i9=="Yes"):
        i9=1
    if(i9=="No"):
        i9=0
    i10 = st.selectbox("Itching:",["No","Yes"])
    if(i10=="Yes"):
        i10=1
    if(i10=="No"):
        i10=0
    i11 = st.selectbox("Irritability:",["No","Yes"])
    if(i11=="Yes"):
        i11=1
    if(i11=="No"):
        i11=0
    i12 = st.selectbox("Delayed Healing:",["No","Yes"])
    if(i12=="Yes"):
        i12=1
    if(i12=="No"):
        i12=0
    i13 = st.selectbox("Partial Paresis (Paralysis condition):",["No","Yes"])
    if(i13=="Yes"):
        i13=1
    if(i13=="No"):
        i13=0
    i14 = st.selectbox("Muscle Stiffness:",["No","Yes"])
    if(i14=="Yes"):
        i14=1
    if(i14=="No"):
        i14=0
    i15 = st.selectbox("Alopecia (Extreme HairFall):",["No","Yes"])
    if(i15=="Yes"):
        i15=1
    if(i15=="No"):
        i15=0
    i16 = st.selectbox("Obesity (Extreme Weight Gain):",["No","Yes"])
    if(i16=="Yes"):
        i16=1
    if(i16=="No"):
        i16=0
    Out=logmodel1.predict([[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16]])
    
    if st.button("Predict"):
        if Out==1:
            st.error(f"You have fairly high chance of having Diabetes. Do not worry. Consult your doctors at the earliest! Take care!")
        elif Out==0:
            st.success(f"You are absolutely fine! Wanna grab some cookies?")
            st.balloons()
            
            
