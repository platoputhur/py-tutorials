from enum import Enum


class TweetType(Enum):
    """
    Topics for tweets
    """
    QUOTE = "quote"
    JOKE = "joke"
    FACT = "fact"
    HAIKU = "haiku"

    @property
    def prompt(self):
        """
        property to get the prompt for openai
        """
        return f"write a tweet with a {'fun ' + self.value if self.value == 'fact' else self.value}"
