import praw
from textblob import TextBlob

from keywords import key_words, r

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyscreenshot

# dictionary = {"hey":1,"hi":2,"hello":3}
# print (dict_to_string(dictionary))

def create_word_cloud(words):
    # To prevent download dialog
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2)  # custom location
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', '/wordclouds')
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/svg+xml')

    driver = webdriver.Firefox(profile)
    # worldcloud generator website we need to access
    driver.get("https://www.jasondavies.com/wordcloud/")
    elem = driver.find_element_by_id("text")
    # clear sample text from wordcloud
    elem.clear()
    # add our words
    elem.send_keys(words)
    elem.send_keys(Keys.RETURN)

    # generate wordcloud
    driver.find_element_by_id("go").click()
    # wait for new wordcloud to load, then download
    time.sleep(5)
    pyscreenshot.grab()
    print(driver.find_element_by_id("text").text)

    driver.find_element_by_id("download-svg").click()
    # change image download settings in Applications tab in Firefox's options
create_word_cloud(key_words(r.redditor('aelo14')))
# def imgur_upload():
# CLIENT_ID = "a73085de79cee10"
# PATH = "C:\Users\gvmer_000\Downloads\wordcloud.svg"
# im = pyimgur.Imgur(CLIENT_ID)
# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
# print(uploaded_image.title)
# print(uploaded_image.link)
# print(uploaded_image.size)
# print(uploaded_image.type)


# print (key_words(me))

# #print (dict_to_string(key_words(r.redditor('therealbillgates'))))
# create_word_cloud(dict_to_string(key_words(me)))
# imgur_upload()
# os.remove("C:\Users\gvmer_000\Downloads\wordcloud.svg")create_word_cloud(key_words(r.redditor('aelo14')))