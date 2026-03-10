#My Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# with arguments

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs) # Return the value of the function
    return wrapper

@do_twice
def greet(name):
    print(f"Hello {name}")
    return f"Finished greeting {name}"

result = greet("Alice")
print(result)

#preserv metadata
import functools

def preserve_metadata(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def original_function():
    """This is a docstring."""
    pass

print(original_function.__name__) # Output: original_function
