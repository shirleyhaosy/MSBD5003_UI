import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

data_dir = './data/'
avg_speed_by_date_hour_path = data_dir + "average_speed_by_date_hour.csv"
avg_speed_by_loc_path = data_dir + "average_speed_by_location.csv"
loc_lookup_path = data_dir + "taxi_zone_lookup.csv"

start_date = datetime.strptime("01/01/2022", '%d/%m/%Y').date()
end_date = datetime.strptime("31/08/2023", '%d/%m/%Y').date()

st.title("1. Explore Average Speed of Rideshare Orders in NYC")
st.markdown("For MSBD5003 Group 9's Course Project")

###########################################
##Average speed by hour on a certain date##
###########################################
st.subheader('Average speed by hour on a certain date')

avg_speed_by_date_hour_df = pd.read_csv(avg_speed_by_date_hour_path)
avg_speed_by_date_hour_df = avg_speed_by_date_hour_df.rename(\
                            {"avg(average_speed)": "Average speed"}, axis = 'columns')
# string to date
avg_speed_by_date_hour_df["date"] = pd.to_datetime(avg_speed_by_date_hour_df["date"]).dt.date
avg_speed_by_date_hour_df = avg_speed_by_date_hour_df[(avg_speed_by_date_hour_df['date']>= start_date) &
                                                    (avg_speed_by_date_hour_df['date']<= end_date)]

date_option = st.date_input(
    f"Please select the date (YYYY-MM-DD) of data to be visualized. Available timespan is from {start_date} to {end_date}.",
    min_value = start_date,
    max_value = end_date,
    format="YYYY-MM-DD",
)
st.markdown(f"Average speed by hour on {date_option}")
st.line_chart(data = avg_speed_by_date_hour_df[avg_speed_by_date_hour_df['date'] == date_option], \
                    x = "hour_of_day", y = "Average speed")

##########################################################################
##Average speed by hour of a certain pair of pickup and dropoff location##
##########################################################################
st.subheader('Average speed by hour of a certain pair of pickup and dropoff location')
st.markdown("Please note that Zone is under Borough.")

loc_lookup_df = pd.read_csv(loc_lookup_path)
# drop unused column
loc_lookup_df = loc_lookup_df.drop(columns = ['service_zone'])

avg_speed_by_loc_df = pd.read_csv(avg_speed_by_loc_path)
avg_speed_by_loc_df = avg_speed_by_loc_df.rename(\
                            {"avg(average_speed)": "Average speed"}, axis = 'columns')

avg_speed_by_loc_df = pd.merge(avg_speed_by_loc_df, loc_lookup_df, left_on=  ["pickup_location"],
                   right_on= ["LocationID"], 
                   how = 'left')
avg_speed_by_loc_df = pd.merge(avg_speed_by_loc_df, loc_lookup_df, left_on=  ["dropoff_location"],
                   right_on= ["LocationID"], 
                   how = 'left', suffixes=("_pickup", "_dropoff"))

pickup_borough_option = st.selectbox(
    "Please select the pickup borough of data to be visualized",
    tuple(list(avg_speed_by_loc_df['Borough_pickup'].drop_duplicates()))
    )
dropoff_borough_option = st.selectbox(
    "Please select the pickup borough of data to be visualized",
    tuple(list(avg_speed_by_loc_df['Borough_dropoff'].drop_duplicates()))
    )

borough_data = avg_speed_by_loc_df[(avg_speed_by_loc_df['Borough_pickup'] == pickup_borough_option) \
                                & (avg_speed_by_loc_df['Borough_dropoff'] == dropoff_borough_option)]

pickup_loc_option = st.selectbox(
    "Please select the pickup location of data to be visualized",
    tuple(list(borough_data['Zone_pickup'].drop_duplicates()))
    )

dropoff_loc_option = st.selectbox(
    "Please select the dropoff location of data to be visualized",
    tuple(list(borough_data['Zone_dropoff'].drop_duplicates()))
    )

loc_data = borough_data[(borough_data['Zone_pickup'] == pickup_loc_option) \
                                & (borough_data['Zone_dropoff'] == dropoff_loc_option)]

st.markdown(f"Average speed by hour of trips from {pickup_loc_option} to {dropoff_loc_option}")
st.line_chart(data = loc_data, x = "hour_of_day", y = "Average speed")
