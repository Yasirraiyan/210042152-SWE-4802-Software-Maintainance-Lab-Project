def validate_number(value: str) -> float:
    """
    Convert user input to a floating-point number.

    Raises:
        ValueError: If the input is not a valid number.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError("Invalid number. Please enter a valid number.")