"""This program checks new posts to a specified subreddit, and if they are not flaired
within 18-20min, the bot will send a private message to the user. This message as well
as it's title and the subreddit the bot is intended to be run on can be specified in
the config.py file."""

import time
import datetime
import praw
import config

def bot_login():
    """This function logs the bot into reddit given the parameters specified in the config.py"""
    reddit = praw.Reddit(username = config.USERNAME,
            password = config.PASSWORD,
            client_id = config.CLIENT_ID,
            client_secret = config.CLIENT_SECRET,
            user_agent = "Flair Bot")

    return reddit

def run_bot(reddit):
    """Runs the bot, checking new posts in a subreddit and messaging users who do not flair their
    posts within the specified timeframe"""
    for submission in reddit.subreddit(config.SUBREDDIT).new(limit=20):
        posttime = get_dif(submission)
        if (posttime > datetime.timedelta(minutes=18) and posttime < datetime.timedelta(minutes=20)
                and submission.link_flair_text is None):
            submission.author.message(config.TITLE, config.MESSAGE)
            print submission.author

def get_dif(submission):
    """This function gets the time difference between the time the thread was updated and now"""
    date = datetime.datetime.fromtimestamp(submission.created_utc)
    dif = datetime.datetime.utcnow() - date

    return dif - datetime.timedelta(hours=4)

reddit = bot_login()

while True:
    run_bot(reddit)
    print "Done loop!"

    time.sleep(118)
