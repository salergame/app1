from django.db import models

# Create your models here.
class Search(models.Model):
    address = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'search'
        verbose_name = 'Поиск'
        verbose_name_plural = 'Поиск'
    
    def __str__(self):
        return self.address