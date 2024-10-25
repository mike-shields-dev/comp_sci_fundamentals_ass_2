def format_to_sterling(value) -> str:
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

    if isinstance(value, (int, float)):
        return f"£{value:.2f}"
    else: 
        raise ValueError("Error: provided value must be an integer or decimal.")