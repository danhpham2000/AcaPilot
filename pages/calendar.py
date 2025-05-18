import streamlit as st
from streamlit_calendar import calendar


st.title("Calendar")

calendar_options = {
    "timeZone": 'UTC',
    "initialView": 'dayGridMonth',
    "events": 'https://fullcalendar.io/api/demo-feeds/events.json',
    "editable": True,
    "selectable": True
}


calendar = calendar(
    options=calendar_options,
    key='calendar', # Assign a widget key to prevent state loss
)
