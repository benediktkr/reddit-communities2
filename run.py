#!/usr/bin/env python3.7

from pprint import pprint
from collections import Counter

import praw

from common import get_parser, log_in

subreddits = Counter()

if __name__ == "__main__":
    args = get_parser()

    reddit = log_in()
    seed = reddit.subreddit(args.seed_subreddit)
    also_post_in = list()
    print(f"Checking where users from /r/{seed} also post...")
    for post in getattr(seed, args.subreddit_mode)(limit=args.post_limit):
        user = reddit.redditor(post.author.name)
        # logger question mark?
        #print(post.author.name)
        for comment in user.comments.new():
            also_post_in.append(comment.subreddit.name)

    subreddits.update(also_post_in)

pprint(subreddits.most_common(10))
