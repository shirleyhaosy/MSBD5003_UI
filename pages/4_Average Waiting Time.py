import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

data_dir = "./data/"
wait_loc_week_path = data_dir + "avg_waiting_location_name_week.csv"
wait_loc_hour_path = data_dir + "avg_waiting_location_name_hour.csv"
loc_lookup_path = data_dir + "taxi_zone_lookup.csv"


st.title("4. Explore Average Waiting Time of Rideshare Orders in NYC")
st.markdown("""Waiting time is the time difference between driver's 
            and passenger's arrival to pickup location, i.e., time duration 
            that drivers wait for passengers.
        """)

st.subheader(f"Average waiting time at all pickup locations by day in week")
wait_loc_week_df = pd.read_csv(wait_loc_week_path)
st.line_chart(data = wait_loc_week_df, x = "day_of_week_num", y= "all_locations")

st.subheader(f"Average waiting time at all pickup locations by hour in a day")
wait_loc_hour_df = pd.read_csv(wait_loc_hour_path)
st.line_chart(data = wait_loc_hour_df, x = "hour_of_day", y= "all_locations")


## Select locations
## Can select multiple zones in the same borough 
loc_lookup_df = pd.read_csv(loc_lookup_path)
loc_lookup_df = loc_lookup_df.drop(columns = ['service_zone'])

borough_option = st.selectbox(
    "Please select the pickup borough of data to be visualized",
    tuple(list(loc_lookup_df['Borough'].drop_duplicates()))
    )

zone_options = st.multiselect(
    "Please select the pickup location of data to be visualized (multiselect available)",
    list(loc_lookup_df[loc_lookup_df['Borough'] == borough_option]['Zone'].drop_duplicates()))

loc_options = [f"{borough_option}_{z}" for z in zone_options]



st.subheader(f"Average waiting time at pickup location {loc_options} by day in week")
st.line_chart(data = wait_loc_week_df, x = "day_of_week_num", y= loc_options)

st.subheader(f"Average waiting time at pickup location {loc_options} by hour in a day")
st.line_chart(data = wait_loc_hour_df, x = "hour_of_day", y= loc_options)