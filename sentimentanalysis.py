
def hello():
    from textblob import TextBlob
    import webbrowser
    import time
    import streamlit as st
    
    
    
    st.title(":two_hearts::grin:Sentiment Analysis:grin::two_hearts:")
    c1, c2, c3 = st.beta_columns((2, 6, 1))
    with c2:
      st.image("Sentiment.png",width =300)
    st.header("Let us check your mood today!:sweat_smile:")
    
    arr=[]
    a=st.selectbox('How do you feel?',['Excellent','Good','Bad','Bored','Tired','Nothing'])
    b=st.selectbox('Did your day till now go well?',['Good','Bad','Dont Know','Boring'])
    c=st.text_input('Want to say something to me?\n')
    
    x=TextBlob(a).sentiment.polarity
    y=TextBlob(b).sentiment.polarity
    z=TextBlob(c).sentiment.polarity
    
    arr.append(x)
    arr.append(y)
    arr.append(z)
    
    
    n=0
    h=0
    s=0
    for i in range(0,3,1):
        if(arr[i]==0):
            n+=1
        if(arr[i]>0 and arr[i]<=1):
            h+=1
        if(arr[i]<0):
            s+=1
    new=[n,h,s]
    l=max(new)
    
    if(st.button("Check Me!")):
        if(n==h and n==s):
            st.warning(":confused: It was really a confusing day it seems. Lets do something interesting to make it thrilling. Wanna listen to songs? :wink:")
            time.sleep(5)
            webbrowser.open("https://www.youtube.com/results?search_query=recent+songs")
        elif(l==n):
            st.info(":sleeping: :expressionless:It is really a monotonous day today! Feels like you are in no mood to do anything. So, you can watch some movies:popcorn::cinema: or just read out good books:books:")
            time.sleep(5)
            webbrowser.open("https://www.hotstar.com/in/movies")
            webbrowser.open("https://www.google.com/search?q=good+ebooks+to+read&oq=good+ebooks+to+read&aqs=chrome..69i57j0i10i433j0i10l8.5761j0j7&sourceid=chrome&ie=UTF-8")
        elif(l==h): 
            st.success(":blush::heart_eyes:You seem really happy today! Good. That seems great! Wish you have a wonderful day ahead!:relieved::sunglasses::heart: Go:dancer:, run:woman-running::man-running:, have some food :hamburger::poultry_leg::cake::yum:! Enjoy!:tada:")
        elif(l==s):
            st.success(":persevere::sob:Please dont be sad today! Okay Let's do something to uplift your mood:scream:. Watch some funny videos on youtube:joy:")
            time.sleep(5)
            webbrowser.open("https://www.youtube.com/results?search_query=funny+videos+cartoon+disney")
