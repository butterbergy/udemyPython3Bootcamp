from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums():
    return sum([x for x in range(20000)])


@speed_test
def sum_nums2():
    return sum(x for x in range(20000))


# print(sum_nums())
# print(sum_nums2())


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed!")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def print_args(*args):
    print(*args)


# print_args(1, 2, 3)
# print_args(1, 2, 3, asdf="asdf")

# Example of passing args into decorator function
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return "First arg needs to be " + str(val)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "pizza"))
print(fav_foods("pizza", "burrito"))
