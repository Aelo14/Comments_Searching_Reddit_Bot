import praw,requests
from bs4 import BeautifulSoup

# Create a reddit instance
r = praw.Reddit(user_agent = "word_comment_bot",
                  client_id = "24p2oR_Mi0pUBQ",
                  client_secret = "9h4_iggh875nPzkfVtbs7BMUp6A",
                  username = "CH_BOT",
                  password = "jonesbitch")

subreddit = r.subreddit('testingground4bots')

""""
for submissions in subreddit.controversial(limit = 10):
    print(submissions.title)
    print(submissions.author)
    print('-'*20)
"""

def comment_word_count(user, keyword):
    word_count = 0
    # Create a reddit user instance
    # get all the comment in the redditor's history
    for comment in user.comments.new(limit = None):
        # Split the words in the comment in the
        for word in comment.body.split(' '):
            word.strip('.,-')
            if word.lower() == keyword:
                word_count += 1
    return word_count
"""
for comment in subreddit.stream.comments():
    text = comment.body
    print(text)
    user = comment.author
    if "!CommentHistory" in text:
        word_count = comment_word_count(user, text.split(' ')[1])
        print(word_count)
        message = "Hey u/{0}, you have commented the word {1} for {2} times!".format(user, text.split(' ')[1],
                                                                                     word_count)
        comment.reply(message)
        continue
"""






