from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Product(models.Model):
    name = models.CharField('NAME', max_length=50)
    cpu = models.CharField('CPU', max_length=50)
    ram = models.CharField('RAM', max_length=20)
    gpu = models.CharField('GPU', max_length=50)
    battery = models.CharField('BATTERY', max_length=20)
    volume = models.CharField('VOLUME', max_length=20)
    weight = models.DecimalField('WEIGHT', decimal_places=3, max_digits=4)
    display = models.DecimalField('DISPLAY', decimal_places=1, max_digits=3)
    maker = models.CharField('MAKER', max_length=50)
    sw_os = models.CharField('SW_OS', max_length=20, default='')
    price = models.IntegerField('PRICE')
    image = models.ImageField('IMAGE', blank=True)
    content = models.ImageField('CONTENT', blank=True)

    tags = TaggableManager(blank=True)

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
    cpu_list = models.CharField(
        verbose_name='CPU_LIST', max_length=50, default='')

    def __str__(self):
        return self.cpu_list


class Ram_list(models.Model):
    ram_volume = models.CharField(
        verbose_name='RAM_VOLUME', max_length=20, default='')

    def __str__(self):
        return self.ram_volume


class Gpu_list(models.Model):
    gpu_list = models.CharField(
        verbose_name='GPU_LIST', max_length=50, default='')

    def __str__(self):
        return self.gpu_list


class Ssd_list(models.Model):
    ssd_volume = models.CharField(
        verbose_name='SSD_VOLUME', max_length=20, default='')

    def __str__(self):
        return self.ssd_volume


class Os_list(models.Model):
    os_list = models.CharField(
        verbose_name='OS_LIST', max_length=20, default='')

    def __str__(self):
        return self.os_list


class Display_list(models.Model):
    display_list = models.IntegerField(verbose_name='DISPLAY_LIST', default='')

    def __str__(self):
        return str(self.display_list)


class Weight_list(models.Model):
    weight_list = models.IntegerField(verbose_name='WEIGHT_LIST', default='')

    def __str__(self):
        return str(self.weight_list)
