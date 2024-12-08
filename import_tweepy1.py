import tweepy
import json

# Twitter API credentials
API_KEY = "Q8aSWFCNgWiwkz8TX6OlUC0yb"
API_SECRET = "lK5dZ72vMakcKK8qygDbuK1xPtPHoLk75rrEYXJebe6DPAYMeN" 
ACCESS_TOKEN = "1864648166378745856-BVELX2VF1m7db7JnEOEvxcnKlll4JD"
ACCESS_TOKEN_SECRET = "UavrCChQPEm3GGvyiF17iTqZrBHSPWw4JqkU0PCH4oAuA"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Fetch tweets from a specific user timeline
def fetch_user_tweets(username, max_tweets=100):
    try:
        tweets = api.user_timeline(screen_name=username, count=max_tweets, tweet_mode="extended")
        return [{"id": tweet.id_str, "text": tweet.full_text, "timestamp": str(tweet.created_at)} for tweet in tweets]
    except tweepy.errors.TweepyException as e:
        print(f"Error: {e}")
        return []

# Save tweets to JSON
def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_csv(data, filename):
    """
    Save data to a CSV file
    """
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "user", "text", "timestamp"])
        writer.writeheader()
        writer.writerows(data)


# Example usage
username = "BBCWorld"
tweets = fetch_user_tweets(username)
save_to_json(tweets, "user_tweets.json")
save_csv(tweets, "uganda_tweets.csv")
print("Tweets saved to user_tweets.json")
