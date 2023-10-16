import time
import random
from functools import wraps


def timer(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print("time cost:{} seconds".format(time.perf_counter() - st))
        return ret

    return decorated


@timer
def random_sleep():
    time.sleep(random.random())


random_sleep()

print(random_sleep.__name__)

def repeat(num):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

# Applying the decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Calling the decorated function
greet("Alice")