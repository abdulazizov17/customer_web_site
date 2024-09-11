import os
from config.settings import BASE_DIR
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
import json
from app.models import Author
from product.models import Product
from users.models import User
from datetime import datetime


def pre_save_author(sender,instance,*args,**kwargs):
    print('Before saving app')

pre_save.connect(pre_save_author,sender=Author)

@receiver(post_save, sender=Author)
def post_save_author(sender, instance, created, *args, **kwargs):
    if created:
        print('After saving author')
        subject = 'Author saved'
        message = f'{instance.full_name} has been created recently'
        from_email = 'abdulazizovasilbek872@gmail.com'
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False
        )



