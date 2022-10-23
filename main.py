import snscrape.modules.twitter as sntwitter
import streamlit as st
import datetime
import pandas as pd
import os

st.set_page_config(page_title="Twitter Scrapper", page_icon=":tada:", layout="wide")
st.header("Twitter Scrapper")

# header sect
#st.sidebar.subheader("ENTER THE DETAILS HERE")
tweet = st.sidebar.text_input("Enter the Twitter hashtag")
if tweet == "":
    st.stop()
nt = st.sidebar.number_input('Insert a number of tweets to search', min_value=1, max_value=100000, value = 1, step=1)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.sidebar.date_input('Start date',today)
end_date = st.sidebar.date_input('End date',tomorrow)

if (st.sidebar.button('Submit')):
    if tweet == "":
        st.error("Enter the Hastag to search")
    if start_date < end_date:
        st.sidebar.success('Date Validated')
        # Query by text search
        # Setting variables to be used below
        # Creating list to append tweet data to
        tweets_list2 = []

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i, tweet in enumerate(
                sntwitter.TwitterSearchScraper(f'#{tweet} since:{start_date} until:{end_date}').get_items()):
            if i > nt:
                break
            #tweets_list2.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.user.followersCount, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.likeCount, tweet.source])
            tweets_list2.append([ tweet.id,tweet.user.username,tweet.user.followersCount, tweet.content,  tweet.likeCount, tweet.retweetCount, tweet.lang, tweet.replyCount,tweet.date, tweet.url,  tweet.source])

        # Creating a dataframe from the tweets list above
        #tweets_df2 = pd.DataFrame(tweets_list2, columns=['Date-time', 'Tweet Id', 'URL', 'Content', 'Username', 'Followers Count', 'Reply Count', 'Retweet Count', 'Language', 'Likes', 'Source'])
        tweets_df2 = pd.DataFrame(tweets_list2,columns=['Tweet Id', 'Username', 'Followers Count',  'Content', 'Likes', 'Retweet Count', 'Language', 'Reply Count', 'Date-time',  'URL', 'Source'])
        # Display first 5 entries from dataframe
        tweets_df2.head()

        # Export dataframe into a CSV
        tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=False)
        st.write(tweets_df2)
        def convert_df(tweets_df2):
            return tweets_df2.to_csv(index=False).encode('utf-8')

        csv = convert_df(tweets_df2)

        st.download_button(
            "Download CSV File",
            csv,
            "tweetreport.csv",
            "text/csv",
            key='download-csv'
        )

        st.write(tweets_list2)
        st.write("Success in Reading Tweets!!!!")
    else:
        st.error('Error: End date must fall after start date.')