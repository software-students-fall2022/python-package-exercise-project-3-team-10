
def convert_number(to_numeral_system, number):
    ''' converts a number into the to_numeral_system indicated 
        Note: The number could be in binary, octal, decimal, or hexadecimal form.
    '''

    numeral_systems = ["binary", "octal", "decimal", "hexadecimal"]
    if to_numeral_system not in numeral_systems:
        raise ValueError("Invalid numeral system")
    try:
        number = int(number)
    except ValueError:
        raise ValueError("Invalid number")
    if to_numeral_system == "binary":
        return bin(number)
    elif to_numeral_system == "octal":
        return oct(number)
    elif to_numeral_system == "decimal":
        return number
    elif to_numeral_system == "hexadecimal":
        return hex(number)