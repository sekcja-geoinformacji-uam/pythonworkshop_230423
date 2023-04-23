import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from funkcje.get import city_names, pollution_data
from funkcje.annotations import add_annotations

#wczytanie danych z pliku tekstowego
with open('dane.txt', 'r') as f:
    lines = f.readlines()
    coordinates = [[float(x) for x in line.strip().split(',')] for line in lines]

#wydzielenie dlugosci i szerokosci do osobnych list
x, y = [x[1] for x in coordinates], [y[0] for y in coordinates]

#dodawanie wartosci do listy: dwa sposoby
#1. list comprehension
city_names = [city_names(coord) for coord in coordinates]

#2. petla
poll_data = []
for coord in coordinates:
    pol_data = pollution_data(coord, 'pm10')
    poll_data.append(pol_data)

#utworzenie ramki danych z poprzednich list
df = pd.DataFrame({
    'miasto': city_names,
    'pm10': poll_data,
    "x": x,
    "y": y
})

#zamiana ramki danych w obiekt przestrzenny
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.x, df.y))
gdf.crs = "EPSG:4326"

#zmiana ukladu wspolrzednych pod dodanie podkladu mapowego
gdf_wm = gdf.to_crs(epsg=3857)

#tworzenie wydruku
ax = gdf_wm.plot()

#ustawienie bbox dla granic Polski
xmin = 1572152.3358098806
ymin = 6275208.094670648
xmax = 2687896.2767484677
ymax = 7330182.431316984

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_axis_off()

#dodanie etykiet dla punktow z kolumny z nazwami miast i wartosciami wskaznika
add_annotations(ax, gdf_wm, "miasto", move=60000)
add_annotations(ax, gdf_wm, "pm10", move=20000)

#dodanie podkladu
ctx.add_basemap(ax)

#wydruk mapy
plt.show()