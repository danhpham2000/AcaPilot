import streamlit as st


home = st.Page("pages/home.py", title="Home", icon=":material/home:")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:")
history = st.Page("pages/history.py", title="History", icon=":material/history:")

chatbot = st.Page("pages/chatbot.py", title="AcaBot", icon=":material/robot:")
roadmap = st.Page("pages/roadmap.py", title="Roadmap", icon=":material/timeline:")
assigment = st.Page("pages/assignments.py", title="Practice", icon=":material/assignment:")
calendar = st.Page("pages/calendar.py", title="Calendar", icon=":material/event:")




pg = st.navigation({
    "Home": [home],
    "Profile": [dashboard, history, roadmap, assigment, calendar],
    "AcaBot": [chatbot]
})

pg.run()