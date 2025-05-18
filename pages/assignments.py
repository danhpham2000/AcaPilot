import streamlit as st
from vector import storage_context, vector_store
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from schema import *
import os




embed_model = OpenAIEmbedding(model="text-embedding-3-large", api_key=os.getenv("OPENAI_API_KEY"))
model = OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

st.title("Assignments")

points = 0

if "courses" not in st.session_state or not st.session_state.courses:
    st.warning("No courses found. Please add your classes from the Dashboard page.")
else:
    for course in st.session_state.courses:
        st.subheader(course["name"])
        st.write(f"Code: {course['code']}")

        if course["syllabus"]:
            for file in course["files"]:
                quiz_key = f"{course['code']}_{file}_quizzes"
                answer_key = f"{course['code']}_{file}_answers"

                with st.popover("Generate Quiz"):
                    with st.form(f"generate_quiz_{course['code']}_{file}"):
                        num_of_questions = st.text_input("Number of questions:")
                        type_of_questions = st.selectbox(
                                    "What would you like to do?",
                                    ("Multiple choice", "Opened Response"),
                                )
                        submit = st.form_submit_button("Generate Quiz")


                

                if submit or quiz_key in st.session_state:
                    if submit:
                        with st.spinner("Loading quiz..."):
                            documents = SimpleDirectoryReader(input_dir="data", recursive=True).load_data()
                            index = VectorStoreIndex.from_documents(documents=documents,
                                                                    storage_context=storage_context,
                                                                    embed_model=OpenAIEmbedding(model="text-embedding-3-large", api_key=os.getenv("OPENAI_API_KEY")))
                            query_engine = index.as_query_engine(output_cls=ListOfMCQuizzes,
                                                                 response_mode="compact",
                                                                 llm=OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")))
                            data = query_engine.query(
                                f"Provide me {num_of_questions} number of quizzes with software engineer related based on the documents"
                            )
                            st.session_state[quiz_key] = data.response                        

                    # Always render quizzes if stored
                    with st.form(f"Submit quiz form for {course["code"]}"):
                        quizzes = st.session_state[quiz_key]
                        for i, quiz in enumerate(quizzes.questions, start=1):
                            st.write(f"{i}. {quiz.question}")
                            q_key = f"{quiz_key}_answer_{i}"
                            user_answer = st.radio("Your answer", [c.choice for c in quiz.choice], key=q_key, index=None)
                            st.write(f"Selected: {user_answer}")
                            if user_answer == quiz.correct_answer.choice:
                                st.success("You are correct")
                                points += 1
                                st.write(quiz.correct_answer.explanation)
                            if user_answer is not None and user_answer != quiz.correct_answer.choice:
                                st.error("You are not corrected")
                                st.write(quiz.correct_answer.explanation)
                            
                        submit_answers = st.form_submit_button("Submit")
                        if submit_answers:
                            st.form_submit_button("Done")
                            st.write(f"Your score: {points} / {num_of_questions}")


                        
                    
        else:
            st.info("Syllabus not uploaded yet.")





