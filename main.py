import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider and select-box
st.title("Weather Forecast for the Next Days")
place = st.text_input("City Name")
days = st.slider(label="Days", min_value=1, max_value=5, value=1,
                 help="Select the number of days to see the forecast")
option = st.selectbox('Select the data to show', ('Temperature', 'Sky Conditions'))
st.subheader(f"{option} for next {days} days in {place}")

# if condition to check if the user has given any input
if place:
    # If the city name is misspelled
    try:
        # Get temperature/sky conditions data
        data, dates = get_data(city=place, forecast_days=days, option=option)

        match option:
            case "Temperature":
                figure = px.line(x=dates, y=data, labels={"x": "Dates", "y": "Temperature(c)"})
                st.plotly_chart(figure)
            case "Sky Conditions":
                images = [f"./images/{sky.lower()}.png" for sky in data]
                st.image(images, width=100, caption=dates)
    except KeyError:
        st.warning("City doesn't exist. Check the entered city name!")
