import sympy as sym

'''
Syntax Error
Lightwork Constants: VAR, FUNC, OUTPUT, CHECK PARSE, VERSION
- A statement does not start with lightwork constants then error. 
- Lightwork should be case sensitive.
- A statement does not end with a semicolon.
- A statement can have multiple semi-colons in a row but they all will be ignored except the first one
- A statement must have only one of the lightwork constants

What to do for syntax error?
Just output that there was a syntax error and how them the line. Link them to the help document if needed. Move onto the next line.
'''

'''
Logic
- Create a tuple that keeps track of the lines
- Have variables that keep track of errors
- Have a set of dictionaries for all variables and another set of dictionaries for all functions
'''


'''
Functions yet to implement:
- valid_var_func: cause I figured if i spend too much time on checking the syntax i would make very little progress, will do this later.

'''

#----------------------------------------------------------------------------------------------------------

#counts how many lightwork constants are present in a user input
def only_1_constant(the_string, constant_list):
    constant_count = 0

    for i in constant_list:
        while i in the_string:
            the_string = the_string.replace(i, "", 1)
            constant_count += 1

            if constant_count > 1:
                return False
    
    return True

#used to check if the first characters match any of the lightwork constants
def first_constant(the_string, constant_tuple, exception_tuple):
    for i in constant_tuple:
        
        if i in exception_tuple:
            if the_string[0: len(i)] == i:
                return True

        else:
            if the_string[0: (len(i) + 1)] == (i + " "):
                return True
    
    return False

#checks if the variable's and function's name (for functions the inside variable as well) is valid or not. Not yet installed.
def valid_var_func(the_string):
    if the_string[0:4] == 'VAR ':
        pass
    elif the_string[0:5] == 'FUNC ':
        pass
    else:
        return NA
    
#adds a variable onto the variable dictionary
def add_variable(the_string, var_dict):
    if the_string[0:4] == "VAR ":
        equal_pos = the_string.index("=")
        name = (the_string[4: equal_pos]).strip()
        contents = (the_string[equal_pos+2:]).strip()
        var_dict[name] = contents

#adds a function onto the function dictionary, and have the sympy implementation here as well. Todo: implement the add_function function
def add_function(the_string, func_dict):
    if the_string[0:5] == "FUNC ":
        open_bracket = the_string.index("(")
        close_bracket = the_string.index(")")
        equal_pos = the_string.index("=")

        name = (the_string[5:open_bracket]).strip()

        variable_tuple = tuple((the_string[open_bracket + 1 : close_bracket]).strip()) #gets the variables in terms of strings
        contents = sym.parse_expr((the_string[equal_pos+1:]).strip()) #the actual function

        variable_dict = {}

        for x in variable_tuple:
            variable_dict[x] = sym.symbols(x)
        
        scanner = the_string[(open_bracket+1) : close_bracket].replace(" ", "") #used to store the variables names as a string so it is easier to scan through the dictionary
        func_dict[name] = (variable_dict, contents, scanner) # the dictionary that houses the variable names and contents, as well as a scanner variable


#performs the correct operation when the OUTPUT command is used. This assumes that the syntax is correct.
def output_function(the_string, var_dict):
    the_string = the_string.strip()
    copy_original = the_string
    
    for var in var_dict:
        if var in the_string:
            the_string = the_string.replace(var, var_dict[var])
    
    print(copy_original, "=", eval(the_string))

#used to simplify functions
def simplify_funtion(the_string, func_dict):
    the_string = the_string.strip()

    

if __name__ == "__main__":

    VALID = 1
    INVALID = 0
    NA = -1

    test_string = '''
VAR g = 12;
FUNC k(x) = x^2 + 1;;;;;;;;OUTPUT g^4;

21 Century Schzoidman;

OUTPUT OUTPUT OUTPUT OUTPUT;


VAR pitr43yuio2            =  3.1415926535;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   

VERSION;

    '''
    
    LIGHTWORK_EXCEPTION_CONSTANTS = ('CHECK PARSING', 'VERSION')
    LIGHTWORK_FUNCTION_CONSTANTS = ("SOLVE", "OUTPUT EVAL", "SIMPLIFY", "INT", "DIFF", "LIM", "FACTOR")
    LIGHTWORK_CONSTANTS = ("VAR", 'FUNC', 'OUTPUT') + LIGHTWORK_EXCEPTION_CONSTANTS + LIGHTWORK_FUNCTION_CONSTANTS

    VERSION = 1.0
    command_tuple = ()
    variable_dict = {} # a dictionary to store all variables, consists of the variable name and value.
    function_dict = {} #dictionary to hold all the functions and their values. Structure is {name : ((variables), function expression)}

    #getting the command tuple

    #correcting the user's syntax a bit by removing all unecessary new lines and semi-colon
    test_string = test_string.replace("^", "**")
    
    while '\n' in test_string: #removing all new lines
        test_string = test_string.replace('\n', '')
    
    while ('; ' in test_string) or (';;' in test_string):
        test_string = test_string.replace('; ', ';')
        test_string = test_string.replace(';;', ';')

    j = 0

    for i in range(len(test_string)): #adding potential commands onto command tuple and also checking syntax
        if test_string[i] == ';':
            
            append_string = test_string[j:i]

            if first_constant(append_string, LIGHTWORK_CONSTANTS, LIGHTWORK_EXCEPTION_CONSTANTS) and only_1_constant(append_string, LIGHTWORK_CONSTANTS):
                command_tuple = command_tuple + (append_string,)
            
            else:
                print("Error Parsing: ", append_string, '\n')
                j += len(append_string)
            
            j = i+1
    
    #execution loop
    for i in command_tuple:
        if i[0:3] == "VAR":
            add_variable(i, variable_dict)
        
        elif i[0:4] == "FUNC":
            add_function(i, function_dict)

        elif i[0:6] == "OUTPUT":
            output_function(i[6:], variable_dict)
        
        elif i[0:13] == "CHECK PARSING":
            print(*command_tuple, sep='\n')
        
        elif i[0:7] == "VERSION":
            print("LIGHTWORK VERSION", VERSION)
        
        elif i[0:8] == "SIMPLIFY":
            simplify_funtion(i[8:], function_dict)
        
    
    print("Testing: ", function_dict["k"][1].subs(function_dict["k"][0]["x"], 4))
#libraries to use: sympy, scipy, numpy, qiskit (for quantum based things)?, matplotlib (maybe even plotly), Pint(unit error management)
#up to line 109
