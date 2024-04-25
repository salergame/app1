from django.shortcuts import render,redirect
import folium
from delivery.forms import SearchForm
import geocoder
from django.http import HttpResponse

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
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Вы ввели неправильный аддрес')
    
    min_lon, max_lon = 85, 50
    min_lat, max_lat = 55, 40
    m = folium.Map(
        max_bounds=True,
        location=[48.39779862449,70.192611690145],
        zoom_start=4.4,
        min_lat=min_lat,
        max_lat=max_lat,
        min_lon=min_lon,
        max_lon=max_lon,
    )
    folium.Marker([lat,lng],tootlip='Нажми на меня',
                  popup=address).add_to(m)
    # folium.CircleMarker([max_lat, min_lon], tooltip="Upper Left Corner").add_to(m)
    # folium.CircleMarker([min_lat, min_lon], tooltip="Lower Left Corner").add_to(m)
    # folium.CircleMarker([min_lat, max_lon], tooltip="Lower Right Corner").add_to(m)
    # folium.CircleMarker([max_lat, max_lon], tooltip="Upper Right Corner").add_to(m)
    m = m._repr_html_()
    context= {
        'm':m,
        'form':form,
    }
    return render(request,'delivery/show_map.html',context)
    
