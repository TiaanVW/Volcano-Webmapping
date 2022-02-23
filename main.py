import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
map = folium.Map
map = folium.Map(location=[40.76,-110.89], zoom_start = 6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Map")

lat =list(data["LAT"])
lon =list(data["LON"])
name =list(data["NAME"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br />
Height: %s m
"""

for x, y, name, elev in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fg.add_child(folium.Marker(location=(x,y), popup=folium.Popup(iframe, parse_html=True), icon=folium.Icon(color="blue")))

map.add_child(fg)

map.save("Gauteng.html")

print(data)
