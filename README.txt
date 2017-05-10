------------------
Assignment 2 - Twitter stream recorder with emoticon tokenizer
Assignment 2 Python 1.0 08 May 2017

------------------
License Information
------------------
Copyright (c) School of Geography.
University of Leeds, Leeds, West Yorkshire, UK. LS2 9JT.
All rights reserved.
This code is under the Common Development and Distribution License (CDDL-1.0).
For details, please see the https://opensource.org/licenses/CDDL-1.0

-------------------
Contact
-------------------
Author = Rowan Gill
Email = ee11rg@leeds.ac.uk

------------------
Basic Information
------------------
This project was aimed at connecting to the Twitter API and streaming services to catch live tweets of any topic the user wants. This will
be saved into a cvs file with the name data_(year/month/day/hour/minute/second) so that no two files are ever the same, the format will be 
screen_name - text(tweet) - Coordinates(if available). This does this by defining a counter to record the number of tweets to a certain point 
defined by the user and creates the csv to record the data with designated column names. Then whenever a tweet is posted that contains the 
words being searched for the code will open the file and write the tweet inside - it will continue to do this until the maximum tweets is met.

The tokeniser then runs through the text column and creates tokens of all the words, hashtags, hyperlinks and emoticons. It runs through all the
rows doing this and then runs a conversion for the emoticons as they will be created as utf-8 byte characters and therefore unreadable. To do this
a conversion csv was made and the code will run through and replace all of the utf-8 emoticon code with a literal string of its meaning.

---------------------
Instructions For Use
---------------------
Stream Grabber
**************

To use the code the user must first obtain their own twitter access token and secret and consumer key and secret in order to connect to the twitter
stream. This can be done by registering an app onto the twitterapps page and they will send you these to use. Once you have these place them in the 
areas designated at the top of the onlineTweep python file. 

The next step is to define how many tweets you want stored per run of the code, by default it will say self.m = 30 which stops at 30 tweets as it 
was used to test the functions of the code. I am not sure of the maximum amount that TweePy can record from the free Twitter stream access so it is 
up to the user to define this number.

The user then needs to only input what words they are going to be searching twitter for in the:

				TweetStream.filter(track=[''])

This is what the code will be looking for in twitter posts and when it finds it will record it in the csv, simply put your terms inbetween the ''
and fire up the code.


Tokenizer
*********

To tokenise the tweets the user needs to define the file they want to tokenise within the:

				bar = pd.read_csv("data_()")
				
This function was going to an iterator through the directory but that was not completed in this time frame so at the moment the user will need to 
hardcode the file name they want to tokenise.



------------------
GitHub
------------------
If you want to see the whole code then go to:

https://github.com//Rohoolio/TwitterDense

------------------
Dependencies
------------------
This project was dependent on certain python libraries such as:

Pandas- http://pandas.pydata.org/
Tweepy - https://github.com/tweepy/tweepy
NLTK - http://www.nltk.org/
