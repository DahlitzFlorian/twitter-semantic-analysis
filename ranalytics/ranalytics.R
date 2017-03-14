# necessary libraries
library(stringr)
library(twitteR)
library(xlsx)
library(plyr)

# connect w/ twitter
connect.twitter = function(api_key="bs11GKzJqqfEsyj9iC93ZifGq",
                            api_secret="9L7A8HIBxttt76JNYIpIWBS0zAJTYncW6gXsW0rbjdloOSEmU0",
                            access_token="1367543593-2Uu7ViD5oB2kaI5ryogWaWzUykkQ4A9gExDtTp3",
                            access_token_secret="0DPMZFQyGVgjwrwxzgLJL0S7PqH2pXrZMwEzP6gMl3PSQ")
{
    api_key <- api_key
    api_secret <- api_secret
    access_token <- access_token
    access_token_secret <- access_token_secret
    setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)
}

# get positive and negative words
get.words = function(full.path=getwd())
{
    neg = scan(paste(full.path, "/ranalytics/src/negative-words.txt", sep=""), what="character", comment.char=";")
    pos = scan(paste(full.path, "/ranalytics/src/positive-words.txt", sep=""), what="character", comment.char=";")

    return(c(pos, neg))
}

# decide sentiment
score.sentiment = function(tweets, pos.words, neg.words)
{
    require(plyr)
    require(stringr)

    scores = laply(tweets, function(tweet, pos.words, neg.words) {



    tweet = gsub('https://','',tweet) # removes https://
    tweet = gsub('http://','',tweet) # removes http://
    tweet=gsub('[^[:graph:]]', ' ',tweet) ## removes graphic characters like emoticons 
    tweet = gsub('[[:punct:]]', '', tweet) # removes punctuation 
    tweet = gsub('[[:cntrl:]]', '', tweet) # removes control characters
    tweet = gsub('\\d+', '', tweet) # removes numbers
    tweet=str_replace_all(tweet,"[^[:graph:]]", " ") 

    tweet = tolower(tweet) # makes all letters lowercase

    word.list = str_split(tweet, '\\s+') # splits the tweets by word in a list
 
    words = unlist(word.list) # turns the list into vector
 
    pos.matches = match(words, pos.words) ## returns matching values for words from list 
    neg.matches = match(words, neg.words)
 
    pos.matches = !is.na(pos.matches) ## converts matching values to true of false
    neg.matches = !is.na(neg.matches)
 
    score = sum(pos.matches) - sum(neg.matches) # true and false are treated as 1 and 0 so they can be added
 
    return(score)
 
}, pos.words, neg.words )
 
scores.df = data.frame(score=scores, text=tweets)
 
return(scores.df)
 
}

# do analysis
do_analysis = function(term, number=100, working.directory=getwd())
{
    if(missing(term)) {
        term <- "Twitter"
    }

    connect.twitter()
    words = get.words(working.directory)

    tweets = searchTwitter(term,n=number)
    Tweets.text = laply(tweets,function(t)t$getText()) # gets text from Tweets

    analysis = score.sentiment(Tweets.text, words[0], words[1]) # calls sentiment function
    write.xlsx(analysis, paste(working.directory, "/log/", term, ".xlsx", sep=""))
}