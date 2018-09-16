from textblob import TextBlob, Word
from slang_ender import find_slang

def slang_coefficient(user):
    word_count = 0
    slang_count = 0
    for comment in user.comments.new(limit = None):
        comment = TextBlob(comment.body)
        #print(comment)
        for word in comment.words:
            word1 = Word(word)
            #print(word)
            word_count += 1
            if len(word1.definitions) != 0:
                continue
            if find_slang(word, 'temp.txt') == True:
                print("SLANG: " + word)
                slang_count += 1
        #print('-' * 20)
    return slang_count*1000.0/word_count

def age(user):
    if slang_coefficient(user) < 5:
        return("You probably are older than 25.")
    else:
        return("You probably are not 25 yet.")
