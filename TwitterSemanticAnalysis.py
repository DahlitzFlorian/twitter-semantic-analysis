"""
    -----------------------------------
    TwitterSemanticAnalysis.py
    -----------------------------------
    This application is made to easily do some semantic analysis making use of the
    Twitter API (used w/ R).
    -----------------------------------
"""
# import rpy2.robjects as ro
import os
from tkinter import *
from tkinter import filedialog
from analytics.twitterapi import TwitterAPI


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.term = Entry(self)
        self.number = Entry(self)
        self.button = Button(self, text="Get", command=self.click_submit)
        self.term_label = Label(self, text="Term to search")
        self.number_label = Label(self, text="Number of tweets")
        self.button.pack()
        self.term_label.pack()
        self.term.pack()
        self.number_label.pack()
        self.number.pack()

    def check_empty(self, term, number):
        if len(term) == 0:
            term = "Twitter"
        if len(number) == 0:
            number = 100
        return {1: term, 2: number}

    def click_submit(self):
        values = self.check_empty(term=self.term.get(), number=self.number.get())
        twitterapi = TwitterAPI(twitter_consumer_key="bs11GKzJqqfEsyj9iC93ZifGq",
                                twitter_consumer_secret="9L7A8HIBxttt76JNYIpIWBS0zAJTYncW6gXsW0rbjdloOSEmU0",
                                twitter_access_token="1367543593-2Uu7ViD5oB2kaI5ryogWaWzUykkQ4A9gExDtTp3",
                                twitter_access_secret="0DPMZFQyGVgjwrwxzgLJL0S7PqH2pXrZMwEzP6gMl3PSQ")
        tweets = twitterapi.get_tweets(term=values[1], number=values[2])

root = App()
root.title("Twitter Semantic Analysis")
root.minsize(width=866, height=533)

# run
root.mainloop()
