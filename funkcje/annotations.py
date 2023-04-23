#ten plik zawiera funkcje sluzaca dodawaniu etykiet do wydruku


def add_annotations(ax, gdf, coldata, colgeom='geometry', move=40000):
    #dodaje etykiety do wydruku
    #ax - obiekt wydruku
    #gdf - przestrzenna ramka danych
    #colgeom - kolumna z geometria dla przestrzennej ramki danych gdf
    #move - wartosc liczbowa reprezentujaca przesuniecie
    #petla iterujaca po ramce danych 
    for _, row in gdf.iterrows():
        #pobranie wartosci x i y z kolumny geometry, 
        #dodanie przesuniecia do wspolrzednej y
        xy = (row[colgeom].x, row[colgeom].y + move)
        #utworzenie etykiet
        ax.annotate(text=row[coldata], xy=xy, ha='center')