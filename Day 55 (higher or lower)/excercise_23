# TODO: Create the logging_decorator() function 👇



# TODO: Use the decorator 👇

def logging_decorator(function):
    def wrapper(*args):
        ans = function(*args)
        print(f"You called {function.__name__}{args}\nIt returned: {ans}")
        return ans
    return wrapper

@logging_decorator    
def a_function(*args):
    return sum(args)

result = a_function(1,2,3)

print(result)