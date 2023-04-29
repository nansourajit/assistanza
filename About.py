import streamlit as st
import streamlit.components.v1 as stc
def AboutUs():
    st.title("Made with :heart: by:")
    st.write("")
    st.write("")
    col1, col2, col3 = st.beta_columns(3)
    col10,col11,col12=st.beta_columns(3)
    col4,col5,col6,col7 =st.beta_columns([2,6,6,1])
    col13,col14,col15,col16 =st.beta_columns([1,4,4,1])



    with col1:
     st.image("Dhruba.jpg",width = 200)
    
    with col2:
        st.image("Barna.jpg",width = 200)
    
    with col3:
        st.image("Aashutosh.jpg",width = 200)
    
    with col10:
        dhr = """<div style="background-color:#bbdff0;padding:10px;border-radius:10px; text-align:center">
                        <span style="color:#0c4059;font-family: cursive; text-align:center;">Dhruba Roy</span>
                        </div>
                   """
        stc.html(dhr)
     
    with col11:
        dhr = """<div style="background-color:#bbdff0;padding:10px;border-radius:10px; text-align:center">
                        <span style="color:#0c4059;font-family: cursive; text-align:center;">Barna Debnath</span>
                        </div>
                   """
        stc.html(dhr)
    with col12:
        dhr = """<div style="background-color:#bbdff0;padding:10px;border-radius:10px; text-align:center">
                        <span style="color:#0c4059;font-family: cursive; text-align:center;">Aashutosh Jaiswal</span>
                        </div>
                   """
        stc.html(dhr)
    
    with col5:
        st.image("Sourajit.jpg",width = 200)
       
    
    with col6:
        st.image("Diya.jpg",width = 200)
    
    with col14:
        dhr = """<div style="background-color:#bbdff0;padding:10px;border-radius:10px; text-align:center">
                        <span style="color:#0c4059;font-family: cursive; text-align:center;">Sourajit Nan</span>
                        </div>
                   """
        stc.html(dhr)
    
    with col15:
        dhr = """<div style="background-color:#bbdff0;padding:10px;border-radius:10px; text-align:center">
                        <span style="color:#0c4059;font-family: cursive; text-align:center;">Debosmita Ganguli</span>
                        </div>
                   """
        stc.html(dhr)

   
    
