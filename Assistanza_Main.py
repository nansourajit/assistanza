import streamlit as st
import hashlib
import pandas as pd
import streamlit.components.v1 as stc
import sqlite3 
import sentimentanalysis as s
import CovidTracker as ctracker
import HeartDisease as h
import Diabetes as diab
import base64
import pytesseract
import numpy as np
from gtts import gTTS
from PIL import Image
import Home
import About
import os
import bmi_calculator as bm
        
#streamlit run .\Assistanza_Main.py
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'



def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if(make_hashes(password)==hashed_text):
        return hashed_text
    return False

import sqlite3
com=sqlite3.connect('newdata.db')
c=com.cursor()

def duplicate_user(un):
    c.execute('SELECT username FROM usertable WHERE username=?',(un,))
    data=c.fetchall()
    if(len(data)!=0):
        return True

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')
    
def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES (?,?)',(username,password))
    com.commit()

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data

def delete_users(un):
    c.execute('DELETE FROM usertable where username=?',(un,))
    com.commit()
st.markdown(
    f"""
    <style>
   .css-17eq0hr {{
   background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
}}
    
    </style>"""
    ,
    unsafe_allow_html=True
)
    
    
choice=st.sidebar.selectbox("Menu",["Login","Signup"])

file_ = open("1.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

lg=st.markdown(
    f'<img width="1190px" src="data:image/gif;base64,{data_url}" alt="Welcome">',
    unsafe_allow_html=True,
)

main_bg = "1.gif"
main_bg_ext = "gif"



v=st.markdown(
    f"""
    <style>
    .reportview-container .main .block-container{{
        max-width: 1200px;
        padding-top: 28px;
        padding-right: 0;
        padding-left: 0;
        padding-bottom:0;
    }}
    .reportview-container .main {{
        background-color:#262A55;}}
    
   .sidebar.sidebar-content {{
    background:#2e7bcf;
}}
    
    </style>"""
    ,
    unsafe_allow_html=True
)

if choice == "Signup":
    st.markdown(
                    f"""
                    <style>
                    .reportview-container {{
                        background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True)
    st.title("Assistanza: A self help Application!")
    lg.empty()
    v.empty()
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password') 
    
    if st.button("SignUp"):
        create_usertable()
        if(duplicate_user(new_user)):
            st.error("USER already exists! Please Login! Else Use a different UserName!")
        elif(new_user.lower()=="admin"):
            st.error("ADMIN User Name cannot be used!")
        else:
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login to login into the application!")




if choice=="Login":
    username=st.sidebar.text_input("User Name")
    password=st.sidebar.text_input("Password", type='password')

    chc=st.sidebar.checkbox("Login")
    if(chc):
  
        lgo=st.title("Assistanza: A self help Application!")
        hashed_pswd = make_hashes(password)
        result=login_user(username,check_hashes(password,hashed_pswd))
        
        
        if (result and (username=="ADMIN") and (password=="1245778@AdminAssistanza")):
            chc2=st.sidebar.button("Logout")
            if(chc2):
                lg.empty()
                v.empty()
                st.markdown(
                f"""
                <style>
                .reportview-container .main .block-container{{
                    max-width: 1200px;
                    padding-top: 28px;
                    padding-right: 0;
                    padding-left: 0;
                    padding-bottom:0;
                }}
                .reportview-container .main {{
                    background-color:#F8EDF3;}}
                
                </style>"""
                ,
                unsafe_allow_html=True
                )
                st.image("logout.png",width = 1200)
            else:
                st.sidebar.success("Logged In as {}".format(username))
                lg.empty()
                v.empty()
                task = st.selectbox("Task",["Delete Users","View Users"])
                if task == "View Users":
                    st.write("Welcome!")
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)
                if task == "Delete Users":
                    unique_list = [i[0] for i in view_all_users()]
                    delete_by_task_name =  st.selectbox("Here are the list of users. Select the one you want to delete! **You cannot Delete the ADMIN**",unique_list)
                    if(st.button("Delete User")):
                        if(delete_by_task_name.lower()=="admin"):
                            st.error("ADMIN cannot be Deleted")
                        else:
                            delete_users((delete_by_task_name))
                            val=view_all_users()
                            clean_db = pd.DataFrame(val,columns=["Username","Password"])
                            st.dataframe(clean_db)
                            st.success("Successfully Deleted!")

        elif (result and (username.lower()!="admin") and (password!="1245778@AdminAssistanza")):
            chc2=st.sidebar.button("Logout")
            if(chc2):
                lg.empty()
                v.empty()
                st.markdown(
                f"""
                <style>
                .reportview-container .main .block-container{{
                    max-width: 1200px;
                    padding-top: 28px;
                    padding-right: 0;
                    padding-left: 0;
                    padding-bottom:0;
                }}
                .reportview-container .main {{
                    background-color:#F8EDF3;}}
                
                </style>"""
                ,
                unsafe_allow_html=True
                )
                st.image("logout.png",width = 1200)
            else:
                st.sidebar.success("Logged In As {}".format(username))
                lg.empty()
                v.empty()
                
                nav = st.sidebar.radio("Navigation",["Home","Health Tracker","BMI Calculator","Sentiment Analysis","Task Manager","Optical Character Recognition","Encryption/Decryption","Play Game","About Us"])
                
                if nav=="About Us":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    About.AboutUs()
                if nav=="BMI Calculator":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    bm.cal()
                
                if nav=="Play Game":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    st.title("GAME:video_game::game_die:")
                    st.image("game.jpg",width = 700)
                    sb=st.selectbox("",["Select a Game","NumberGuessing Game","Rearrange Game"])
                    if sb=="NumberGuessing Game":
                        import game
                        try:
                            if(st.checkbox("End Game!")):
                                st.success("Thanks For Playing! :blush::blush:")
                                st.balloons()
                                st.info("Uncheck the checkbox to play again!")
                            else:
                                st.title("NumberGuessing Game :thought_balloon: :open_mouth:")
                                try:
                                    rinp = int(st.text_input("Guess a number between 1 and 20"))
                                    game.check(rinp)
                                except:
                                    pass
                            
                        except:
                            try:
                                    rinp = int(st.text_input("Guess a number between 1 and 20"))
                                    game.check(rinp)
                            except:
                                    pass
    
                    if sb=="Rearrange Game":
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
                        
                                
                if nav == "Home":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#FDFCA1  ,#FDA1B6, #581845 ); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    Home.home2()
        
                if nav == "Health Tracker":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#FDA1B6, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    ch=st.sidebar.selectbox("Prediction:",['Select the Predictor',"Heart Disease","Diabetes","Covid Risk Detector"])    
                    if ch=="Select the Predictor":
                        st.title("Health Tracker:pill::syringe:")
                        st.image("health.png",width = 700)
                        st.success("<----------- Look at the navbar to select the tracker!")
                    if ch == "Diabetes":
                        diab.dia()
                        
                    if ch == "Heart Disease":
                        h.hd()
                
                    if ch == "Covid Risk Detector":
                        ctracker.ct()
                     
                if nav == "Sentiment Analysis":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    s.hello()
            
                if nav == "Task Manager":
      
                    conn2 = sqlite3.connect('data.db',check_same_thread=False)
                    cn = conn2.cursor()
                    
                    
                    def create2_table():
                    	cn.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE)')
                    
                    
                    def add2_data(task,task_status,task_due_date):
                    	cn.execute('INSERT INTO taskstable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
                    	conn2.commit()
                    
                    
                    def view2_all_data():
                    	cn.execute('SELECT * FROM taskstable')
                    	data = cn.fetchall()
                    	return data
                    
                    def view2_all_task_names():
                    	cn.execute('SELECT DISTINCT task FROM taskstable')
                    	data = cn.fetchall()
                    	return data
                    
                    def get2_task(task):
                    	cn.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
                    	data = cn.fetchall()
                    	return data
                    
                    def get2_task_by_status(task_status):
                        cn.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
                        data = cn.fetchall()
                        return data
                    
                    
                    def edit2_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
                    	cn.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
                    	conn2.commit()
                    	data = cn.fetchall()
                    	return data
                    
                    def delete2_data(task):
                    	cn.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
                    	conn2.commit()
                    
                    st.image("taskmanager.png",width = 700)
                    
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    
                    HTML_BANNER = """
                        <div style="background-color:#900C3F ;padding:10px;border-radius:10px">
                        <h1 style="color:white;font-family: cursive; text-align:center;">Task Manager</h1>
                        </div>
                        """
                    stc.html(HTML_BANNER)
                    menu = ["Create","Read","Update","Delete"]
                    choice = st.sidebar.selectbox("Menu",menu)
                    create2_table()
                    if choice == "Create":
                        st.subheader("Add Item")
                        col1,col2 = st.beta_columns(2)
                        with col1:
                            task = st.text_area("Task To Do")
                        with col2:
                            task_status = st.selectbox("Status",["ToDo","Doing","Done"])
                            task_due_date = st.date_input("Due Date")
                        if st.button("Add Task"):
                            add2_data(task,task_status,task_due_date)
                            st.success("Added ::{} ::To Task".format(task))
                    
                    elif choice == "Read":
                    		
                        with st.beta_expander("View All"):
                            result = view2_all_data()
                            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                            st.dataframe(clean_df) 
                        
                        with st.beta_expander("Task Status"):
                            task_df = clean_df['Status'].value_counts().to_frame()
                            task_df = task_df.reset_index()
                            st.dataframe(task_df)
                       
                    elif choice == "Update":
                        st.subheader("Edit Items")
                        with st.beta_expander("Current Data"):
                            result = view2_all_data()
                            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                            st.dataframe(clean_df)
                        list_of_tasks = [i[0] for i in view2_all_task_names()]
                        selected_task = st.selectbox("Task",list_of_tasks)
                        task_result = get2_task(selected_task)
                        if (task_result):
                            task = task_result[0][0]
                            task_status = task_result[0][1]
                            task_due_date = task_result[0][2]
                            col1,col2 = st.beta_columns(2)
                            with col1:
                                new_task = st.text_area("Task To Do",task)
                            with col2:
                                new_task_status = st.selectbox(task_status,["ToDo","Doing","Done"])
                                new_task_due_date = st.date_input(task_due_date)
                            if st.button("Update Task"):
                                edit2_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
                                st.success("Updated ::{} ::To {}".format(task,new_task))
                            with st.beta_expander("View Updated Data"):
                                result = view2_all_data()
                                clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                                st.dataframe(clean_df)
                    
                    elif choice == "Delete":
                        st.subheader("Delete")
                        with st.beta_expander("View Data"):
                            result = view2_all_data()
                            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                            st.dataframe(clean_df)
                        unique_list = [i[0] for i in view2_all_task_names()]
                        delete_by_task_name =  st.selectbox("Select Task",unique_list)
                        if st.button("Delete"):
                            delete2_data(delete_by_task_name)
                            st.warning("Deleted: '{}'".format(delete_by_task_name))
                        with st.beta_expander("Updated Data"):
                            result = view2_all_data()
                            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                            st.dataframe(clean_df)
                    
                    
                if nav=="Encryption/Decryption":
                    st.markdown(
                        f"""
                        <style>
                        .reportview-container {{
                            background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True)
                    import streamlit as st
                    import random
                    from cryptography.fernet import Fernet
                    from FileEncryption import Encryptor 
                    encryptor=Encryptor()
                    global text
                    mykey=encryptor.key_create()
                    st.title("Encryption/Decryption:lock::key::unlock:")
                    st.image("ende.png",width = 700)
                    newfile = st.text_input("Insert the File Path you want to convert:")
                    ed = st.selectbox("Encrypt or Decrypt Your File:",["Encrypt","Decrypt"])
                    encryptor.key_write(mykey, 'mykey.key')
                    if(ed=="Encrypt"):
                        loaded_key=encryptor.key_load('mykey.key')
                        if(st.checkbox("Encrypt")):
                            val="Download_Encrypted_file"+ str(random.randint(0,10000000))+".txt"
                            encryptor.file_encrypt(loaded_key, newfile, val)
                            
                            def download_link(object_to_download, download_filename, download_link_text):
                                    if isinstance(object_to_download, pd.DataFrame):
                                        object_to_download = object_to_download.to_csv(index=False)
                                
                                    b64 = base64.b64encode(object_to_download.encode()).decode()
                                
                                    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
                                
                            btn=st.button("Download the text")
                            if btn:
                                with open(val,'r') as file:
                                    text = file.read()
                                    st.write("Your Encryption Key is: (Note it down securely for decryption later) Note: Take the value inside the inverted commas: b'key'", loaded_key)
                                    st.success('Done!')
                                    tmp_download_link = download_link(text, val, 'Click here to download your data!')
                                    st.markdown(tmp_download_link, unsafe_allow_html=True)
                            
                    if(ed=="Decrypt"):
                        load_key = st.text_input("Insert the Encryption Key:")
                        ch=st.selectbox("Please enter the destination file type (It should be same as the original file before encryption):",['.pdf',".txt",".pptx",".docx",".csv",".xlsx"]) 
                        if(st.checkbox("Decrypt")):
                            des="Download_Decrypted_File"+str(random.randint(0,10000000))+ch
                            encryptor.file_decrypt(load_key, newfile, des)
                            import requests
                            
                            
    
                            def get_binary_file_downloader_html(bin_file, file_label='File'):
                                with open(bin_file, 'rb') as f:
                                    data = f.read()
                                bin_str = base64.b64encode(data).decode()
                                href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
                                return href
                                
                            btn=st.button("Download")
                            if btn:
                                    st.markdown(get_binary_file_downloader_html(des,ch[1:]), unsafe_allow_html=True)
                
                if nav=="Optical Character Recognition":
                    st.markdown(
                    f"""
                    <style>
                    .reportview-container {{
                        background-image: linear-gradient(#F6C2C2  ,#F6C2F0, #FBFC73); 
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True)
                    st.title(":mag:Optical Character Recognition:mag_right:")
                    st.image("ocr.jpg",width = 700)
                    image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','JPG'])
                    if(st.checkbox("Convert")):
                        try:
                            image = Image.open(image_file)
                            filename = np.array(image)
                            text = pytesseract.image_to_string(filename, config=tessdata_dir_config)
                            st.image(image,width=500,channels='BGR')
                            st.header('Text Output:')
                            st.write(text)
                            my_bar = st.progress(0)
                        
                        
                            f = open('txt', 'w')
                            my_bar.progress(10)
                            f.write(text)
                            my_bar.progress(20)
                            f = open('txt', 'r')
                            my_bar.progress(30)
                            textFile = f.read()
                            my_bar.progress(40)
                            language = 'en'
                            my_bar.progress(50)
                            output = gTTS(text=textFile, lang=language, slow=False)
                            my_bar.progress(60)
                            output.save('output.mp3')
                            my_bar.progress(70)
                            f.close()
                            my_bar.progress(80)
                            audio_file = open('output.mp3', 'rb')
                            my_bar.progress(90)
                            audio_bytes = audio_file.read()
                            my_bar.progress(100)
                            st.audio(audio_bytes, format='audio/mp3')
                            my_bar.empty()
                            
                       
                        
                        

                            def download_link(object_to_download, download_filename, download_link_text):
                                if isinstance(object_to_download, pd.DataFrame):
                                    object_to_download = object_to_download.to_csv(index=False)
                            
                                b64 = base64.b64encode(object_to_download.encode()).decode()
                            
                                return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
                            
                            btn=st.button("Download the text")
                            if btn:
                                st.success('Done!')
                                tmp_download_link = download_link(text, 'Untitled.txt', 'Click here to download your data!')
                                st.markdown(tmp_download_link, unsafe_allow_html=True)
                        
                        except FileNotFoundError:
                            st.error('File not found.')
                            my_bar=st.progress(100)
                            my_bar.empty()
# =============================================================================
#                         except Exception:
#                             st.error('Something went wrong.')
#                             my_bar=st.progress(100)
#                             my_bar.empty()
# =============================================================================
                  
                   
    
        else:
            lgo.empty()
            st.markdown(
                    f"""
                    <style>
                    .reportview-container .main .block-container{{
                        max-width: 1200px;
                        padding-top: 0;
                        padding-right: 0;
                        padding-left: 145px;
                        padding-bottom:0;
                    }}
                    .reportview-container .main {{
                        background-color:#FBC42C;}}
                    </style>
                    """,
                    unsafe_allow_html=True)
            lg.empty()
            v.empty()
            file_ = open("error.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            
            st.markdown(
                f'<img width="1000px" src="data:image/gif;base64,{data_url}" alt="error 404">',
                unsafe_allow_html=True,
            )