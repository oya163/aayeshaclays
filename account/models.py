from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import related
from iso import get_country_codes
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
        null=True,
        blank=True,
        default=None
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        null=True,
        blank=True,
        default=None        
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
        null=True,
        blank=True,
        default=None        
    )

    city = models.CharField(
        "City",
        max_length=1024,
        null=True,
        blank=True,
        default=None        
    )

    country = models.CharField(
        "Country",
        max_length=2,
        choices=get_country_codes(),
        default='US'
    )

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()