import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import sqlite3 
    
    

class Tm():
    
    
    conn2 = sqlite3.connect('data.db',check_same_thread=False)
    cn = conn2.cursor()
    
    
    def create2_table(cn,conn2):
    	cn.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE)')
    
    
    def add2_data(task,task_status,task_due_date,cn,conn2):
    	cn.execute('INSERT INTO taskstable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
    	conn2.commit()
    
    
    def view2_all_data(cn,conn2):
    	cn.execute('SELECT * FROM taskstable')
    	data = cn.fetchall()
    	return data
    
    def view2_all_task_names(cn,conn2):
    	cn.execute('SELECT DISTINCT task FROM taskstable')
    	data = cn.fetchall()
    	return data
    
    def get2_task(task,cn,conn2):
    	cn.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
    	data = cn.fetchall()
    	return data
    
    def get2_task_by_status(task_status,cn,conn2):
        cn.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
        data = cn.fetchall()
        return data
    
    
    def edit2_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date,cn,conn2):
    	cn.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
    	conn2.commit()
    	data = cn.fetchall()
    	return data
    
    def delete2_data(task,cn,conn2):
    	cn.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
    	conn2.commit()
    
    
    HTML_BANNER = """
        <div style="background-color:#eb2d7c;padding:10px;border-radius:10px">
        <h1 style="color:white;font-family: Comic sans; text-align:center;">Task Manager</h1>
        </div>
        """
    stc.html(HTML_BANNER)
    menu = ["Create","Read","Update","Delete"]
    choice = st.sidebar.selectbox("Menu",menu)
    create2_table(cn,conn2)
    if choice == "Create":
        st.subheader("Add Item")
        col1,col2 = st.beta_columns(2)
        with col1:
            task = st.text_area("Task To Do")
        with col2:
            task_status = st.selectbox("Status",["ToDo","Doing","Done"])
            task_due_date = st.date_input("Due Date")
        if st.button("Add Task"):
            add2_data(task,task_status,task_due_date,cn,conn2)
            st.success("Added ::{} ::To Task".format(task))
    
    elif choice == "Read":
    		
        with st.beta_expander("View All"):
            result = view2_all_data(cn,conn2)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df) 
        
        with st.beta_expander("Task Status"):
            task_df = clean_df['Status'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
       
    elif choice == "Update":
        st.subheader("Edit Items")
        with st.beta_expander("Current Data"):
            result = view2_all_data(cn,conn2)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)
        list_of_tasks = [i[0] for i in view2_all_task_names(cn,conn2)]
        selected_task = st.selectbox("Task",list_of_tasks)
        task_result = get2_task(selected_task,cn,conn2)
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
                edit2_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date,cn,conn2)
                st.success("Updated ::{} ::To {}".format(task,new_task))
            with st.beta_expander("View Updated Data"):
                result = view2_all_data(cn,conn2)
                clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                st.dataframe(clean_df)
    
    elif choice == "Delete":
        st.subheader("Delete")
        with st.beta_expander("View Data"):
            result = view2_all_data(cn,conn2)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)
        unique_list = [i[0] for i in view2_all_task_names(cn,conn2)]
        delete_by_task_name =  st.selectbox("Select Task",unique_list)
        if st.button("Delete"):
            delete2_data(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))
        with st.beta_expander("Updated Data"):
            result = view2_all_data(cn,conn2)
            clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
            st.dataframe(clean_df)