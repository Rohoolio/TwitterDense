"""
 * onlineTweep 1.0 10 May 2017
 *
 * Copyright (c) School of Geography.
 * University of Leeds, Leeds, West Yorkshire, UK. LS2 9JT.
 * All rights reserved.
 *
 * This code is under the Attribution 4.0 International CC BY 4.0 License.
 * For details, please see the https://creativecommons.org/licenses/by/4.0/legalcode.
"""


import sys
import tweepy
import csv
import time
import pandas as pd
import numpy as np

# These are the custom access and consumer codes that allows access to
# the twitter stream and process the data obtained.
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


# This authorises the user using the access and consumer details with tweepy so
# that it can access the data and use its API.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# This is the stream listener that connects to twitter, this is where the original
# twitter API is overridden so that we can manipulate the data to our needs.
class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api
        # This starts a self timer at 0, this will be used to count the number of tweets collected.
        self.n = 0
        # This will be the number of tweets that the streamer will collect before it stops collecting.
        self.m = 30

        # Create a file with 'data_' and the current time
        self.filename = 'data' + '_' + time.strftime('%Y%m%d%H%M%S') + '.csv'
        # Create a new file with that filename
        csvFile = open(self.filename, 'w')

        # Create a csv writer
        # Line terminator prevents the program adding unwanted extra lines that can upset later functions.
        csvWriter = csv.writer(csvFile, lineterminator = '\n')

        # Write a single row with the headers of the columns
        csvWriter.writerow(['user.screen_name',
                            'text',
                            'coordinates'])


    # This changes the on_data method of a stream listener which receives all messages and calls functions according to the message type
    # def on_data(self, data):
    #   all_data = json.loads(data)

    #    with open('Tweets.txt', 'a', encoding='utf-8') as f:
    #        f.write(data)
    #        self.n = self.n + 1
    #        if self.n < self.m:
    #            print('tweets = ' + str(self.n))
    #            return True
    #        else:
    #           print('finished')
    #           return False

    # When a tweet appears.
    def on_status(self, status):

        # Open the csv file created previously.
        csvFile = open(self.filename, 'a')

        # Create a csv writer.
        # Line terminator will prevent a new line from being added every time.
        csvWriter = csv.writer(csvFile, lineterminator='\n')

        # If the tweet is not a retweet.
        if not 'RT @' in status.text:
            # Try to
            try:
                # This counts up the counter by 1 each tweet.
                self.n = self.n + 1
                # If the tweet count is still below the maximum then continue and print tweets.
                if self.n < self.m:
                    print('tweets = ' + str(self.n))
                    # Write the tweet's information to the csv file.
                    csvWriter.writerow([status.user.screen_name,
                                        status.text.encode('utf-8'),
                                        status.coordinates])

                else:
                    print('finished')
                    return False
            # If some error occurs.
            except Exception as e:
                # Print the error.
                print(e)
                # and continue.
                pass

        # Close the csv file.
        csvFile.close()

        # Return nothing.
        return

    # This changes the on_status class - when the twitter user posts a
    # status related to the filters assigned this will catch it.
    """
    def on_status(self, status):
        with open('Tweets.txt', 'a', encoding='utf-8', newline='') as f:
            if not 'RT @'in status.text:
                try:
                    f.writerow([status.screen_name, status.text, status.coordinates])
                    self.n = self.n + 1
                    if self.n < self.m:
                        print('tweets = ' + str(self.n))
                        return True
                    else:
                        print('finished')
                        return False
                except Exception as e:
                    # Print the error
                    print(e)
    """


    # When the stream encounters an error of any kind this will print it out and
    # keep the stream running.
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

    # If the stream times out then this method will post a message and keep running
    # the stream.
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True


# This defines the stream using the authorization settings and the stream listener.
TweetStream = tweepy.streaming.Stream(auth, CustomStreamListener())

# This is the filter for the stream, all the buzzwords and markers the user wants to
# catch in statuses are put into here.
TweetStream.filter(track=['chicken'])
