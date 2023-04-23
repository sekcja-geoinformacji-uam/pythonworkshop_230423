import os
import requests
import json
from dotenv import load_dotenv

#ten plik zawiera wydzielone funkcje do pozyskania wartosci z dwoch wybranych API,
#HERE oraz OpenWeather. 

#wczytanie zmiennych srodowiskowych z pliku .env
#zawieraja klucze do API
load_dotenv()
here_api_key = os.getenv("HERE_API_KEY")
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")


def city_names(coordinates):
    #pozyskuje wartosc nazwy miasta dla podanych wspolrzednych
    #coordinates - lista zlozona z dwoch wartosci, x i y
    url = f"https://revgeocode.search.hereapi.com/v1/revgeocode?at={coordinates[0]}%2C{coordinates[1]}&lang=en-US&apiKey={here_api_key}"
    #otrzymany z zapytania tekst konwertowany jest do formy slownika
    response = requests.get(url)
    data = json.loads(response.text)
    #pozyskanie nazwy miasta ze slownika przy wykorzystaniu kolejnych zagniezdzonych kluczy
    city_name = data['items'][0]['address']['city']
    #zwracanie nazwy miasta
    return city_name

def pollution_data(coordinates, index):
    #pozyskuje wartosc indeksu zanieczyszczenia powietrza
    #wybranego przez uzytkownika dla podanych wspolrzednych
    #coordinates - lista zlozona z dwoch wartosci, x i y
    #index - tekst reprezentujacy wybrany wskaznik 
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={coordinates[0]}&lon={coordinates[1]}&appid={openweather_api_key}'
    #otrzymany z zapytania tekst konwertowany jest do formy slownika
    response = requests.get(url)
    data = json.loads(response.text)
    #pozyskanie nazwy miasta ze slownika przy wykorzystaniu kolejnych zagniezdzonych kluczy
    pollution_data = data['list'][0]['components'][index]
    #zwracanie wartosci indeksu
    return pollution_data