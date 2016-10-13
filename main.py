import praw
import settings
from scrappers import elmostrador
import os, pprint

def main():
    user_agent = ("User-Agent: python:cl.vgr.chilerobot:v1.0.0 (by /u/XzAeRosho) github.com/xzaero/chilerobot")

    reddit = praw.Reddit(
        user_agent=user_agent,
        client_id=os.environ.get("CLIENT_ID"),
        client_secret=os.environ.get("CLIENT_SECRET"),
        username=os.environ.get("USERNAME"),
        password=os.environ.get("PASSWORD")
    )

    subreddit = reddit.subreddit('chilerobot_bootcamp')
    #for submission in reddit.subreddit('chile').hot(limit=20):
    #    process_submission(submission)
    for submission in subreddit.stream.submissions():
        process_submission(submission)

def process_submission(submission):
    supported_domains = ['elmostrador.cl']

    if submission.domain in supported_domains:
        parser = elmostrador.Parser(submission.url)
        submission.reply(parser.parse() + settings.SIGNATURE_TEMPLATE)


if __name__ == '__main__':
    main()
