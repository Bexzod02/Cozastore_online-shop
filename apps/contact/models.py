from django.db import models

# Create your models here.
class Contacts(models.Model):
    
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    