#! /usr/bin/python

import json
import urllib2
import time
import os

def getWeather():	
	#weather from file (used in testing)
	#data = json.loads(dataFile.read())
	
	#weather from api ( https://api.forecast.io/forecast/19c800f33bf2003db19cc4aae7db507a/39.0932,-94.4156 )
	data = json.loads(urllib2.urlopen(" https://api.forecast.io/forecast/19c800f33bf2003db19cc4aae7db507a/39.0932,-94.4156").read())
	
	currentTemp = int(round(data['currently']['temperature']))
	currentIcon = data['currently']['icon']
	
	if currentIcon == 'clear-day' or currentIcon == 'clear-night' or currentIcon == 'wind':
		currentIcon = 'sun'
	elif currentIcon == 'cloudy' or currentIcon == 'partly-cloudy' or currentIcon == 'partly-cloudy-day' or currentIcon == 'partly-cloudy-night' or currentIcon == 'fog':
		currentIcon = 'clouds'
	elif currentIcon == 'rain':
		currentIcon = 'rain'
	elif currentIcon == 'snow' or currentIcon == 'sleet':
		currentIcon = 'snow'
	else:
		currentIcon = 'sun'
		
	
	dailyHigh = int(round(data['daily']['data'][0]['temperatureMax']))
	dailyIcon = data['daily']['data'][0]['icon']
	
	if dailyIcon == 'clear-day' or dailyIcon == 'clear-night' or dailyIcon == 'wind':
		dailyIcon = 'sun'
	elif dailyIcon == 'cloudy' or dailyIcon == 'partly-cloudy' or dailyIcon == 'partly-cloudy-day' or dailyIcon == 'partly-cloudy-night' or dailyIcon == 'fog':
		dailyIcon = 'clouds'
	elif dailyIcon == 'rain':
		dailyIcon = 'rain'
	elif dailyIcon == 'snow' or dailyIcon == 'sleet':
		dailyIcon = 'snow'
	else:
		dailyIcon = 'sun'
	
	if currentTemp < 0:
		currentTemp = 0
	elif currentTemp > 100:
		currentTemp = 100
	
	if dailyHigh < 0:
		dailyHigh = 0
	elif dailyHigh > 100:
		dailyHigh = 100
		
	showForecast = False #GPIO.input(switch)
	
	if showForecast:
		displayWeather(dailyHigh, dailyIcon)
	else:
		displayWeather(currentTemp, currentIcon)
		
def displayWeather(temp, icon):
	# servo control here for temp and conditions display
	print temp, icon
	
	
def getSpeed():
	print('getting connection speed...')
	os.system("python speedtest.py > speed.txt")
	dataFile = file("speed.txt", "r")
	data = dataFile.read()
	speed = int(round(float(data[data.find("Download: ") + len("Download: "):data.find("Testing upload speed")].split(" ")[0])))
	
	if speed < 0:
		speed = 0
	elif speed > 100:
		speed = 100
		
	displaySpeed(speed)
	
def displaySpeed(speed):
	# servo control here for speed display
	print(speed)


getWeather()
getSpeed()
#time.sleep(10)