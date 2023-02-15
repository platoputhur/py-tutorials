from enum import Enum

class InvalidTweetTypeError(Exception):
    """Raises when invalid tweet type is given"""

class TweetType(Enum):
    """
    Topics for Tweets
    """
    QUOTE = "quote"
    JOKE = "joke"
    FACT = "fact"


    @property
    def prompt(self):
        """
        A helper function for getting the prompt from the tweet type
        """
        if self.value == "quote":
            return "write tweet with a quote"
        elif self.value == "joke":
            return "write tweet with a joke"
        elif self.value == "fact":
            return "write a tweet with a fun fact"
        else:
            raise InvalidTweetTypeError("Invalid tweet type")
