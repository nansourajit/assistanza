# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:18:05 2021

@author: Debosmita
"""

def ct():
    import streamlit as st
    import pandas as pd
    
    covid_data = pd.read_csv('Covid_Final.csv')
    x2 = covid_data.drop('Severity_None',axis=1)
    y2 = covid_data['Severity_None']
    from sklearn.model_selection import train_test_split
    x2_train,x2_test,y2_train,y2_test = train_test_split(x2,y2,test_size=0.3,random_state=3)
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(x2_train,y2_train)
    
    
    st.title("Covid Risk Analysis Predictor")
    st.image("Covid.png",width=700)
    
    st.header("Know your Health Condition")
    
    i10 = st.slider('Age', 0, 150, 1)
    
    if(i10>=0 and i10<=9) :
        i10=1
    if(i10>=10 and i10<=19):
        i10=2
    if(i10>=20 and i10<=24):
        i10=3
    if(i10>=25 and i10<=59):
        i10=4
    if(i10>=60):
        i10=5
       
    i11 = st.selectbox("Gender:",["Female","Male","Transgender"])
    if(i11=="Male"):
        i11=1
    if(i11=="Female"):
        i11=2
    if(i11=="Transgender"):
        i11=3
    
    i1 = st.selectbox("Fever",["No","Yes"])
    if(i1=="Yes"):
        i1=1
    if(i1=="No"):
        i1=0
    i2 = st.selectbox("Tiredness",["No","Yes"])
    if(i2=="Yes"):
        i2=1
    if(i2=="No"):
        i2=0
    i3 = st.selectbox("Dry Cough",["No","Yes"])
    if(i3=="Yes"):
        i3=1
    if(i3=="No"):
        i3=0
    i4 = st.selectbox("Difficulty Breathing",["No","Yes"])
    if(i4=="Yes"):
        i4=1
    if(i4=="No"):
        i4=0
    i5 = st.selectbox("Sore Throat",["No","Yes"])
    if(i5=="Yes"):
        i5=1
    if(i5=="No"):
        i5=0
    i6 = st.selectbox("Pains in body",["No","Yes"])
    if(i6=="Yes"):
        i6=1
    if(i6=="No"):
        i6=0
    i7 = st.selectbox("Nasal congestion",["No","Yes"])
    if(i7=="Yes"):
        i7=1
    if(i7=="No"):
        i7=0
    i8 = st.selectbox("Runny Nose",["No","Yes"])
    if(i8=="Yes"):
        i8=1
    if(i8=="No"):
        i8=0
    i9 = st.selectbox("Diarrhea",["No","Yes"])
    if(i9=="Yes"):
        i9=1
    if(i9=="No"):
        i9=0
    
    i12 = st.selectbox("Mild Symptoms",["No","Yes"])
    if(i12=="Yes"):
        i12=1
    if(i12=="No"):
        i12=0
    
    i13 = st.selectbox("Moderate Symptoms",["No","Yes"])
    if(i13=="Yes"):
        i13=1
    if(i13=="No"):
        i13=0
    
    i14 = st.selectbox("Severe Symptoms",["No","Yes"])
    if(i14=="Yes"):
        i14=1
    if(i14=="No"):
        i14=0
    
    i15 = st.selectbox("Contact with Covid patient:",["No","Yes","Don't Know"])
    if(i15=="Yes"):
        i15=3
    if(i15=="No"):
        i15=2
    if(i15=="Don't Know"):
        i15=1
    Out=model.predict([[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15]])
    
    if st.button("Predict"):
        if Out==0:
            st.error(f"You may have chances of contracting the Virus! Take a test and follow the guidance of the Doctor ASAP!")
        elif Out==1:
            st.success(f"You are Absolutely fine and you have no severity of the Covid disease! Take Care.")
            st.balloons()
