# validators.py

from typing import Optional

from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min_length: int, max_length: int, message: Optional[str] = None):
    """
    Function-based validator factory.
    Validates that numeric value length (in digits) is between min_length and max_length.
    """

    if message is None:
        message = f"Number length must be between {min_length} and {max_length} digits."

    def _number_length(form, field: Field):
        data = field.data
        if data is None:
            raise ValidationError(message)

        digits = str(data)
        if digits.startswith("+"):
            digits = digits[1:]

        if not digits.isdigit():
            raise ValidationError(message)

        length = len(digits)
        if length < min_length or length > max_length:
            raise ValidationError(message)

    return _number_length


class NumberLength:
    """
    Class-based validator.
    Validates that numeric value length (in digits) is between min_length and max_length.
    """

    def __init__(self, min_length: int, max_length: int, message: Optional[str] = None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = (
            message
            if message is not None
            else f"Number length must be between {min_length} and {max_length} digits."
        )

    def __call__(self, form, field: Field):
        data = field.data
        if data is None:
            raise ValidationError(self.message)

        digits = str(data)
        if digits.startswith("+"):
            digits = digits[1:]

        if not digits.isdigit():
            raise ValidationError(self.message)

        length = len(digits)
        if length < self.min_length or length > self.max_length:
            raise ValidationError(self.message)
