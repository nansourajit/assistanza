import streamlit as st
import streamlit.components.v1 as stc
def home2():
    st.title("Welcome to Assistanza! :blush:")
    st.subheader("Let us take a walk to understand the ideation of the entire Application!")
    
    health = """<div style="background-color:#bbdff0;padding:10px;border-radius:10px">
                        <h1 style="color:#0c4059;font-family: cursive; text-align:center;">Health Tracker</h1>
                        </div>
                       """
    hinfo = """<div style="background-color:#e4e6f7;padding:10px;border-radius:10px;text-align:center;">
                        <span style="color:black;font-size:18px;font-family: Times New Roman; text-align:center;">
                        This is majorly to take care of your health. We have three major predictors in this genre. They are: Covid Risk Analysizer, Heart Disease Detector and Diabetes Predictor. We care for you and hence we have made a self help tracking system to help you know about the risks and go to doctor in case you are at high risk.
                        Take care of yourself! Stay Safe and Stay Healthy but don't forget to Stay Happy!</span>
                        </div>
                       """
    bmi = """<div style="background-color:#FCFA72  ;padding:10px;border-radius:10px">
                        <h1 style="color:#D84C0F;font-family: cursive; text-align:center;">BMI Calculator</h1>
                        </div>
                       """
    binfo = """<div style="background-color:#F2FC9E ;padding:10px;border-radius:10px;text-align:center;">
                        <span style="color:black;font-size:18px;font-family: Times New Roman; text-align:center;">
                        Now calculate your BMI and understand whether your weight suits you and is not overweight or underweight. It will tell you whether you require any aid or not and help you live a healthy life based on the BMI calculated. It is as per the WHO standard and speciafically meant for people people above the age of 21 as the calculation vaires for people below that age. 
                        </span>
                        </div>
                       """
    sentiment = """<div style="background-color:#edc4f2;padding:10px;border-radius:10px">
                        <h1 style="color:#7a108f;font-family: cursive; text-align:center;">Sentiment Analysis</h1>
                        </div>
                        """
    sinfo = """<div style="background-color:#f6f0f7;padding:10px;border-radius:10px;text-align:center">
                        <span style="color:black;font-size:18px;font-family: Times New Roman; text-align:center;">
                        Have you ever thought about your sentiments? Life is not a bed of roses and hence your life will give you thorns to deal with. Why not take a chance to know about your mental health? We have made this section for you so that you can predict your current mood and we can do something for you incase you feel low!
                        Hover about the app and don't forget to take a quick jump to this. All the best!
                        </span>
                        </div>
                       """
    task = """<div style="background-color:#cef5cf;padding:10px;border-radius:10px">
                        <h1 style="color:#108f1d ;font-family: cursive; text-align:center;">Task Manager</h1>
                        </div>
                        """
    tinfo = """<div style="background-color:#eef5ed;padding:10px;border-radius:10px;text-align:center">
                        <span style="color:black;font-size:18px;font-family: Times New Roman; text-align:center;">
                        OMG! Your tasks are overburdening you? Forgeting things are becoming common. Now you don't have to worry about that.
                        Because we have come up with an excellent task manager to manage your tasks neatly and in an extremely organized manner.
                        So, let us stop the habit of forgetting and deliver all the works with utmost punctuality!
                        </span>
                        </div>
                       """
    ocr = """<div style="background-color:#ffd1e0;padding:10px;border-radius:10px">
                        <h1 style="color:#8f1043;font-family: cursive; text-align:center;">Optical Character Recognition</h1>
                        </div>
                        """
    oinfo = """<div style="background-color:#f5edf1;padding:10px;border-radius:10px;text-align:center">
                        <span style="color:black;font-size:18px;font-family: Times New Roman; text-align:center;">
                        This is designed in order to help you out to extract text from any images and download the file. You can also hear the audio of the text extracted from the image.
                        This will prove extremely beneficial for any blind person who won't be able to figure out what is written in a softcopy image. Utilize the advantages and get started today!
                        </span>
                        </div>
                       """
    ende = """<div style="background-color:#fafa93;padding:10px;border-radius:10px">
                        <h1 style="color:#d99502;font-family: cursive; text-align:center;">Encryption/Decryption</h1>
                        </div>
                        """
    einfo = """<div style="background-color:#f6f7d7;padding:10px;border-radius:10px;text-align:center">
                        <span style="color:black;font-size:18px;font-family:Times New Roman; text-align:center;">
                        Wanna send some secret message and you don't want anybody else to know about it except the person you want? Here is the perfect solution for you. You can get fully protected and encrypted document which can also be decrypted using the particular key generated.
                        Share the encrypted file and the key with the desired person and you get the original document right away. Have a safe and secured sharing with utmost privacy protection.
                        </span>
                        </div>
                       """
    gm = """<div style="background-color:#ffd4b3;padding:10px;border-radius:10px">
                        <h1 style="color:#d92202;font-family: cursive; text-align:center;">Play Games</h1>
                        </div>
                        """
    ginfo = """<div style="background-color:#fcebde;padding:10px;border-radius:10px;text-align:center">
                        <span style="color:black;font-size:18px;font-family:Times New Roman; text-align:center;">
                        Yohoooo! Playing games are fun. After continuous monotonus jobs you would feel the urge to get refreshed. Here we have presented to you games that may uplift your mood and break open the shackles of boredom.
                        Brainstorm and find out the answers. Get the highest scores and beat your friends in the game. Make your day better. Happy Play In!
                        </span>
                        </div>
                       """
                       
    stc.html(health)
    stc.html(hinfo)
    stc.html(bmi)
    stc.html(binfo)
    stc.html(sentiment)
    stc.html(sinfo)
    stc.html(task)
    stc.html(tinfo)
    stc.html(ocr)
    stc.html(oinfo)
    stc.html(ende)
    stc.html(einfo)
    stc.html(gm)
    stc.html(ginfo)