import streamlit as st

st.title("Weather Forecast "
         "For The Next Days")

place = st.text_input("Place: ")

days = st.slider("Days ",
                 min_value=1,
                 max_value=5,
                 help="Select the number "
                      "of days to be "
                      "forecasted.")

option = st.selectbox("Select the data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for {days} days in {place}")
