import streamlit as st
import datetime
import pandas as pd
st.set_page_config(page_title="Twitter Scrapper", page_icon=":tada:", layout="centered")

# header sect
st.header("Twitter Scrapping Project")
#st.title("First Twitter Project")

tweet = st.text_input("Enter the Twitter hashtag",)
if tweet == "":
    st.stop()
nt = st.number_input('Insert a number of tweets to search', min_value=1, max_value=100000, value = 1, step=1)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date',today)
end_date = st.date_input('End date',tomorrow)

if (st.button('Submit')):
    if start_date < end_date:
        st.success('Date Validated')
    else:
        st.error('Error: End date must fall after start date.')
