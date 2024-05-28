import streamlit as st
import pandas as pd
import numpy as np
import datetime

data_dir = './data/'
daily_num_order_path = data_dir + "Num_order_by_date.csv"
hour_num_order_path = data_dir + "Daily_avg_num_order_by_hour.csv"
loc_num_order_path = data_dir + "daily_num_order_by_pickup_loc.csv"

st.title("2. Explore Number of Rideshare Orders in NYC")
st.markdown("For MSBD5003 Group 9's Course Project")

st.subheader('Number of orders by date')
daily_num_order = pd.read_csv(daily_num_order_path)
daily_num_order = daily_num_order.rename({"count": "Number of orders"}, axis = 'columns')
# convert to date from string
daily_num_order["date"] = pd.to_datetime(daily_num_order["date"]).dt.date


try:
  date_option = st.date_input(
    "Please select the period (YYYY-MM-DD) of data to be visualized. Default is the whole timespan of the data set.",
    (min(daily_num_order["date"]), max(daily_num_order["date"])),
    min_value = min(daily_num_order["date"]),
    max_value = max(daily_num_order["date"]),
    format="YYYY-MM-DD",
  )
  if date_option[0] == date_option[1]:
    st.text('Please choose an end date that is larger than start date.')
  # check if start date < end date
  st.line_chart(data = daily_num_order[(daily_num_order['date']>=date_option[0]) & \
        (daily_num_order['date']<=date_option[1])], x = "date", y = "Number of orders")
except IndexError:
  st.markdown("Please make sure both start and end date have been entered.")


st.subheader('Daily average number of orders by hour')
hour_num_order = pd.read_csv(hour_num_order_path)
hour_num_order = hour_num_order.rename({"avg_count": "Number of orders"}, axis = 'columns')
st.line_chart(data = hour_num_order, x = "hour_of_day", y = "Number of orders")


st.subheader('Daily average number of orders by pickup location')
loc_num_order = pd.read_csv(loc_num_order_path)
loc_num_order = loc_num_order.rename({"avg_count": "Number of orders"}, axis = 'columns')
loc_option = st.selectbox(
    "Please select the borough of data to be visualized. Default is Manhattan",
    tuple(list(loc_num_order['Borough'].drop_duplicates()))
    )

st.bar_chart(loc_num_order[loc_num_order["Borough"] == loc_option],\
             x="Zone", y="Number of orders")
