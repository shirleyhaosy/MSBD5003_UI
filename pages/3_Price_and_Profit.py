import streamlit as st
import pandas as pd
import numpy as nps
import datetime

data_dir = "./data/"
price_by_hour_path = data_dir + "PriceByHour.csv"
price_by_time_path = data_dir + "PriceByTime.csv"
price_by_loc_path = data_dir + "PriceInAreas.csv"
profit_by_hour_path = data_dir + "ProfitByHour.csv"
profit_by_time_path = data_dir + "ProfitByTime.csv"
loc_lookup_path_path = data_dir + "taxi_zone_lookup.csv"

st.title("3. Explore Price and Profit of Rideshare Orders in NYC")
st.markdown("For MSBD5003 Group 9's Course Project")

st.subheader("Average price of order by hour")
price_by_hour_df = pd.read_csv(price_by_hour_path)
price_by_hour_df = price_by_hour_df.rename({"average_price": "Average price"}, axis = 'columns')
st.line_chart(data = price_by_hour_df, x = "hour_of_day", y = "Average price")


st.subheader("Average price of order by date")
price_by_time_df = pd.read_csv(price_by_time_path)
price_by_time_df["date"] = pd.to_datetime(price_by_time_df["date"]).dt.date
price_by_time_df = price_by_time_df.rename({"average_price": "Average price"}, axis = 'columns')

try:
    price_date_option = st.date_input(
    "Please select the period (YYYY-MM-DD) of data to be visualized. Default is the whole timespan of the data set.",
    (min(price_by_time_df["date"]), max(price_by_time_df["date"])),
    min_value = min(price_by_time_df["date"]),
    max_value = max(price_by_time_df["date"]),
    format="YYYY-MM-DD",
    )
    if price_date_option[0] == price_date_option[1]:
        st.text('Please choose an end date that is larger than start date.')
    # check if start date < end date
    st.line_chart(data = price_by_time_df[(price_by_time_df['date']>=price_date_option[0]) & \
            (price_by_time_df['date']<=price_date_option[1])], x = "date", y = "Average price")
except IndexError:
  st.markdown("Please make sure both start and end date have been entered.")

st.subheader("Average price of order by pickup location")
price_by_time_df = pd.read_csv(price_by_time_path)
price_by_time_df["date"] = pd.to_datetime(price_by_time_df["date"]).dt.date

price_by_loc_df = pd.read_csv(price_by_loc_path)
price_by_loc_df = price_by_loc_df.rename({"average_price": "Average price"}, axis = 'columns')

loc_option = st.selectbox(
    "Please select the borough of data to be visualized. Default is Manhattan.",
    tuple(list(price_by_loc_df['Borough'].drop_duplicates()))
    )

st.bar_chart(price_by_loc_df[price_by_loc_df["Borough"] == loc_option],\
             x="Zone", y="Average price")



st.subheader("Average profit of order by hour")
profit_by_hour_df = pd.read_csv(profit_by_hour_path)
profit_by_hour_df = profit_by_hour_df.rename({"average_profit": "Average profit"}, axis = 'columns')
st.line_chart(data = profit_by_hour_df, x = "hour_of_day", y = "Average profit")


st.subheader("Average profit of order by date")
profit_by_time_df = pd.read_csv(profit_by_time_path)
profit_by_time_df["date"] = pd.to_datetime(profit_by_time_df["date"]).dt.date
profit_by_time_df = profit_by_time_df.rename({"average_profit": "Average profit"}, axis = 'columns')

try:
    profit_date_option = st.date_input(
    "Please select the period (YYYY-MM-DD) of data to be visualized. Default is the whole timespan of the data set.",
    (min(profit_by_time_df["date"]), max(profit_by_time_df["date"])),
    min_value = min(profit_by_time_df["date"]),
    max_value = max(profit_by_time_df["date"]),
    format="YYYY-MM-DD",
    key = 1,
    )
    if profit_date_option[0] == profit_date_option[1]:
        st.markdown('Please choose an end date that is larger than start date.')
    # check if start date < end date
    st.line_chart(data = profit_by_time_df[(profit_by_time_df['date']>=profit_date_option[0]) & \
            (profit_by_time_df['date']<=profit_date_option[1])], x = "date", y = "Average profit")
except IndexError:
  st.markdown("Please make sure both start and end date have been entered.")