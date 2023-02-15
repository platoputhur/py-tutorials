import logging
from typing import Optional
from src.utils.settings import get_env
from src.utils.tweet_type import TweetType
import openai

class GPTManager:
    def __init__(self) -> None:
        self._api_key = get_env("OPENAI_API_KEY")

    def generate_tweet(self, tweet_type: TweetType) -> Optional[str]:
        """
        Generates the tweet based on the tweet_type param
        """
        openai.api_key = self._api_key
        try:
            # Ref 1: https://platform.openai.com/docs/models/gpt-3
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=tweet_type.prompt,
                temperature=0.5,
                max_tokens=50
            )
            return response.choices[0].text.strip()
        except openai.error.RateLimitError as e:
            logging.getLogger("GPTTweeter").error(e)
            return None

