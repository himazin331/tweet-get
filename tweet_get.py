import config
import tweepy

import matplotlib.pyplot as plt
from PIL import Image
import io
import requests

# API Key & Access Token
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# Twitter API Authentication
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

user_id = input("User ID : ")
print("")

try:
    # Get tweets from a user's timeline
    for status in api.user_timeline(id=user_id):

        print("User Name : ", status.user.name)
        print("Tweet : ", status.text)
        print("Image : ", end="")
        try:
            # If the tweet contains an image
            for i in range(len(status.extended_entities['media'])):
                url = status.extended_entities['media'][i]['media_url']
                image = Image.open(io.BytesIO(requests.get(url).content))

                plt.axis("off")
                plt.imshow(image)
                plt.show()

        except AttributeError:
            # If the tweet not contains an image
            print("None")

    print("--------------------------")

except tweepy.TweepError as e:

    print("Error Code: {}".format(e.args[0][0]['code']))
    print(e.args[0][0]['message'])