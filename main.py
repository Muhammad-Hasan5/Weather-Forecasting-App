import streamlit as st
import plotly.express as px

st.title("Weather Forecast "
         "For The Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days ",
                 min_value=1,
                 max_value=5,
                 help="Select the number "
                      "of days to be "
                      "forecasted.")

option = st.selectbox("Select the data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for {days} days in {place}")

def get_data(day):
    date = ["2025-17-8", "2025-18-8", "2025-19-8"]
    temp = [10, 11, 15]
    temp = [day * i for i in temp]
    return date, temp

d, t = get_data(days)

figure = px.line(x=d, y=t,
                 labels={"x" : "Date",
                        "y" : "Temperature"})
st.plotly_chart(figure)