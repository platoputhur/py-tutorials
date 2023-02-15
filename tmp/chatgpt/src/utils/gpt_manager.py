import openai
from src.utils.settings import get_env
from src.utils.tweet_type import TweetType
import logging

class GPTManager:
    """
    GPTManager which generates the interacts with the openai api
    """
    def __init__(self) -> None:
        """
        Initializes the gpt manager class with the api key
        """
        self._api_key = get_env("OPENAI_API_KEY")

    def generate_tweet(self, tweet_type: TweetType = TweetType.QUOTE) -> str:
        """
        generates the tweet
        """
        openai.api_key = self._api_key
        """
        Token: A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This translates to roughly ¾ of a word (so 100 tokens ~= 75 words).
        https://platform.openai.com/tokenizer

        Engine: https://platform.openai.com/docs/models/gpt-3
        """
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{tweet_type.prompt}",
                temperature=0.5,
                max_tokens=50, # 50*4 = 200 close to twitter's limit
                n=1,
                stop=None,
                frequency_penalty=0,
                presence_penalty=0
            )
            tweet = response.choices[0].text.strip()
            return tweet
        except openai.error.RateLimitError as e:
            logging.getLogger("Tweeter").error(e)
            return None
