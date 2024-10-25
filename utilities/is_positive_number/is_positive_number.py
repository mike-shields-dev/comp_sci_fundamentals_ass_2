def is_positive_number(value: float | int) -> bool:
    """
    Returns: 
        (bool): True if the provided value is a `float` or `int` 
                and that it is greater than 0
    """
    return isinstance(value, (int, float)) and value > 0

