import csv
import pandas as pd

rows = []

with open('bright_stars.csv', 'r') as f:
    csv_r = csv.reader(f)
    for row in csv_r:
        rows.append(row)

headers = rows[0]
stars_data = rows[1:]
headers[0] = 'Index'

star_data = []

for star_name in stars_data:
    if star_name[3] != '?': 
        star_name[3] = float(star_name[3].strip("\'"))*1.989e+30
    
    if star_name[4] != '?':
        star_name[4] = float(star_name[4].strip("\'"))*6.957e+8
    star_data.append(star_name)

gravity_data = []

for star_name in star_data:
    if star_name[3] != '?' and star_name[4] != '?':
        gravity = (6.674e-11 * float(star_name[3]))/(float(star_name[4])*float(star_name[4]))
    star_name.append(gravity)
    gravity_data.append(star_name)

name = []
distance = []
mass = []
radius = []
gravity = []

for row in gravity_data:
    name.append(row[1])
    distance.append(row[2])
    mass.append(row[3])
    radius.append(row[4])
    gravity.append(row[5])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)

df.to_csv('main.csv')