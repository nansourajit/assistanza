import streamlit as st
import random

c=0
inp = random.randint(1, 20)

def check(val):
    global c,inp
    c+=1
    if (val < inp):
        st.info("Try again, guess a greater number")
    elif (val > inp):
        st.info("Try again, guess a smaller number")
    elif(val==inp):
        inp=random.randint(1, 10)
        c=0
        st.success(":heavy_check_mark: Perfect guessing! You have won!:grinning_face_with_star_eyes:")
    if (c == 10):
        inp=random.randint(1, 10)
        c=0
        st.warning(":pensive: You have used maximum number of chances.....! Game Over! :pensive:")
