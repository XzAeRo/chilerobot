import praw
import settings
import os

user_agent = ("User-Agent: python:cl.vgr.chilerobot:v1.0.0 (by /u/XzAeRosho) github.com/xzaero/chilerobot")

reddit = praw.Reddit(user_agent=user_agent,
                     client_id=os.environ.get("CLIENT_ID"),
                     client_secret=os.environ.get("CLIENT_SECRET"),
                     username=os.environ.get("USERNAME"),
                     password=os.environ.get("PASSWORD"))

for submission in reddit.subreddit('chile').hot(limit=10):
    print(submission.title)
