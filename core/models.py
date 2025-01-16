import pyotp
from django.db import models
from django.contrib.auth.models import AbstractUser


class MFAUser(AbstractUser):
    """Custom User model with 2fa attributes for google authenticator"""

    is_two_fa_enabled = models.BooleanField(default=True)
    two_fa_secrate = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def generate_random_secrate(self):
        """Generate a random secret for 2fa"""
        self.secrate = pyotp.random_base32()
        self.two_fa_secrate = self.secrate
        self.save()

    def verify_two_fa_code(self, two_fa_code):
        """Verify 2fa code"""
        totp = pyotp.TOTP(self.two_fa_secrate)
        return totp.verify(two_fa_code)
