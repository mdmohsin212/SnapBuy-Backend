from django.db import models
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        email_subject = f"User Contact with You"
        email_body = render_to_string('contact.html', {'user' : self})
            
        email = EmailMultiAlternatives(email_subject, '', to=['mohsin416m@gmail.com'])
        email.attach_alternative(email_body, "text/html")
        email.send()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username