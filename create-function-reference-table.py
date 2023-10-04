import inspect
from prettytable import PrettyTable

def myfunc1(my_age: int, other_age: int):
    """
    This is a function to compare 2 ages
    """
    if my_age == other_age:
        age_equal = True
    else:
        age_equal = False
    return print(f'Age equal: {age_equal}')
    
def myfunc2(birth_town: str, country: str):
    """
    This is a function to print the birth town and country of birth
    """
    return print(f'I live in {birth_town} in {country}')

# Get the current module (the module where your script is running)
current_module = inspect.currentframe().f_globals

# Initialize a pretty table to store function information
function_table = PrettyTable()
function_table.field_names = ["Name", "Arguments", "Type Hints", "Docstring"]

# Filter and extract only functions
functions = [item for item in current_module.items() if inspect.isfunction(item[1])]

# Loop through the list of functions and gather information
for name, function in functions:
    if name != 'main':  # Exclude the 'main' function if it exists
        # Get function docstring
        docstring = inspect.getdoc(function)

        # Get function signature (arguments and type hints)
        signature = inspect.signature(function)
        args = []
        type_hints = []
        for param_name, param in signature.parameters.items():
            args.append(param_name)
            type_hints.append(str(param.annotation))

        # Add the function information to the table
        function_table.add_row([name, ", ".join(args), ", ".join(type_hints), docstring])

# Set left alignment for all columns
function_table.align = "l"

# Print the nicely formatted table
print("Function Reference Table:")
print(function_table)
