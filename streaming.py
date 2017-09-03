from tweepy import OAuthHandler
from tweepy import API
import twitter

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = API(auth)
    for item in api.search("python"):
        print("@%s" % item.user.screen_name)
        print(item.text)
        print("-----------")
        print("")