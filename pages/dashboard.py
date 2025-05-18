import streamlit as st
import datetime
import os
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from vector import storage_context, vector_store
from schema import *

spring_semester_begin = datetime.date(datetime.datetime.now().year, 1, 1)
spring_semester_end = datetime.date(datetime.datetime.now().year, 5, 30)


embed_model = OpenAIEmbedding(model="text-embedding-3-large", api_key=os.getenv("OPENAI_API_KEY"))
model = OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))



st.title("Dashboard")
st.write("Spring Semester " + str(datetime.datetime.now().year))



if "courses" not in st.session_state:
    st.session_state.courses = []

if "resources" not in st.session_state:
    st.session_state.resources = []


if "roadmap" not in st.session_state:
    st.session_state.roadmap = []


with st.popover("Add your class"):
    with st.form("Add your current classes"):
        course_name = st.text_input("Class name")
        course_code = st.text_input("Class code")
        submit = st.form_submit_button("Add class")

    
st.markdown("<br/>", unsafe_allow_html=True)   

if submit:
    if not course_name or not course_code:
        st.warning("Please fill your course name and course code")
        st.stop()
    
    for current_course in st.session_state.courses:
        if course_name in current_course["name"] or course_code in current_course["code"]:
            st.warning(f"{course_name} already in your dashboard")
            st.session_state.courses.remove({"name": course_name, "code": course_code, "syllabus": False, "files": []})

        
    st.session_state.courses.append({"name": course_name, "code": course_code, "syllabus": False, "files": []})

count = 0

for course in st.session_state.courses:
    st.write(course["name"])
    st.write(course["code"])
    file = st.file_uploader("Upload your syllabus", key=f"{course['code'] + str(count)}_syllabus")
    count += 1
    
    if file is not None:
        with open(os.path.join("data", file.name), "wb") as f:
            f.write(file.getbuffer())

        course["syllabus"] = True
        course["files"].append(file.name)


        with st.spinner(text="Extracting data from the syllabus"):
            documents = SimpleDirectoryReader(input_dir=f"data", recursive=True).load_data()
            index = VectorStoreIndex.from_documents(documents=documents,
                                                    storage_context=storage_context,
                                                    embed_model=embed_model)
            
            query_engine_1 = index.as_query_engine(output_cls=ClassInfo, response_mode="compact",
                                                 llm=model)
            assignment = query_engine_1.query("You should extract ALL everything important number of assignments, number of exams, " \
            "any projects, along with all the gradings of  " \
            "exams from the ACCT_100 syllabus along with their date and timeframe")

            query_engine_2 = index.as_query_engine(output_cls=Roadmap, response_mode="compact",
                                                 llm=model)
            roadmap = query_engine_2.query("You should give the students tips and external resources" \
            "on how to master this class and get good grades")

            st.session_state.resources.append(assignment.response)
            st.session_state.roadmap.append(roadmap.response)
            


                
        
        



    

    


