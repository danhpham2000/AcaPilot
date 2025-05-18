import streamlit as st


home = st.Page("pages/home.py", title="Home", icon=":material/home:")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:")
history = st.Page("pages/history.py", title="History", icon=":material/history:")

chatbot = st.Page("pages/chatbot.py", title="AcaBot", icon=":material/robot:")
roadmap = st.Page("pages/roadmap.py", title="Roadmap", icon=":material/timeline:")
assigment = st.Page("pages/assignments.py", title="Practice", icon=":material/assignment:")
calendar = st.Page("pages/calendar.py", title="Calendar", icon=":material/event:")
profile = st.Page("pages/profile.py", title="Profile", icon=":material/person:")
exam_space = st.Page("pages/exam_space.py", title="Stimulation Exam", icon=":material/video_call:")




pg = st.navigation({
    "Home": [home, profile],
    "Workspace": [dashboard, history, roadmap, assigment, calendar, exam_space],
    "AcaBot": [chatbot]
})

pg.run()