import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def get_env(env_key: str) -> str:
    """
    Gets the environment variables based on key
    """
    return os.environ.get(env_key)