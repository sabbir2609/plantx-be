from django.db import models

from django.utils.translation import gettext_lazy as _


class UserRole(models.Model):
    role = models.CharField(
        max_length=100, help_text=_("Enter the name of the user role.")
    )
    description = models.TextField(
        help_text=_("Provide a description for the user role.")
    )


class User(models.Model):
    first_name = models.CharField(
        max_length=100, help_text=_("Enter the first name of the user.")
    )
    last_name = models.CharField(
        max_length=100, help_text=_("Enter the last name of the user.")
    )
    email = models.EmailField(help_text=_("Enter the email of the user."))
    password = models.CharField(
        max_length=100, help_text=_("Enter the password of the user.")
    )
    role = models.ForeignKey(
        UserRole, on_delete=models.CASCADE, help_text=_("Select the role for the user.")
    )
    image = models.ImageField(
        upload_to="users/", help_text=_("Upload an image for the user.")
    )
    phone = models.CharField(
        max_length=20, help_text=_("Enter the phone number of the user.")
    )
    address = models.TextField(help_text=_("Enter the address of the user."))
    city = models.CharField(max_length=100, help_text=_("Enter the city of the user."))
    country = models.CharField(
        max_length=100, help_text=_("Enter the country of the user.")
    )
    postal_code = models.CharField(
        max_length=20, help_text=_("Enter the postal code of the user.")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
