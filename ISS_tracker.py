# Project from: https://projects.raspberrypi.org/en/projects/where-is-the-space-station
# Verification: https://spotthestation.nasa.gov/tracking_map.cfm

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
    print(p['name'], 'in', p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# University Commons, Chapel Hill
lat = 35.896902
lon = -79.074937

location = turtle.Turtle()
location.penup()
location.color('turquoise')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
# print over

style = ('Arial', 8, 'bold')
location.write(time.ctime(over), font=style)

# forces the program to wait for me to type something before closing. (the python function and the turtle function)
# input()
# turtle.exitonclick()

turtle.done()
