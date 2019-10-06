#!/usr/bin/python
import bme280
import requests

temperature,pressure,humidity = bme280.readBME280All()

print "Temperature : ", temperature, "C"
print "Pressure : ", pressure, "hPa"
print "Humidity : ", humidity, "%"
