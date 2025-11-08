# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Email,
    InputRequired,
    NumberRange,
    Optional,
)

from validators import number_length, NumberLength


class RegistrationForm(FlaskForm):
    # email: text, required, email format
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email format."),
        ],
    )

    # phone: number, required, 10 digits, only positive
    phone = IntegerField(
        "Phone",
        validators=[
            InputRequired(message="Phone is required."),
            NumberRange(min=0, message="Phone must be a positive number."),
            number_length(10, 10, message="Phone must contain exactly 10 digits."),
        ],
    )

    # name: text, required
    name = StringField(
        "Name",
        validators=[DataRequired(message="Name is required.")],
    )

    # address: text, required
    address = StringField(
        "Address",
        validators=[DataRequired(message="Address is required.")],
    )

    # index: only numbers, required
    index = IntegerField(
        "Index",
        validators=[
            InputRequired(message="Index is required."),
            NumberRange(min=0, message="Index must be a positive number."),
        ],
    )

    # comment: text, optional
    comment = TextAreaField(
        "Comment",
        validators=[Optional()],
    )

    # example of class-based validator usage (not required, but exists for Task 2):
    # alt_phone = IntegerField(
    #     "Alt phone",
    #     validators=[
    #         InputRequired(),
    #         NumberLength(10, 10, message="Alt phone must contain exactly 10 digits."),
    #     ],
    # )
