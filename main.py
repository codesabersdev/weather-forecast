import streamlit as st


st.title("Weather Forecast for the Next Days")

place = st.text_input("City Name")
days = st.slider(label="Days", min_value=1, max_value=5, value=1,
                 help="Select the number of days to see the forecast")
option = st.selectbox('Select the data to show', ('Temperature', 'Sky Conditions'))
st.subheader(f"{option} for next {days} days for {place}")
