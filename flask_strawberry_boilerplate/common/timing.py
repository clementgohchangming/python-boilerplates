import time
from functools import partial, wraps

from common.logger import logger


def timeit(func=None, *, tag=None):
    """
    A decorator to time a callable function
    :param func: decorate a function definition with this decorator to time the function

    @timeit
    def my_function()

    :param tag:
    :return: Returns the decorated function, with a timing and logging behaviour.
    - It will now run the function, and logs the time taken
    """
    if func is None:
        return partial(timeit, tag=tag)

    @wraps(func)
    def _timeit(*args, **kwargs):
        tstart = time.time()
        res = func(*args, **kwargs)
        duration = time.time() - tstart
        logger.info(f'{tag or func.__name__} takes about {duration} seconds. args={args}, kwargs={kwargs}')
        return res
    return _timeit


def timeslow(func=None, *, tag=None, threshold: int = 5):
    """
    A decorator to time a callable function, if it took longer than the threshold number of seconds
    :param func: decorate a function definition with this decorator to time the function

    @timeit
    def my_function()

    :param tag:
    :return: Returns the decorated function, with a timing and logging behaviour.
    - It will now run the function, and logs the time taken if it took longer than 5 seconds
    """
    if func is None:
        return partial(timeit, tag=tag)

    @wraps(func)
    def _timeit(*args, **kwargs):
        tstart = time.time()
        res = func(*args, **kwargs)
        duration = time.time() - tstart
        if duration >= threshold:
            logger.info(f'Slow function detected. {tag or func.__name__} takes about {duration} seconds. args={args}, kwargs={kwargs}')
        return res
    return _timeit
