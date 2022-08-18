from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG


class Lead(models.Model):
    
    # SOURCE_CHOICE = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #      ('NewLetter', 'NewLetter')
        
    # )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # phoned = models.BooleanField(default=False)
    #  source = models.CharField(choices=SOURCE_CHOICE, max_length=100)
    
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FieldFile(blank=True)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email
    
    
    
    
