import streamlit as st


st.title("Stimulation exam")
st.subheader("Environment for you to prepare for real-time exam at school or university")

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take Photo", disabled=not enable)

if picture:
    st.button("Setting check")