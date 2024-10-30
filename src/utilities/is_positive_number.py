def is_positive_number(value: float | int) -> bool:
    """
    Validates that the provided value argument is
    a non-empty string. 
    
    Returns: 
        (bool): 
            - True: 
                if the provided value is a `float` or `int` 
                and it is greater than 0
                
            - False: 
                otherwise
    """
    # Check if value is an int or float, but not a bool
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0
