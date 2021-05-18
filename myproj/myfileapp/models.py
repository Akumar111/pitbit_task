from django.db import models

# Create your models here.


class myuploadfile(models.Model):
    myfiles = models.FileField(upload_to="")
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.info
