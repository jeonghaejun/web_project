from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('NAME', max_length=50)
    cpu = models.CharField('CPU', max_length=50)
    ram = models.CharField('RAM', max_length=20)
    gpu = models.CharField('GPU', max_length=50)
    battery = models.CharField('BATTERY', max_length=20)
    volume = models.CharField('VOLUME', max_length=20)
    weight = models.CharField('WEIGHT',max_length=20)
    display = models.DecimalField('DISPLAY', decimal_places=1,max_digits=3)
    maker = models.CharField('MAKER', max_length=50)
    sw_os = models.CharField('SW_OS', max_length=20, default='')
    price = models.CharField('PRICE', max_length=50)
    image = models.ImageField('IMAGE', blank=True)
    content = models.ImageField('CONTENT', blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url

class Maker_list(models.Model):
    maker_list = models.CharField(verbose_name='MAKER_LIST', max_length=50)

    def __str__(self):
        return self.maker_list

class Cpu_list(models.Model):
    manufacturer = models.CharField(verbose_name='MANUFACTURER', max_length=50)
    series = models.CharField(verbose_name='SERIES', max_length=20)
    generation = models.CharField(verbose_name='GENERATION', max_length=20)
    
    def __str__(self):
        return self.manufacturer

class Ram_list(models.Model):
    ram_weight = models.CharField(verbose_name='RAM_WEIGHT', max_length=50)

    def __str__(self):
        return self.ram_weight