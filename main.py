import streamlit as st
import datetime
import pandas as pd
st.set_page_config(page_title="Twitter Scrapper", page_icon=":tada:", layout="wide")

# header sect
st.header("Twitter Scrapping Project")
#st.title("First Twitter Project")

tweet = st.text_input("Enter the Twitter hashtag", "Type Here ...")
nt = st.text_input("Enter the no of Tweets", "Type Here ...")


if (st.button('Submit')):
    result = tweet.title()
    st.success(result)

srt = st.date_input(
    "Enter the Start date of HashTag",
    datetime.date(2021, 1, 1))
ed = st.date_input(
    "Enter the Start date of HashTag",
    datetime.date(2022, 10, 2))

st.write("Your data is range is from ", srt, ed)