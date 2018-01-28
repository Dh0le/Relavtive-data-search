import urllib.request
import os
import simplejson
import csv
import json
import time
import datetime
import subprocess


def main():
	searchtype = input("Enter 1 to use general search\n Enter 2 to use percise search\n")
	if int(searchtype) == 1:
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
        #TODO: needs data process after download according to the type user chosed.s
    elif int(searchtype) == 2:
    	#use percise search interface and take input of locations id

    


main()