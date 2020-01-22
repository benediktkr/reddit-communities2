# reddit-communities2

Some years ago I made [reddit-communities](https://github.com/benediktkr/reddit-communities) that looked at how subreddits were connected through the links on their sidebars.

Now I want to see how subreddits are connected based on where their users are active. That will be a lot more data, and this time I'll make a nicer presentatino. The data from the former project still exists, and could be presented in the same format. I hear theres nice JS plugins you can just plug the data into.

DISCLAIMER: This is purely a weekend/evening hack project.

## Current status

Looking at the crazy side of reddit:

```
$ pipenv run python run.py --seed-subreddit the_donald
Checking where users from /r/the_donald also post...
[('The_Donald', 1734),
 ('worldpolitics', 51),
 ('Conservative', 35),
 ('Kanye', 23),
 ('PublicFreakout', 21),
 ('politics', 20),
 ('Full_news', 17),
 ('AskReddit', 13),
 ('hiphopheads', 12),
 ('funny', 12)]
 ```

 More chill:
