# imports needed for bot
import tweepy
import time
import requests
import schedule

# setting up authentication with twitter API
auth = tweepy.OAuthHandler(ACCESS_TOKEN,
                           ACCESS_TOKEN_SECRET)
auth.set_access_token(API_KEY,
                      API_KEY_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# function for getting data and making twitter tweet


def dailyTweet():
    dailyVerseRequest = requests.get(
        'https://labs.bible.org/api/?passage=votd&type=json').json()[0]
    dailyVerse = f'{dailyVerseRequest["bookname"]} {dailyVerseRequest["chapter"]}:{dailyVerseRequest["verse"]} | {dailyVerseRequest["text"]}'
    api.update_status(dailyVerse)
    print("Tweet Tweeted!")


# function to follow back users that follow bot
def follow():
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            follower.follow()

# function to run functions


def bot_functions():
    dailyTweet()
    follow()


schedule.every().day.at("07:30").do(bot_functions)

while True:
    schedule.run_pending()
    time.sleep(1)
