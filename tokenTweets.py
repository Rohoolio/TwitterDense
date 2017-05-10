import json
import re
import csv
import nltk
import pandas as pd

# The emoticon string to be used in regex expression, this defines the order or characters
# to create the emoticon so it can be registered as 1 whole token.
emoticons_str = r"""
    (?:
       [\>]? #eyebrows
       [:=;8xXB] # Eye notations
       [o0-]? # Noses
       [\\\|/\)\(\]\[pPoODsS3\@$] # Mouths
    )"""

# This is the regex that will search for HTML tags, @-mentions, hashtags, URLS, words with 'and' and utf-8 bytes
# for emoticons
regex_str = [emoticons_str, r"(<[^>]+>)|(?:@[\w_]+)|"
                            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)|"
                            r"(http)[s]?:[/]+.+(?='|\b)|"
                            r"(?:[a-z][a-z'\-_]?|[0-9])+|"
                            r"([\\x][a-z0-9]{3}){1,}"]


# This compiles the regex. It allows for easier readibility using the VERBOSE flag which
# allows the user to have comments within the regex and ignores the case of the letters using the IGNORECASE flag.
tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


# This defines the function tokenise which will execute the regex and return all the tokens created by it from the
# subject text.
def tokenize(s):
    return tokens_re.findall(s)


# This defines the preprocess function which takes in the tokens and makes them uppercase. Then it runs the emoticon
# regex on the tokens. After that is complete it checks if the text is in lowercase and if so it changes the token
# value in the regex to be lowercase and then runs it.
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

# This defines the run process which will take in the tweettext. It will try to create a column to put the processed
# tokens in called val[0] and passes if it it fails.
def run(text):
    try:
        processed = [val[0] for val in tokenize(text.lower())]
    except:
        pass

    #Accesses the index and item within the enumerated processed text and if the item starts with \\
    #the the process opens and finds rhe location of bytes to equal the item and then changes the
    #value to the same rows description. it returns the newly processed token.
    for idx, item in enumerate(processed):
        if item[:1] == "\\":
            try:
                processed[idx] = foo.loc[foo["Bytes"] == item]["Description"].values[0]
            except:
                pass

    return processed

# This function was going to be used to iterate throught he directory and collect all the csv
# files and combine them all into one and then run through tokenizing. However this was not
# in the scope of this project.
""" 
fout = open("combine.csv", "a")
#select first file - this may have to be a manual process
for line in open("data_20170508151443.csv"):
    fout.write(line)
# This range is used to make sure everything from the year 2017 - 2018 is combined to one csv.
for num in range(20170508151654,20180000000000):
    f = open("data_"+str(num)+".csv")
    f.next()
    for line in f:
        fout.write(line)
    f.close()
fout.close()
"""

# This reads in the unicdoe conversion csv using pandas.
foo = pd.read_csv("Unicode_convert.csv")
# This reads in the datafile with the tweets in using pandas.
bar = pd.read_csv("data_20170508151654.csv")

# This is the array tokenized tweets. for every row in the data the tokenized sents will run
# the above functions.
tokenized_sents = []
for row in bar.iterrows():
    tokenized_sents.append(run(row[1]["text"]))

# This will print out the results.
print(tokenized_sents)

# This was a previous attempt at getting the conversion csv to replace the tweet value with the value of the same
# description - this was an overthought process but was kept in just to show the working done to get to the correct
# solution, or at least one that works at a basic level.
"""
desc = []
bytes = []
ctext = []

with open('data_20170508151654.csv', 'r') as f, open('Unicode_convert.csv', 'r', ) as convert:
    reader = csv.reader(f, delimiter=',')
    reader2 = csv.reader(convert, delimiter=',')
    next(convert)
    for row in reader2:
        bytes.append(row[1])
        desc.append(row[2])
    #print(bytes)
    #print(desc)
    next(f)
    for row in reader:
        ctext.append(row[1])
        tokenized_sents = [preprocess(i) for i in ctext]
        #for i in tokenized_sents:
        #    print(i)
print(tokenized_sents)
"""

# This piece of code was the initial tokenising code that did not take into account the fact that emoticons
# would come out in utf-8 bytes and so was not used in the final release.
"""
ctext = []
with open('data_20170508151654.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ctext.append(row[1])
        tokenized_sents = [preprocess(i) for i in ctext]
        for i in tokenized_sents:
            print(i)
"""
