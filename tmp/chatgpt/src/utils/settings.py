import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def get_env(env_key: str):
    """
    Gets the relevant environment variable value
    """
    return os.environ.get(env_key)
