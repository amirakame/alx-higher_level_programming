#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    
    for i in range(len(roman_string)):
        current_value = roman_values[roman_string[i]]
        
        if i == len(roman_string) - 1:
            integer_value += current_value
        else:
            next_value = roman_values[roman_string[i+1]]
            
            if current_value >= next_value:
                integer_value += current_value
            else:
                integer_value -= current_value
    
    return integer_value
