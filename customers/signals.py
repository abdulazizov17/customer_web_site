import os
from datetime import datetime
import json
from django.core.mail import send_mail
from django.core.serializers import json
from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver

from config.settings import BASE_DIR
from customers.models import Customer


def pre_save_customer(sender, instance, *args, **kwargs):
    print('Before saving customer')


pre_save.connect(pre_save_customer, sender=Customer)

@receiver(post_save, sender=Customer)
def post_save_customer(sender, instance, created, **kwargs):
    if created:
        print("After saving customer")
        subject = 'Customer saved'
        message = f'{instance.full_name} saved'
        from_email = 'abdulazizovasilbek872@gmail.com'
        recipient_list = ['abdulazizovasilbek005@gmail.com']
        fail_silently = False
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=fail_silently

        )
@receiver(pre_delete, sender=Customer)
def save_delete_customer(sender, instance,*args, **kwargs):
    current_date = datetime.now()

    filename = os.path.join(BASE_DIR,'customers/customers_data',f'{instance.id}')
    customer_data = {
        'id':instance.id,
        'full_name' : instance.full_name,
        'email':instance.email,
        'phone':instance.phone,
        'address':instance.address,
        'image':instance.image,
    }
    with open(filename,mode='w')as f:
        json.dump(customer_data,f,indent=4)

    print('Customer successfully deleted')