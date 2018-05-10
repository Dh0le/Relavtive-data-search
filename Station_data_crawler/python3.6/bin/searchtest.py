import urllib.request
import os
import simplejson
import csv
import json
import time
import datetime
import subprocess

glob_la = 0
glob_lo = 0
result_bus = 0
result_subway = 0
sub_num = 0
bus_num = 0
count = 0
inputfilename = ''
outputfilename= ''
def manual():
    rawurl = "https://maps.googleapis.com/maps/api/place/nearbysearch/"
    filetype = input("Please enter 'xml' or 'json'\n")
    location = input("Please type in the location of station in format: 'Latitude,Longditude' \n")
    radius = input("Please enter the radius of search in meters (<=50000)\n")
    if int(radius) > 50000:
        print("Wrong input detected\n Exiting program\n")
        exit(1)
    locationtype = input("Please enter the type of places you want to search like restaurant\n")
    keyword = input("Please enter the keyword you want to search in places name\n")
    finalurl = rawurl + filetype + "?location=" + location + "&radius="+ radius + "&type=" + locationtype + "&keyword="+ keyword + "&key=AIzaSyAkQGdnrTiFJLPtnA9IHXCoTlsMj1xEFqU"
    filename = input("Please enter your target filename in format like .xml or .json\n")
    response = urllib.request.urlretrieve(finalurl, filename)
    try:
        response = urllib.request.urlretrieve(finalurl, filename)
    except (urllib.error.URLError) as e:
        print("Connection timeout, please try again later\n")

def takecsvinput():
	#let user to enter the filename they want to auto process.
	#read locations of each station in the file into global lists
	#double check the index before deplorement
    global glob_la
    global glob_lo
    global count
    global inputfilename
    global outputfilename
    global result_subway
    global result_bus
    inputfilename=input("Please enter the input filename in .csv format\n")#get the input filename to read
    outputfilename=input("Please enter the output filename in .csv format\n")#get the output filename to write



    count = len(open(inputfilename,'rU').readlines())#get the line number of  current open filename
    initial_value = 0
    glob_la = [ initial_value for i in range(count)] #inilized the global list before using
    glob_lo = [ initial_value for i in range(count)]
    result_bus = [ initial_value for i in range(count)]  #initilized the result list to write
    result_subway = [ initial_value for i in range(count)] #initilized the reuslt list to write
    with open(inputfilename) as f:
        reader = list(csv.reader(f))
        for x in range (0,count):
            glob_la[x] = reader[x][1]
            glob_lo[x] = reader[x][2]


def auto():
    rawurl = "https://maps.googleapis.com/maps/api/place/nearbysearch/"
    filetype = "json"
    radius = input("Please enter the radius of search in meters (<=50000)\n")
    if int(radius) > 50000:
        print("Wrong input detected\n Exiting program\n")
        exit(1)
    #change to global varibale mode to ready write-in
    global glob_lo
    global glob_la
    #bus part readin and download part here
    takecsvinput()
    for i in range (1,count):
        locationtype = "Bus station"
        location = str(glob_la[i])+','+str(glob_lo[i])
        print(location)
        finalurl = rawurl + filetype + "?location=" + location + "&radius="+ radius + "&type=" + locationtype + "&key=AIzaSyAkQGdnrTiFJLPtnA9IHXCoTlsMj1xEFqU"
        #response = urllib.request.urlretrieve(finalurl, "temp.json")
        try:
            response = urllib.request.urlretrieve(finalurl, "temp.json")
        except (urllib.error.URLError) as e:
            print("Connection timeout, please try again later\n")
            #process the data,write into ori file then delete the tempfile.
        data = json.load(open("temp.json"))
        bus_result_num = len(data["results"])
        result_bus[i] = bus_result_num

        locationtype = "Subway station"
        finalurl = rawurl + filetype + "?location=" + location + "&radius="+ radius + "&type=" + locationtype + "&key=AIzaSyBCbqJ9EJcRUn_I7mMGscbOnIWUkzGxXj8"
        try:
            response = urllib.request.urlretrieve(finalurl, "temp.json")
        except (urllib.error.URLError) as e:
            print("Connection timeout, please try again later\n")
        data = json.load(open("temp1.json"))
        sub_result_num = len(data["results"])
        result_subway[i] = sub_result_num
        write_out(inputfilename,outputfilename)



#TODO:This function needs to be modifed to be used.
def write_out(filename,targenemt):
    with open(filename,'r') as inputf:
        with open("csvtemp1.csv",'w') as outputf:
            writer = csv.writer(outputf,lineterminator='\n')
            reader = csv.reader(inputf)
            all = []
            row = next(reader)
            row.append("Bus_station_number")
            all.append(row)
            x = 0
            for row in reader:
                row.append(result_bus[x])
                all.append(row)
                x = x+1
            writer.writerows(all)
    with open("csvtemp1.csv",'r') as inputf:
        with open(targenemt,'w') as outputf:
            writer = csv.writer(outputf,lineterminator='\n')
            reader = csv.reader(inputf)
            all = []
            row = next(reader)
            row.append("Subway_station_number")
            all.append(row)
            x = 0
            for row in reader:
                row.append(result_subway[x])
                all.append(row)
                x = x+1
            writer.writerows(all)


def main():
	mode = input("Please enter 1 for auto and 2 for manual\n")
	if int(mode) == 1:
		auto()
	elif int(mode) == 2:
		manual()

main()