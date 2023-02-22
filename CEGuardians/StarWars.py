import requests
import csv

url = "https://swapi.dev/api/planets/?page=1"

planets = []

while url:
    response = requests.get(url)
    data = response.json()
    planets += data["results"]
    url = data["next"]

cleaned_planets = []
for planet in planets:
    if all(val is not None and val != "unknown" for val in [planet.get(field) for field in ["diameter", "gravity", "climate", "population"]]):
        cleaned_planets.append({
            "name": planet["name"],
            "diameter": planet["diameter"],
            "gravity": planet["gravity"],
            "climate": planet["climate"],
            "population": planet["population"]
        })

with open("cleaned_planets.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "diameter", "gravity", "climate", "population"])
    writer.writeheader()
    for planet in cleaned_planets:
        writer.writerow(planet)