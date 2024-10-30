def format_to_sterling(value: float | int) -> str:
    """
    Formats a numeric value as a denomination in 
    pounds sterling.

    Args: 
        (int or float): The value to be formatted.

    Raises:
        ValueError: If provided value is not an integer or a decimal. 

    Returns: 
        str: The provided numeric value with
            - Prefix: "£" symbol
            - Suffix: The value padded to 2 decimal places
    """

    # Check if value is an int or float, but not a bool
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return f"£{value:.2f}"
    else: 
        raise ValueError("Error: Cannot format provided amount, the amount must be number")
