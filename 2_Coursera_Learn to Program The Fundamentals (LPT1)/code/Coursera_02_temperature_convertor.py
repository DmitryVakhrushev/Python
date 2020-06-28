#------------------------------------
# Coursera_02_temperature_convertor.py

def convert_to_celsius(fahrenheit):
    '''
    (number) -> float
    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''
    return (fahrenheit - 32) * 5/9



#---------------------------
# Examples
# >>> convert_to_ccelsius(32)
# 0
# >>> convert_to_celsius(212)
# 100
        
# Type Contract
# (number) -> number
        
# Header
# def convert_to_celsius(fahrenheit):
        
# Description
# Return the number of Celsius degrees equivalent to fahrenheit degrees.
        
# Body
# return (fahrenheit - 32) * 5 / 9
        
# Test
# Run the examples.   
        

