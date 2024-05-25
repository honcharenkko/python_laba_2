from django.db import models


class Skils(models.Model):
    tittle= models.CharField('Name', max_length=50)
    
    def __str__(self):
        return self.tittle
    
    
class Image(models.Model):
    title = models.CharField('Name', max_length=50)
    image = models.ImageField('Image', upload_to='img')

    def __str__(self):
        return self.title