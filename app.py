import os, datetime, re
import RPi.GPIO as GPIO

from flask import Flask, render_template, request, redirect, abort

import requests

from Adafruit_ADS1x15 import ADS1x15
from time import sleep

sensors = {
    2 : { 'name' : 'FSR 2', 'value' : 0 },
    3 : { 'name' : 'FSR 3', 'value' : 0 }
    }


app = Flask(__name__)
app.config['CSRF_ENABLED'] = False


def analogue():
    adc = ADS1x15()

    while True:
        for s in sensors:
		sensors[s]['value'] = adc.readADCSingleEnded(s)
        	sleep(.5)




@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")

    
    analogue()
    
    templateData = {
        'sensors': sensors
    }
    return render_template("main.html", **templateData)



if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 80, debug = True)







