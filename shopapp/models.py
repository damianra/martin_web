from django.db import models
from django.utils.text import slugify
from jsonfield import JSONField


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return '%s' % self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.lower().replace(' ', '-'))
        super(Category, self).save(*args, **kwargs)

# Product Model
class Product(models.Model):
    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Agotado = 'Agotado'
    ESTADO = (
        (Borrador,'Borrador'),
        (Publicado, 'Publicado'),
        (Agotado, 'Agotado'),
    )

    name = models.CharField(max_length=300)
    picture = models.FileField(upload_to='img_products', default='default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100,blank=True)
    oferta = models.BooleanField(default=False, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO, default='Borrador')
    price = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.lower().replace(' ', '-'))
        super(Product, self).save(*args, **kwargs)

class Promo(models.Model):
    name = models.CharField(max_length=200)
    picture = models.FileField(upload_to='img_products', default='default.jpg')
    data = JSONField()
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s' % self.name


class BussinesData(models.Model):
    name = models.CharField(max_length=300)
    logo = models.FileField(upload_to='img_logo', default='default.jpg')
    instagram = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    mail = models.CharField(max_length=300)
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.name