import urllib.request
import os
import simplejson
import csv
import json
import time
import datetime
import subprocess


def main():
    rawurl = "https://maps.googleapis.com/maps/api/place/nearbysearch/"
    filetype = input("Please enter 'xml' or 'jason'\n")
    location = input("Please type in the location of station in format: 'Latitude,Longditude' \n")
    radius = input("Please enter the radius of search in meters (<=50000)\n")
    if int(radius) > 50000:
        print("Wrong input detected\n Exiting program\n")
        exit(1)
    locationtype = input("Please enter the type of places you want to search like restaurant\n")
    keyword = input("Please enter the keyword you want to search in places name\n")
    finalurl = rawurl + filetype + "?location=" + location + "&radius="+ radius + "&type=" + locationtype + "&keyword="+ keyword + "&key=AIzaSyBCbqJ9EJcRUn_I7mMGscbOnIWUkzGxXj8"

    filename = input("Please enter the filename you want in format:'Filename.xml' or 'Filename.json'\n")
    try:
        response = urllib.request.urlretrieve(finalurl, filename)
    except (URLError,TimeoutError,OSError) as e:
        print("Connection timeout, please try again later\n")


main()