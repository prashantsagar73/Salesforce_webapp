from django.db import models

# Create your models here.

TITLE_CHOICES = (
    ('Mr', 'Mr'),
    ('Mrs.', 'Mrs'),
    ('Ms', 'Ms'),
)
# contact model for user details 
class Contact(models.Model):
    Title = models.CharField(choices=TITLE_CHOICES, max_length=19, blank=False, null=False)
    FirstName = models.CharField(max_length=255, blank=True, null=True)
    LastName = models.CharField(max_length=255, blank=False, null=False)
    Email = models.CharField(max_length=255, blank=False, null=False, unique=True)
    Phone = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.FirstName
