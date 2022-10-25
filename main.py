import snscrape.modules.twitter as sntwitter
import streamlit as st
import datetime
import pandas as pd
from pymongo import MongoClient
from streamlit_lottie import st_lottie
import lottie as lo
import time


st.set_page_config(page_title="Twitter Scrapper", page_icon=":tada:", layout="wide")

title_container = st.container()
col1, col2 = st.columns([1,20])
with title_container:
    with col1:
        st_lottie(lo.lottie_anim.lottie_coding, height=100)
    with col2:
        st.markdown('<h1 style="color: purple;">Twitter HashTag Scrapper</h1>', unsafe_allow_html=True)

#twitter animation in sidebar
with st.sidebar:
    st_lottie(lo.lottie_anim.lottie_coding1, height=300)

#text box to enter the twitter hashtag
tweet_keyword = st.sidebar.text_input("Enter the Twitter hashtag")
if tweet_keyword == "":
    st.stop()

nt = st.sidebar.number_input('Insert a number of tweets to search', min_value=1, max_value=100000, value = 10, step=1)

# date validation code for start_date and end_date
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.sidebar.date_input('Start date',today)
end_date = st.sidebar.date_input('End date',tomorrow)

if (st.sidebar.button('Submit')):
    #if tweet == "":
        #st.error("Enter the Hastag to search")

    if start_date < end_date:
        #st.sidebar.success('Date Validated')

        #loading animation after Submit Button is pressed
        with st.spinner('Loading..........'):
            time.sleep(5)
        st.success('Data Successfully Extracted!')

        #my_bar = st.sidebar.progress(0)
        #for percent_complete in range(100):
            #time.sleep(0.001)
            #my_bar.progress(percent_complete + 1)

        # Query by text search
        # Setting variables to be used below
        # Creating list to append tweet data to
        tweets_list = []

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'#{tweet_keyword} since:{start_date} until:{end_date}').get_items()):
            if i > nt:
                break
            tweets_list.append([tweet.id,tweet.user.username,tweet.user.followersCount, tweet.content,  tweet.likeCount, tweet.retweetCount, tweet.lang, tweet.replyCount,tweet.date, tweet.url,  tweet.source, tweet.sourceLabel,tweet_keyword])

        # Creating a dataframe from the tweets list above
        tweets_df = pd.DataFrame(tweets_list,columns=['Tweet Id', 'Username', 'Followers Count',  'Content', 'Likes', 'Retweet Count', 'Language', 'Reply Count', 'Date-time',  'URL', 'Source', 'Source Label', 'Keyword'])

        # Display first 5 entries from dataframe
        #tweets_df.head()

        #Display the result in streamlit
        st.write(tweets_df)

        #client = MongoClient("mongodb://localhost:27017/")
        #st.success("Connection Successfull")
        #db = client["Tweet_Scrap"]
        #st.success("Database Created")
        #tweet_db = db["Hash_detail"]
        #st.success("Collection Created")
        #data_dict = tweets_df.to_dict("records")
        #tweet_db.insert_many(data_dict)
        #st.success("Details Uploaded Successfully")

        # Export dataframe into a CSV
        def convert_df(tweets_df):
            return tweets_df.to_csv(index=False).encode('utf-8')
        csv = convert_df(tweets_df)
        tweets_df.to_csv('text-query-tweets.csv', sep=',', index=False)

        # Converts dataframe into a Json
        json_string = tweets_df.to_json(orient='index')
        #json_string = json.dumps(tweets_list,default=str)
        #st.json(json_string, expanded=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button('Upload To Database'):
                # Making a Connection with MongoClient
                client = MongoClient("mongodb://localhost:27017/")
                #client = pymongo.MongoClient('localhost', 27017)

                # database
                db = client["Tweet_Scrap"]
                #db = client.Twitter_Scrap

                # collection
                tweet_db = db["Hash_detail"]
                #tweet_db = db.Hash_detail

                #Converts data frame into dictonary because Mongodb Reads only Dictonary
                data_dict = tweets_df.to_dict("records")

                # Insert collection
                tweet_db.insert_many(data_dict)


        with col2:
            #st.download_button(label="Download JSON File ",file_name="data.json",mime="application/json",data=json_string)
            st.download_button("Download JSON File", json_string, "tweetreport.json", "application/json", key='download-json')

        with col3:
            st.download_button("Download CSV File", csv, "tweetreport.csv", "text/csv", key='download-csv')

    else:
        st.error('Error: End date must fall after start date.')