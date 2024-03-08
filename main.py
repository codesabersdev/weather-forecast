import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")

place = st.text_input("City Name")
days = st.slider(label="Days", min_value=1, max_value=5, value=1,
                 help="Select the number of days to see the forecast")
option = st.selectbox('Select the data to show', ('Temperature', 'Sky Conditions'))
st.subheader(f"{option} for next {days} days for {place}")


def get_data(slider_days):
    dates = ["2024-03-01", "2024-03-02", "2024-03-03"]
    temperature = [10, 20, 5]
    temperature = [slider_days * temp for temp in temperature]
    return dates, temperature


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature(c)"})
st.plotly_chart(figure)
