import streamlit as st
import plotly.express as px
from backend import get_data

# add widgets
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

if place:
    # get the temp/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        # plot the temperature
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures,
                     labels={"x" : "Date",
                            "y" : "Temperature"})
        st.plotly_chart(figure)

    if option == "Sky":
        # inserting sky images
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        sky_and_img = {"Clear" : "weather_images/clear.png", "Clouds" : "weather_images/cloud.png",
                       "Snow" : "weather_images/snow.png", "Rain" : "weather_images/rain.png"}
        img_paths = [sky_and_img[condition] for condition in sky_conditions]
        st.image(img_paths, width=115)



