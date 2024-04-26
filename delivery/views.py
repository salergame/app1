from django.shortcuts import render,redirect
import folium
from folium import plugins
from delivery.forms import SearchForm
import geocoder
from django.http import HttpResponse
import requests
import polyline
from delivery import getroute
from folium.plugins.geocoder import Geocoder

from delivery.models import Search
# Create your views here.
def show_map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/delivery/showmap/')
    else:
        form = SearchForm()
    
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    
    if lat is None or lng is None:
        address.delete()
        return HttpResponse('Вы ввели неправильный адрес')
    
    min_lon, max_lon = 85, 50
    min_lat, max_lat = 55, 40
    
    m = folium.Map(
        max_bounds=True,
        location=[51.1308,71.4331],
        zoom_start=10,
        min_lat=min_lat,
        max_lat=max_lat,
        min_lon=min_lon,
        max_lon=max_lon,
    )

    
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
    
    m = m._repr_html_()
    
    context = {
        'm': m,
        'form': form,
    }
    
    return render(request, 'delivery/show_map.html', context)
