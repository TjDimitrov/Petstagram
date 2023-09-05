from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


def send_successful_registration_email(user):
    send_mail(
        subject='Registration successful!',
        message='It works!',
        from_email='info@petstagram.com',
        recipient_list=('tjdimitrovv@gmail.com',)
    )


@receiver(post_save, sender=UserModel)
def user_created(*args, **kwargs):
    send_successful_registration_email(None)
