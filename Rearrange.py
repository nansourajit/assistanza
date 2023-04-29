import streamlit as st
import rgame

try:
    if(st.checkbox("END")):
                     st.success("Thanks for playing :blush::blush:")
                     st.balloons()
                     st.info("Uncheck the checkbox to play again!")
                     
    else:
        st.title("Rearrange the Word :thinking_face:")
        try:
            ch=rgame.shuffled
            r = st.text_input("Rearrange the below word and guess the Correct word!")
            if(st.button("Check Me!")):
                rgame.check2(r)
            if rgame.d==0:
                st.warning("The word to be rearranged is :point_down: :")
                st.info(ch)
                
        except:
                pass
    
except:
        try:
            ch=rgame.shuffled
            r = st.text_input("Rearrange the below word and guess the Correct word!")
            if(st.button("Check Me!")):
                rgame.check2(r)
            if rgame.d==0:
                st.warning("The word to be rearranged is :point_down: :")
                st.info(ch)
                
        except:
                pass