import validators
from validator_collection import validators, checkers, errors

email = input("Email:")

try:
    email_address = validators.email(email)
    print("Valid")
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")

