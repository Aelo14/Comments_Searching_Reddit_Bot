import praw
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt
from slang_ender import find_slang
import pyimgur
from age_prediction import age
from praw.models import Message
# Create a reddit instance
r = praw.Reddit(user_agent = "word_comment_bot",
                  client_id = "24p2oR_Mi0pUBQ",
                  client_secret = "9h4_iggh875nPzkfVtbs7BMUp6A",
                  username = "CH_BOT",
                  password = "jonesbitch")



def comment_word_count(user, keyword):
    """
    :param user: the user we want to investigate
    :param keyword: the word we want to count
    :return: how many times a word has been in the user's comment history
    """
    word_count = 0
    # Create a reddit user instance
    # get all the comment in the redditor's history
    for comment in user.comments.new(limit = None):
        # Split the words in the comment in the
        for word in comment.body.split(' '):
            word.strip(".,-!")
            word.strip("\n")
            if word.lower() == keyword:
                word_count += 1
    return word_count

def word_trend(user):
    word_dict = {}
    # Check the past n comments of the user
    for comment in user.comments.new(limit = None):
        # Make the comment a TextBlob object
        comment = TextBlob(comment.body)
        # print(comment)
        for word, tags in comment.tags:
            # Only put the nouns in the dictionary
            if (tags not in ['NN', 'NNP', 'NNPS']) or (len(word) <= 2):
                continue
            # Checking if the word is already in the dictionary
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 1
            else:
                word_dict[word.lower()] += 1
    return word_dict


#me = r.redditor('aelo14')
#me.message('TEST', 'test message from CH_BOT')


# This function returns the words that repeat the most in a reddit user's comment history
def key_words(user):
    input_dict = word_trend(user)
    str = ""
    # Print out the popular words for my account
    for key, value in input_dict.items():
        if (value > 3) and (find_slang(key, 'slang_dict.txt') == False):
            str += key + " "
            #print(key, value)
    return str


# Create a wordcloud
def create_word_cloud(user):
    wordcloud1 = WordCloud(background_color='white').generate(key_words(user))
    wordcloud1.to_file('wordcloud.png')


def imgur_upload(user):
    CLIENT_ID = "a73085de79cee10"
    create_word_cloud(user)
    PATH = "C:/Users/ouyuj/PycharmProjects/hackrice/wordcloud.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print(user.name)
    print(uploaded_image.link)
    print("-"*20)
    return uploaded_image.link

def message_reply():
    for item in r.inbox.unread():
        item.mark_read()
        if "!CommentHistory" in item.body:
            try:
                item.reply(imgur_upload(r.redditor(item.body.split(' ')[1])))
            except:
                item.reply("Something went wrong...Sorry!")
        elif "!AgePrediction" in item.body:
            try:
                item.reply(age(r.redditor(item.body.split(' ')[1])))
            except:
                item.reply("Something went wrong...Sorry!")

message_reply()
