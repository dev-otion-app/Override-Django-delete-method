from django.db import models
##from .utils import delete_images

class AppModel(models.Model):
    name = models.CharField(max_length = 250)
    image = models.ImageField(default = None)

    """ 
    Uncomment this to try the overrided method. It's important to disable the signal as in this case we don't want to use it.
        def delete(self):
        delete_images('/media/'+self.image.name)
        return super().delete()
    """
    

    def __str__ (self):
        return self.name