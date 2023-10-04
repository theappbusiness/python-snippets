'''
This is an example of how to dynamically extract the required arguments of functions and pass the relevant variable as needed.
Create any number of functions and a number of variables. As long as the variable names match the names of the function arguments this will work.
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

# Get the current module (the module where the script is running)
current_module = inspect.currentframe().f_globals

# Filter and extract only functions
functions = [item for item in current_module.items() if inspect.isfunction(item[1])]

# Loop through the list of functions and call each one
for name, function in functions:
    if name != 'main':  # Exclude the 'main' function if it exists
        print(f"Calling function: {name}")
        try:
            # get the function arguments that are required
            arg_names = inspect.getfullargspec(function).args

            # get the variables to pass as function arguments
            args_to_pass = {arg_name: vars_dict[arg_name] for arg_name in arg_names if arg_name in vars_dict}

            # Call the function
            result = function(**args_to_pass)
            print(f"Function {name} returned: {result}")

        except Exception as e:
            print(f"Error calling function {name}: {e}")
