import re


def validate_password(password):

    if password == "":
        raise ValueError("Password cannot be empty")

    if len(password) < 8 or len(password) > 20:
        raise ValueError("Password length should be between 8 and 20 characters")

    if re.search(r"[a-z]", password) is None:
        raise ValueError("Password needs a lowercase letter")

    if re.search(r"[A-Z]", password) is None:
        raise ValueError("Password needs an uppercase letter")

    if re.search(r"\d", password) is None:
        raise ValueError("Password needs a digit")

    if re.search(r"[@#$%!*&]", password) is None:
        raise ValueError("Password needs a special character")

    return True