from src.utils.gpt_manager import GPTManager
from src.utils.tweet_type import TweetType


def start_worker():
    gpt_manager = GPTManager()
    tweet_types = '\n- '.join([v.value for v in TweetType])
    while True:
        print("This program generates tweets.")
        print(f"""What kind of tweet do you want?
- {tweet_types}
- exit (exits the app)
        """)
        user_input = input("Please enter your choice: ").lower()
        if user_input not in [v.value for v in TweetType]:
            exit(0)
        tweet_type = TweetType(user_input)
        if tweet := gpt_manager.generate_tweet(tweet_type=tweet_type):
            print(tweet)
        else:
            print("Sorry, tweet can't be generated at the moment!")
        print("\n")

