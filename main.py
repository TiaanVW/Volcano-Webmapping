import folium
import pandas
from folium.plugins import BeautifyIcon

data = pandas.read_csv("Volcanoes.txt")
map = folium.Map
map = folium.Map(location=[40.76,-110.89],
                 zoom_start = 6,
                 tiles="Stamen Terrain")
volc_fg = folium.FeatureGroup(name="Volcanoes")

lat =list(data["LAT"])
lon =list(data["LON"])
name =list(data["NAME"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br />
Height: %s m
"""

def color_picker(elevation):
    if (elevation > 1000.0) & (elevation < 2000.0):
        return "green"
    elif (elevation > 2000.0) & (elevation < 3000.0):
        return "orange"
    elif elevation > 3000.0:
        return "red"
    else:
        return "blue"

for x, y, name, elev in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (name, name, str(elev)), width=200, height=100)
    volc_fg.add_child(folium.CircleMarker(
        location=(x,y),
        popup=folium.Popup(iframe, parse_html=True),
        fill_color=color_picker(elev), color="grey",
        fill_opacity=0.8,
        radius=7)
                 )

pop_data=open("world.json", "r", encoding="utf-8-sig")

pop_fg = folium.FeatureGroup(name="Population")

pop_fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000  else "yellow"
                            if 1000000 <= x["properties"]["POP2005"] < 30000000 else "orange"
                            if 30000000 <= x["properties"]["POP2005"] < 50000000 else "red" }
                            )
             )

map.add_child(volc_fg)
map.add_child(pop_fg)
map.add_child(folium.LayerControl())

map.save("Volcanoes.html")

print(data)
