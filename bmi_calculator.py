# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:12:39 2021

@author: lenovo
"""

import streamlit as st

def cal():    
    st.header("**BMI Calculator**")
    st.image("BMI.png",width = 700)
    i=st.number_input("Enter your age:",21,200)
    if(i>20):    
    
        a=st.number_input("Enter your weight in kgs:",1,500)
        b=st.number_input("Enter your height in ft.:",1.00,20.00)
    
        bm=a/(b*b*0.3048*0.3048)
        bmi=round(bm,2)
        if(st.button("Calculate my BMI")):
            st.success("Your BMI is :point_down::")
            st.info(bmi)
            if(bmi<18.5):
                st.warning("You are underweight!")
            if(bmi>=18.5 and bmi<=24.9):
                st.success("You have a perfect height-weight balance and you seem healthy!")
                st.balloons()
            if(bmi>=25.0 and bmi<=29.9):
                st.warning("You are overweight and in a pre-obesity stage!")
            if(bmi>=30.0 and bmi<=34.9):
                st.warning("You are belonging in obesity class-I!")
            if(bmi>=35.0 and bmi<=39.9):
                st.warning("You are belonging in obesity class-II!")
            if(bmi>=40.0):
                st.warning("You are belonging in obesity class-III!")
    st.write("")
    st.write("")    
    st.write("**Note:**You can calculate your BMI if you are above 20 years old")    
    st.subheader("Nutritional Status Chart")   
    BMI_Index = {
    "BMI":["Below 18.5","18.5–24.9","25.0–29.9","30.0–34.9","35.0–39.9","Above 40"],
    "Nutritional Status":["Underweight","Normal weight","Pre-obesity","Obesity class I","Obesity class II","Obesity class III"],
    }  
    st.table(BMI_Index)
    
    
