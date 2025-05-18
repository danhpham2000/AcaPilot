import streamlit as st


st.title("Assignments")

if "courses" not in st.session_state or not st.session_state.courses:
    st.warning("No courses found. Please add your classes from the Dashboard page.")
else:
    for course in st.session_state.courses:
        st.subheader(course["name"])
        st.write(f"Code: {course['code']}")
        if course["syllabus"]:
            st.success("Syllabus uploaded and processed.")
            for file in course["files"]:
                with st.form("Generate Quiz"):
                    st.write(file)
                    st.form_submit_button("Generate Quiz")
        else:
            st.info("Syllabus not uploaded yet.")








