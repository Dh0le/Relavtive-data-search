import threading
import urllib.request
import os
import simplejson
import csv
import json
import time
import datetime
import subprocess
from threading import *


filecounter = 0
countlist = [0,0,0,0,0,0,0,0,0,0] #initialize the filelist to name the datafile.
datapath = os.path.abspath(os.curdir)
##def start_in():
  #  start_collect()
   # t = Timer(200, start_in())
    #t.start()
def filecount(): #start create or using exist filecount.txt for next step.
    global countlist
    path = datapath + '/filecount.txt'
    isExists = os.path.exists(path)
    if not isExists:
        file = open(path,'w')
        file.write(countlist)
        file.close()
        return True
    else:
        file = open(path,'r')
        tempstr = file.readlines()
        #print(tempstr[0])
        str = tempstr[0]
        str = str.lstrip('[')
        str = str.rstrip(']')
        templist = str.split(',')  
        i = 0
        for x in templist:
            countlist[i] = int(x)
            i+=1
        file.close()
        return False

def write_log(filepath):
    now=datetime.datetime.now()
    path = filepath+"log.txt"
    isExists = os.path.exists(path)
    if not isExists:
        file = open(path,'w')
        file.write(now.strftime('%Y-%m-%d %H:%M:%S'))
        file.write("\n")
        file.close()
        return True
    else:
        file = open(path,'a+')
        file.write(now.strftime('%Y-%m-%d %H:%M:%S'))
        file.write("\n")
        file.close()


def savecount(): #save the current file progress for next run. 
    global countlist
    path = datapath + '/filecount.txt'
    file = open(path, 'w')
    file.write(str(countlist))
    file.close()


def nestedlist2csv(list, out_file): #csv working part.
    with open(out_file, 'wb') as f:
        w = csv.writer(f)
        fieldnames=list[0].keys()  # solve the problem to automatically write the header
        w.writerow(fieldnames)
        for row in list:
            w.writerow(row.values())

def read_json(filename):             #read the json file downloaded by url link.
    return json.loads(open(filename).read())


def write_csv(data, filename):  #write the translated file into csv file formate. 
    with open(filename, 'w') as outf:
        dw = csv.DictWriter(outf, data[0].keys())
        dw.writeheader()
        for row in data:
            dw.writerow(row)


def write_time(filename,targenemt):
    now=datetime.datetime.now()
    with open(filename,'r') as inputf:
        with open(targenemt,'w') as outputf:
            writer = csv.writer(outputf,lineterminator='\n')
            reader = csv.reader(inputf)

            all = []
            row = next(reader)
            row.append('Download Time')
            all.append(row)

            for row in reader:
                row.append(now.strftime('%Y-%m-%d %H:%M:%S'))
                all.append(row)
            writer.writerows(all)
    os.remove(filename)




def mkdir(path): #createing a file folder for the city if it does not exist. 
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def chicago():
    global filecounter
    global countlist
    chicago_url = 'https://feeds.divvybikes.com/stations/stations.json' #static urllink for chicago station data. 
    myfilepath = datapath+'/Chicago_data' #local file path to store the data. 
    mkdir(myfilepath)
    filepath = myfilepath+"/Chicago_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(chicago_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['stationBeanList'] #acquire the data from its origninal array. 
    csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath+'/'+'chicago'+str(countlist[0]) +'.csv'
    countlist[0] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)

def boston():
    global filecounter
    global countlist
    boston_url = 'https://secure.thehubway.com/data/stations.json'
    myfilepath = datapath+'/Boston_data'
    mkdir(myfilepath)
    filepath = myfilepath + "/Boston_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(boston_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['stations'] #acquire the data .
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'Boston' + str(countlist[1]) + '.csv'
    countlist[1] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)


def los_angeles():
    global countlist
    la_url = 'https://gbfs.bcycle.com/bcycle_lametro/station_status.json'
    myfilepath = datapath + '/La_data'
    mkdir(myfilepath)
    filepath = myfilepath + "/LA_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(la_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['data']['stations']
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'La' + str(countlist[2]) + '.csv'
    countlist[2] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)


def bayarea():
    global  countlist
    Bay_url = 'http://feeds.bayareabikeshare.com/stations/stations.json'
    myfilepath = datapath + '/Bay_data'
    mkdir(myfilepath)
    filepath = myfilepath + "/Bay_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(Bay_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['stationBeanList']
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'Bay' + str(countlist[3]) + '.csv'
    countlist[3] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)

    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)


def NewYork():
    global countlist
    NY_url = 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json'
    myfilepath = datapath + '/NY_data'
    mkdir(myfilepath)
    filepath = myfilepath + "/NY_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(NY_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['data']['stations']
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'NY' + str(countlist[4]) + '.csv'
    countlist[4] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)


def Phi():
    phi_url = 'https://gbfs.bcycle.com/bcycle_indego/station_status.json'
    myfilepath = datapath + '/Phi_data'
    mkdir(myfilepath)
    filepath = myfilepath + "/Phi_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(phi_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['data']['stations']
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'Phi' + str(countlist[5]) + '.csv'
    countlist[5] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)

def Minnesota():
    Min_url = 'https://api-core.niceridemn.org/gbfs/fr/station_status.json'
    myfilepath = datapath + '/Min_data'
    mkdir(myfilepath)
    filepath = myfilepath + "/Min_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(Min_url, filepath)
    except (URLError,TimeoutError,OSError) as e:
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['data']['stations']
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'Min' + str(countlist[6]) + '.csv'
    countlist[6] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)

def DC():
    Dc_url = "https://gbfs.capitalbikeshare.com/gbfs/en/station_status.json"
    myfilepath = datapath + "/DC_data"
    mkdir(myfilepath)
    filepath = myfilepath + "/DC_Tempfile.json"
    try:
        response = urllib.request.urlretrieve(Dc_url, filepath)
    except (URLError,TimeoutError,OSError):
        write_log(myfilepath)
    fd = open(filepath)
    data1 = simplejson.load(fd)
    mylist = data1['data']['stations']
    csv_name = csv_name = myfilepath+'/'+'ori' + '.csv'
    target_name = myfilepath + '/' + 'DC' + str(countlist[7]) + '.csv'
    countlist[7] += 1
    try:
        write_csv(mylist,csv_name)
    except (ValueError,IndexError) as e:
        write_log(myfilepath)
    #write_time(csv_name,target_name)
    fd.close()
    os.remove(filepath)

def start_collect(event): #experimental timedelay function. ready for use.
    while not event.is_set():
        event.wait(timeout = 10)
        chicago()
        boston()
        los_angeles()
        bayarea()
        NewYork()
        Phi()
        Minnesota()
        #DC()


def main():
    filecount()
    i = datetime.datetime.now()
    while(i.minute%10 != 0):
        time.sleep(1)
        i = datetime.datetime.now()
    


    while True:
        chicago()
        boston()
        los_angeles()
        bayarea()
        NewYork()
        Phi()
        Minnesota()
        DC()
        savecount()
        time.sleep(600) #start working and getting file every 600 seconds. 


main()