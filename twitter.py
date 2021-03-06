import tweepy


auth = tweepy.OAuthHandler(ACCESS_TOKEN,
                           ACCESS_TOKEN_SECRET)
auth.set_access_token(API_KEY,
                      API_KEY_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
