# Chap02/twitter_get_home_timeline.py
import json
from tweepy import Cursor
from TwitterClient import get_twitter_client

if __name__ == '__main__':

    client = get_twitter_client()

    with open('home_timeline.jsonl', 'w') as f:
        for page in Cursor(client.home_timeline, count = 200).pages(4):
            for status in page:
                # Process a single status
                f.write(json.dumps(status._json)+"\n")
# Chap02/twitter_get_home_timeline.py
import json
from tweepy import Cursor
from TwitterClient import get_twitter_client

if __name__ == '__main__':

    client = get_twitter_client()

    with open('home_timeline.jsonl', 'w') as f:
        for page in Cursor(client.home_timeline, count = 200).pages(4):
            for status in page:
                # Process a single status
                f.write(json.dumps(status._json)+"\n")
