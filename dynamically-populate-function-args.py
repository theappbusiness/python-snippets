'''
This is an example of how to dynamically extract the required arguments of functions and pass the relevant variable as needed.
Create any number of functions and a number of variables. As long as the variable names match the names of the function arguments this will work.

Improvement: how can we programmatically extract the list of functions to call and then call them one by one?
function_list = ([f.__name__ for f in globals().values() if type(f) == type(lambda *args: None)]) - this produces a list of functions with each one being a string, which is not callable.
'''

import inspect
import pprint

def myfunc1(my_age: int, other_age: int):
    if my_age == other_age:
        age_equal = True
    else:
        age_equal = False
    return print(f'Age equal: {age_equal}')
    
def myfunc2(birth_town: str, country: str):
    return print(f'I live in {birth_town} in {country}')

my_age = 42
other_age = 10
birth_town = 'Newcastle'
country = 'UK'

# list of variables in the current context using vars()
vars_dict = {k: v for k, v in vars().items()}

# List of functions
functions = [myfunc1, myfunc2]

# Loop through functions and dynamically pass arguments
for function in functions:
    arg_names = inspect.getfullargspec(function).args
    args_to_pass = {arg_name: vars_dict[arg_name] for arg_name in arg_names if arg_name in vars_dict}
    print(f'function: {function.__name__} -> function args: {arg_names} -> args_to_pass: {args_to_pass}')
    # Call the function with the arguments
    result = function(**args_to_pass)
