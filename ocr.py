def ocr2():
        import streamlit as st
        import pandas as pd
        import base64
        import pytesseract
        import numpy as np
        from gtts import gTTS
        
        from PIL import Image
        
        pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
        
        #st.header=("Upload Image")
        
        #tempimg = st.file_uploader(type=['png','jpg'])
        
        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','JPG'])
        
        
        if(st.checkbox("Convert")):
            try:
                image = Image.open(image_file)
                filename = np.array(image)
                text = pytesseract.image_to_string(filename)
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
            
            except FileNotFoundError:
                st.error('File not found.')
            except TypeError:
                st.error('File type error.')
        
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

ocr2()