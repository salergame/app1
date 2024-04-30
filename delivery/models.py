from django.db import models
from users.models import User
# Create your models here.
class Search(models.Model):
    address = models.CharField(max_length=200,null=True,verbose_name='Адрес')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Время поиска')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,verbose_name='пользователь')
    
    class Meta:
        db_table = 'search'
        verbose_name = 'Поиск'
        verbose_name_plural = 'Поиск'
    
    def __str__(self):
        return self.address
    
class Cart(models.Model):
    cart_number = models.IntegerField()
    validity = models.DateField()
    cvv = models.IntegerField(max_length=3)
    Owner = models.CharField(max_length=200)