from django.shortcuts import render, get_object_or_404
from promo.models import RadioStation


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def home_radio(request):
    list_radio = RadioStation.objects.all()
    return render(request, 'all_radio.html', {'list_radio': list_radio})


def radio_page(request, name):
    lower_name = name.lower().title()
    radio = get_object_or_404(RadioStation, name_en=lower_name)
    return render(request, 'radio_page.html', {'radio': radio})
