from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def home(request):
    if request.method == "POST":
        city = request.POST["city"].upper()
        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e4f4965a6360a7b17caeb95e9706f66f").read()
        response = json.loads(source)
        data = {
            "country_code": str(response["sys"]["country"]),
            "coordinate": str(response["coord"]["lon"]) + "°" + " - " + str(response["coord"]["lat"]) + "°",
            "temperature": str(response["main"]["temp"]) + "k",
            "pressure": str(response["main"]["pressure"]) + "pa",
            "humidity": str(response["main"]["humidity"]) + "g.m-3",
        }
    else:
        data = {}
        city = ""
    return render(request, "index.html", {"city":city, "data":data})