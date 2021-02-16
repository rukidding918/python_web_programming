from functools import wraps
from inspect import getcallargs
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_args = getcallargs(func, *args, **kwargs)
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'{func.__name__!r}: {run_time:.4f} seconds, {func_args}')
        return value
    return wrapper

# def type_check(func):
#     @wraps(func)
#     def wrapper(*args, **kwags):
#         for a in args:
#             try:
#                 type(a) != int
#             except Exception as e:
#                 print('It`s not integer!', e)
#
#
# @type_check
@timer
def some_calc(num):
    for _ in range(num):
        some_list = [x**x for x in range(1000)]

if __name__ == '__main__':
    some_calc(1000)

class Pizza:
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)