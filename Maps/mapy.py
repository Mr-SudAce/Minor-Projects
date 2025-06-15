import folium
from folium.plugins import Search

# Initial map coordinates
lat = 40.6892
long = -74.0445
zoom = 2  # Zoomed out so you can see multiple locations

# Locations dictionary
locations = {
    'Kathmandu': [27.7172, 85.3240],
    # 'New York': [40.7128, -74.0060],
    # 'London': [51.5074, -0.1278],
    # 'Tokyo': [35.6762, 139.6503]
}

# Create map
m = folium.Map(location=[lat, long], zoom_start=zoom)

# Feature group for markers (needed for Search plugin)
marker_group = folium.FeatureGroup(name="Locations").add_to(m)

# Add markers to the feature group
for name, coord in locations.items():
    folium.Marker(
        location=coord,
        popup=name,
        tooltip=f"{name} - Click me!"
    ).add_to(marker_group)

# Add a search box for location names
Search(
    layer=marker_group,
    search_label='popup',  # Search by popup text (the location name)
    placeholder='Search for a location...',
    collapsed=False
).add_to(m)

# Save the map
m.save("searchable_map.html")
