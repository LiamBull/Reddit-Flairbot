import praw
import datetime
import config
import time

def bot_login():
    reddit = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Flair Bot")
    
    return reddit
    
def run_bot(reddit):
    for submission in reddit.subreddit(config.subreddit).new(limit=20):
        posttime = get_dif(submission)
        if posttime > datetime.timedelta(minutes=18) and posttime < datetime.timedelta(minutes=20) and submission.link_flair_text is None:
            submission.author.message(config.title, config.message)
            print submission.author
        
def get_dif(submission):
    date = datetime.datetime.fromtimestamp(submission.created_utc)
    dif = datetime.datetime.utcnow() - date
    
    return dif - datetime.timedelta(hours=4)

reddit = bot_login()

while True:
    run_bot(reddit)
    print "Done loop!"

    time.sleep(118)