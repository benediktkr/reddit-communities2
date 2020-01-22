#/usr/bin/env python3.7

import argparse
import json

import praw

POST_MODES = [   "hot"
               , "new"
               , "rising"
               , "controversial"
               , "top" ]
USER_AGENT = "github.com/benediktkr/reddit-communities2"

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-subreddit", required=True)
    parser.add_argument("--subreddit-mode", choices=POST_MODES, default="hot")
    parser.add_argument("--post-limit", type=int, default=25)

    return parser.parse_args()

def get_config(path=None):
    if not path:
        path = ".config"
    with open(path, 'r') as f:
        return json.loads(f.read())

def log_in():
    config = get_config()
    return  praw.Reddit(client_id=config['id'],
                        client_secret=config['secret'],
                        password=config['pass'],
                        user_agent=USER_AGENT,
                        username=config['user'])
