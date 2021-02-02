from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField('NAME', max_length=50)
    cpu = models.CharField('CPU', max_length=50)
    ram = models.IntegerField('RAM')
    gpu = models.CharField('GPU', max_length=50)
    battery=models.IntegerField('BATTERY')
    volume = models.IntegerField('VOLUME')
    weight = models.DecimalField('WEIGHT',decimal_places=2,max_digits=4)
    display = models.DecimalField('DISPLAY', decimal_places=1,max_digits=3)
    maker = models.CharField('MAKER', max_length=50)
    sw_os = models.CharField('SW_OS', max_length=20, default='')
    price = models.IntegerField('PRICE')
    image = models.ImageField('IMAGE',upload_to='product/', blank=True)
    content = models.TextField('CONTENT')
    
    def __str__(self):
        return self.name