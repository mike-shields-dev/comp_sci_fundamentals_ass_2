def is_non_empty_str(value: str) -> bool:
    """
    Returns:
        bool: 
            Indicates whether the provided value is:
            - A string
            - A non-empty string with non-whitespace characters
    """
    return isinstance(value, str) and bool(value.strip())