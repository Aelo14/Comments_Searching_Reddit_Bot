def find_slang(slang, filename):
    f = open(filename, 'r')
    for line in f:
        if slang.lower() == line.split('`')[0].lower():
            return True
    return False

"""
def slang_count_func(user):
    word_dict = word_trend(user)
    slang_count = 0
    for key, value in word_dict:
        if find_slang(key) == True:
            slang_count += value
    return slang_count

slang_count_func(r.redditor('aelo14'))
"""