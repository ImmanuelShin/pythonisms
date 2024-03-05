import time
import logging

logging.basicConfig(level=logging.INFO)

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time spent in {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

def log_info(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} completed with result: {result}")
        return result
    return wrapper

def slow_down(func):
    def wrapper(*args, **kwargs):
        time.sleep(2)  
        result = func(*args, **kwargs)
        return result
    return wrapper

def convert_return_value(conversion_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return conversion_func(result)
        return wrapper
    return decorator

def validate_condition(condition_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition_func(*args, **kwargs):
                result = func(*args, **kwargs)
                return result
            else:
                raise ValueError("That ain't valid.")
        return wrapper
    return decorator


@calculate_time
def five_second_runtime():
    time.sleep(5)
    return "Five second execution complete"

@log_info
def multiply_numbers(x, y):
    return x * y

@calculate_time
@slow_down
def greet(name):
    return f"Two seconds later... Hello, {name}!"

@convert_return_value(lambda x: x ** 2)
def square_number(number):
    return number

@validate_condition(lambda a, b: b != 0)
def divide_numbers(a, b):
    return a / b

if __name__ == "__main__":
    print(five_second_runtime())
    print("----------------------------")
    print(multiply_numbers(3, 4))
    print("----------------------------")
    print(greet("John"))
    print("----------------------------")
    print(square_number(4))
    print("----------------------------")
    try:
        print(divide_numbers(10, 0))
    except ValueError as e:
        print(f"Error: {e}")