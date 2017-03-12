"""
    This module contains some analytical features
"""
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import os


"""
    main method doing the analysis
"""


def do_twitter_analysis(term=None):
    if term is None:
        term = "Twitter"

    connect_to_twitter()
    words = load_semantic_words()


"""
    Connecting w/ the Twitter API through developer account

    Note that R package twitteR has to be installed and a developer account
    w/ given tokens and keys has to exist (have to be changed in the code beneath or
    have to be delivered through parameters)
"""


def connect_to_twitter(api_key="bs11GKzJqqfEsyj9iC93ZifGq",
                       api_secret="9L7A8HIBxttt76JNYIpIWBS0zAJTYncW6gXsW0rbjdloOSEmU0",
                       access_token="1367543593-2Uu7ViD5oB2kaI5ryogWaWzUykkQ4A9gExDtTp3",
                       access_token_secret="0DPMZFQyGVgjwrwxzgLJL0S7PqH2pXrZMwEzP6gMl3PSQ"):
    twitter = importr("twitteR")
    twitter.setup_twitter_oauth(api_key, api_secret, access_token, access_token_secret)


"""
    Loading files containing positive and negative words for scoring
"""


def load_semantic_words(directory=None):
    if directory is None:
        directory = os.path.dirname(__file__)
    else:
        directory = directory

    directory = directory.replace("\\", "/")
    ro.r('setwd("' + directory + '")')
    neg = ro.r('scan("words/negative-words.txt", what="character", comment.char = ";")')
    pos = ro.r('scan("words/positive-words.txt", what="character", comment.char = ";")')

    return [neg, pos]
