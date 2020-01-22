#!/usr/bin/env python3.7

from collections import Counter
from pprint import pprint
from time import sleep
import logging

import praw

from common import get_parser, log_in

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

subreddits = Counter()

if __name__ == "__main__":
    args = get_parser()
    if args.debug:
        handler = logging.StreamHandler()
        prawlogger = logging.getLogger('prawcore')
        prawlogger.addHandler(handler)
        prawlogger.setLevel(logging.DEBUG)
        #logger.setLevel(logging.DEBUG)

    reddit = log_in()
    seed = reddit.subreddit(args.seed_subreddit)
    also_post_in = list()
    logging.info(f"Checking where users from /r/{seed} also post...")
    for post in getattr(seed, args.subreddit_mode)(limit=args.post_limit):
        user = reddit.redditor(post.author.name)
        logging.info(f"Checking where /u/{post.author.name} posts..")
        for comment in user.comments.new():
            # Looks like comment.subreddit.name isnt a simple attribute
            # but is making http calls to reddit.com/r/subreddit/about
            # each time
            subreddit_name = str(comment.subreddit)
            also_post_in.append(subreddit_name)

    subreddits.update(also_post_in)

pprint(subreddits.most_common(10))
