from app import cel
import time
from utils.util_example import util_func


@cel.task
def task1_1(*args, **kwargs):
    util_func()
    print args
    print kwargs
    count = 0
    while True:
        time.sleep(1)
        print count,'......'
        count += 1
        if count >= 10:
            break

    return 123