import os
import json
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save,pre_delete
from django.dispatch import receiver
from social_core.pipeline import user
from users.models import User
from product.models import Product
from config.settings import BASE_DIR
from datetime import datetime


def pre_save_products(sender, instance, **kwargs):
    print("before save product_data")


pre_save.connect(pre_save_products, sender=Product)


@receiver(post_save, sender=Product)
def post_save_products(sender, instance, created, **kwargs):
    if created:
        print(" After create product_data")
        subject = 'Product subject'
        message = 'Product message'
        from_email = 'abdulazizovasilbek872@gmail.com'
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(
            subject=subject,
            message = message,
            from_email = from_email,
            recipient_list = recipient_list,
            fail_silently = False
        )

@receiver(pre_delete, sender=Product)
def save_deleted_product(sender, instance, *args, **kwargs):
    current_date = datetime.now()

    filename = os.path.join(BASE_DIR, 'product\product_data', f'{instance.name}.json')
    product_data = {
        'id ': instance.id,
        'name': instance.name,
        'description': instance.description,
        'price': instance.price,
        'category': instance.category,
        'discount': str(instance.discount),
        'quantity': instance.quantity
    }
    with open(filename, mode='w') as f:
        json.dump(product_data, f, indent=4)


