def is_name_valid(value: str):
    return not any(char.isdigit() for char in value)
