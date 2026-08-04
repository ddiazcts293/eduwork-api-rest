from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core.validators import RegexValidator
from django.utils import timezone

# Validador de números de teléfono
phone_number_validator = RegexValidator(
    regex=r'^(\+?\d{1,3}-)?\d{3}-\d{3}-\d{4}$',
    message="Enter a valid phone number"
)

# Validador de nombres propios
@deconstructible
class NameValidator:
    def __call__(self, value):
        if any(char.isdigit() for char in value):
            raise ValidationError('Names cannot contain digits')

# Validador de edades con base en la fecha de nacimiento
class AgeValidator:
    def __init__(self, min_age=18, max_age=120):
        self.min_age = min_age
        self.max_age = max_age

    def __call__(self, value):
        today = timezone.now().date()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

        if age < self.min_age:
            raise ValidationError('Must be 18 years old to create an account')
        elif age > self.max_age:
            raise ValidationError('Enter a valid date of birth')
        return value
