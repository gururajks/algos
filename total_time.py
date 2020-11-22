import os, json
import functools
import time
import enum

def total_time(f):
    @functools.wraps(f)
    def wraps(*args, **kwargs):
        start_time = time.time()
        val = f(*args, **kwargs)
        end_time = time.time()
        duration = (end_time - start_time)
        unit = {
            0 : "seconds",
            1 : "milli seconds",
            2 : "micro seconds",
            3 : "nano seconds"
        }
        count = 0
        while duration < 1:
            duration *= 1000
            count += 1
        print(f"Duration: {duration}  {unit[count]}")
        return val

    return wraps
