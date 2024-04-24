from django.shortcuts import render
import folium
# Create your views here.
def show_map(request):
    min_lon, max_lon = 85, 50
    min_lat, max_lat = 55, 45
    m = folium.Map(
        max_bounds=True,
        location=[48.39779862449,70.192611690145],
        zoom_start=4.4,
        min_lat=min_lat,
        max_lat=max_lat,
        min_lon=min_lon,
        max_lon=max_lon,
    )

    m = m._repr_html_()
    context= {
        'm':m,
    }
    return render(request,'delivery/show_map.html',context)
    
