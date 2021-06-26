"""
Hello, dear reader this repo contains important functions for python.
"""
# 1. Hello World most basic function in  python 
def Hello():
    return('Hello, World!')

Hello()

def split(word=Hello(),splitter = ','): # variables initialized, in case we don't define them while calling it will work with default
    splitter = '?'
    return word.split(f'{splitter}')
word = 'Hello? dear Azerbaijan solider? you deserve respect'
split(word)

def sum(a=0,b=0):
    a = 5 
    b = 3
    return a+b
sum()
""" 
Here, we can understand that functions are working in some sequence
def function(arg1,arg2): ------- You must define arguments here,if not, operation can only be done inside by initializing all variables
    function operation
    ...
    ...
    function operation
    return function(arg1,arg2) --- It is must part you must return in order to see result of function while Calling function 
funtion(arg1,arg2) ------- Here arg1,arg2 can be defined or not. This part is integrated part, 
means that you can update it consistently
"""
# Some most used functions in python 
