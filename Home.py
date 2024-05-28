import streamlit as st

st.set_page_config(
    page_title="Exploring Rideshare in New York",
)

st.title("Exploring Rideshare in New York")

st.markdown(
    """
    This Streamlit Web App is the UI of Group 9's MSBD5003 Course Project
    ### Please select the variable you would like to explore (options are also availale on the sidebar):
    - [Average Speed by Hour](/Average_Speed_by_Hour)
    - [Number of Orders](/Number_of_Orders)
    - [Average Waiting Time for Drivers to Pick Up Passengers](/Average_Waiting_Time)
    """
)