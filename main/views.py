from django.shortcuts import render
from django.views import View

from . import api
class WeatherView(View):
    template = 'main/weather.html'
    def get(self, request):
        return render(request, self.template, {})


    def post(self, request):
        city = request.POST.get('city')
        city = city[0].upper() + city[1:].lower()
        weather = api.get_weather(city)

        if weather:
            return render(request, self.template, {'weather': weather})

        return render(request, self.template, {'errors': 'Please enter correct city'})

