from django.urls import path
from goods import views

app_name='goods'

urlpatterns = [
<<<<<<< HEAD
    path('search/',views.catalog,name='search'),
=======
>>>>>>> 7203c0d3ca24d97ad35e4406b64f3838b5a5f355
    path('<slug:category_slug>/',views.catalog,name='index'),
    path('product/<slug:product_slug>/',views.product,name='product')
]
