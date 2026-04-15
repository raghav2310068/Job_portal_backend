from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


class Users(models.Model):
    ROLE_CHOICES = (("recruiter", "Recruiter"),)

    name = models.CharField(max_length=50)

    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(regex=r"^[6-9]\d{9}$", message="Enter valid mobile number")
        ],
    )

    email = models.EmailField(unique=True)

    password = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8, message="Password should have at least 8 characters")
        ],
    )

    role = models.CharField(max_length=20, default="recruiter")

    def __str__(self):
        return self.email
