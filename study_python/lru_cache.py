import time
import functools

def perf_time_checker(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return value
    return wrapper

@functools.lru_cache(maxsize=None)
@perf_time_checker
def calc_with_lru(number: int) -> int:
    total = 0
    for n in range(number):
        total += n**n
    return total


@perf_time_checker
def calc_with_not_lru(number: int) -> int:
    total = 0
    for n in range(number):
        total += n**n
    return total

print(calc_with_lru(3000))
print(calc_with_lru(3000))
print()
print(calc_with_not_lru(3000))
print(calc_with_not_lru(3000))