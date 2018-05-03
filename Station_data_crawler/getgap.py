import glob
import os
import time
import datetime
from time import mktime
from datetime import datetime

def getgap(string,city):
	#srcpath = os.path.abspath(os.curdir)
	input_path = string
	csvx_list = glob.glob(input_path)
	csvx_list.sort(key=os.path.getmtime)
	j = 0
	print("Start to process!!!!")
	for i in csvx_list:
		filemt = time.localtime(os.stat(csvx_list[j]).st_mtime)
		if j+1 == len(csvx_list):
			break
		filemt1 = time.localtime(os.stat(csvx_list[j+1]).st_mtime)
		datetime = FiletimeToDateTime(filemt)
		datetime1 = FiletimeToDateTime(filemt1)
		#print(datetime)
		#print(datetime1)
		result = datetime1 - datetime
		result1 = result.seconds/3600
		if result1 > 2 :
			write_log(city,datetime,datetime1)
		j += 1


def FiletimeToDateTime(ft):
    dt = datetime.fromtimestamp(time.mktime(ft))
    return dt

def write_log(city,time1,time2):
    path = "/depot/cai161/data/Bike_Share_Data/Station_data/Time_log/"+city + "Interval_log.txt"
    isExists = os.path.exists(path)
    file = open(path,'a')
    file.write(time1.strftime('%Y-%m-%d %H:%M:%S'))
    #print(time1.strftime('%Y-%m-%d %H:%M:%S'))
    file.write(" to ")
    file.write(time2.strftime('%Y-%m-%d %H:%M:%S'))
    #print(time2.strftime('%Y-%m-%d %H:%M:%S'))
    file.write("\n")
    file.write("\n")
    file.close()
    return True


def main():
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/Chicago_data/*.csv','Chicago_')
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/Bay_data/*.csv','Bay_')
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/La_data/*.csv','La_')
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/Boston_data/*.csv','Boston_')
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/Min_data/*.csv','Min_')
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/NY_data/*.csv','NY_')
	getgap('/depot/cai161/data/Bike_Share_Data/Station_data/Phi_data/*.csv','Phi_')


main()