from functools import wraps
from time import time


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(
            f"{func.__name__}: {(end_time-start_time)*1000:.3f} milliseconds.")
        return result
    return wrapper
