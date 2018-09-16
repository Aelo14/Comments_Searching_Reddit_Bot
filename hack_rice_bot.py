import praw

## Creating a new bot instance
bot = praw.Reddit(user_agent = "hack_rice_bot",
                  client_id = "zdJnszNfMHt_2Q",
                  client_secret = "Bx_vyLj1XpJMYhCVwNRZIayLutQ",
                  username = "cute_doggo_pic",
                  password = "jonesbitch")

## This subreddit is useful
subreddit = bot.subreddit('testingground4bots')

## This maintains a constant stream of comments in real time
comments = subreddit.stream.comments()

## Looks at every comment
for comment in comments:
    text = comment.body ## Get comment's body
    author = comment.author ## Get comment's body
    if 'hackrice' in text.lower():
        ## Generate message
        message = "Hey u/{0}, it looks like you're interested in HackRice! For more information, please visit [our website](http://hack.rice.edu)".format(author)
        comment.reply(message) ## Send message

