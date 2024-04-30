from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import folium
from folium import plugins
from delivery.forms import SearchForm
from orders.models import Order, OrderItem
import geocoder
from django.http import HttpResponse

from delivery import getroute

from delivery.models import Search
# Create your views here.

@login_required
def show_map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_entry = form.save(commit=False)
            search_entry.user = request.user
            search_entry.save()
            return redirect('/delivery/showmap/')
    else:
        form = SearchForm()
    
    # Извлекаем последнюю точку для текущего пользователя
    last_search = Search.objects.filter(user=request.user).last()
    if last_search:
        address = last_search.address
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
        
        if lat is None or lng is None:
            last_search.delete()
            return HttpResponse('Вы ввели неправильный адрес')
    else:
        lat = 51.1308  
        lng = 71.4331  
        address = '' 
    
    min_lon, max_lon = 72.2461, 70.9442
    min_lat, max_lat = 51.4610, 50.8907
    
    m = folium.Map(
        max_bounds=True,
        location=[lat, lng],  # Используем координаты последней точки или значения по умолчанию
        zoom_start=10,
        min_lat=min_lat,
        max_lat=max_lat,
        min_lon=min_lon,
        max_lon=max_lon,
    )

    
    # folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(m)
    # folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(m)
    # folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(m)
    # folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(m)
    
    plugins.LocateControl(
        auto_start=False,
        strings={"title": "Посмотреть свое место нахождение", "popup": "Ваша позиция"},
    ).add_to(m)
    
    plugins.Fullscreen(
        position="topright",
        title="Развернуть",
        title_cancel="Выйти",
        force_separate_button=True,
    ).add_to(m)
    
    folium.Marker(
        [lat, lng],
        tooltip='Нажми на меня',
        popup=address
    ).add_to(m)
    
    shop_location = [51.0910, 71.4180]
    folium.Marker(
        location=shop_location,
        popup='Магазин мебели HOME'
    ).add_to(m)
    
    route_info = getroute.get_route(lng, lat, shop_location[1], shop_location[0])
    route = route_info['route']
    
    folium.PolyLine(route, color="blue", weight=2.5, opacity=1).add_to(m)
    
    has_paid_orders = Order.objects.filter(user=request.user, is_paid=True).exists()
    
    payment_on_get_orders = Order.objects.filter(user=request.user, payment_on_get=True).exists()
    
    m = m._repr_html_()
    test=True
    context = {
        'm': m,
        'form': form,
        'has_paid_orders':has_paid_orders,
        'payment_on_get_orders':payment_on_get_orders,
        'test': test,
    }
    
    return render(request, 'delivery/show_map.html', context)
