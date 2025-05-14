import streamlit as st
from ai.vector import get_index
import datetime
from random import randint


spring_semester_begin = datetime.date(datetime.datetime.now().year, 1, 1)
spring_semester_end = datetime.date(datetime.datetime.now().year, 5, 30)



st.title("Dashboard")
st.write("Spring Semester " + str(datetime.datetime.now().year))




if "courses" not in st.session_state:
    st.session_state.courses = []

with st.form("Add your current classes"):
    course_name = st.text_input("Class name")
    course_code = st.text_input("Class code")
    submit = st.form_submit_button("Add class")
    

   

if submit:
    if not course_name or not course_code:
        st.warning("Please fill your course name and course code")
        st.stop()
    
    for current_course in st.session_state.courses:
        if course_name in current_course["name"] or course_code in current_course["code"]:
            st.warning(f"{course_name} already in your dashboard")
        
    st.session_state.courses.append({"name": course_name, "code": course_code, "syllabus": False})



for course in st.session_state.courses:
    st.write(course["name"])
    st.write(course["code"])
    if course["syllabus"] == False:
        file = st.file_uploader("Upload your syllabus", key=f"${randint(1, 20)}")
        print(file=file)
        if file is not None:
            # Save uploaded file temporarily
            file_path = f"./{course['code']}.pdf"
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())

            # Call your function to process it
            with st.spinner("Extracting information..."):
                result = get_index(file_path)

            # Update state
            st.write(result)
            st.success("Syllabus processed successfully!")
        



    

    


