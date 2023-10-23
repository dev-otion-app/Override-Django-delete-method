from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import AppModel
from .utils import delete_images


@receiver(post_delete, sender=AppModel)
def appmodel_delete_images(sender, **kwargs):
    delete_images('/media/'+kwargs['instance'].image.name)
