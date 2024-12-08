import tweepy
import csv

# Twitter API credentials
API_KEY = '*******************************'
API_SECRET = '*******************************'
ACCESS_TOKEN = '*******************************'
ACCESS_TOKEN_SECRET = '*******************************'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Search for tweets
query = "Uganda"  # Adjust the query as needed
geocode = "1.3733,32.2903,500km"  # Approximate center of Uganda
tweets = tweepy.Cursor(api.search_tweets, q=query, geocode=geocode, lang="en", tweet_mode="extended").items(1000)

# Write to CSV
with open('uganda_tweets.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ID', 'Created At', 'Text', 'User', 'Location', 'Hashtags'])
    for tweet in tweets:
        hashtags = [ht['text'] for ht in tweet.entities['hashtags']]
        csvwriter.writerow([tweet.id, tweet.created_at, tweet.full_text, tweet.user.screen_name, tweet.user.location, ', '.join(hashtags)])

print("Data saved to uganda_tweets.csv")

