import tweepy
import time
import requests
import schedule

auth = tweepy.OAuthHandler(ACCESS_TOKEN,
                           ACCESS_TOKEN_SECRET)
auth.set_access_token(API_KEY,
                      API_KEY_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def dailyTweet():
    dailyVerseRequest = requests.get(
        'https://labs.bible.org/api/?passage=random&type=json').json()[0]
    dailyVerse = f'{dailyVerseRequest["bookname"]} {dailyVerseRequest["chapter"]}:{dailyVerseRequest["verse"]} | {dailyVerseRequest["text"]}'
    api.update_status(dailyVerse)
    print("Tweet Tweeted!")


schedule.every().day.at("7:00").do(dailyTweet)

while True:
    schedule.run_pending()
    time.sleep(1)
