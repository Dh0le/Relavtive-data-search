import glob
import os

datapath = "/depot/cai161/data/Bike_Share_Data/Station_data"
counterpath = datapath + '/filecount.txt'
outputpath = os.path.abspath(os.curdir) + "/aftermergeout/"
srcpath =  os.path.abspath(os.curdir)


def mchicago():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/Chicago_data/*.csv'
	csvx_list = glob.glob(input_path)
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
	print('write-in successful！')
	print('write-in complete！')


def mBay():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/Bay_data/*.csv'
	csvx_list = glob.glob(input_path)
	#csvx_list = glob.glob('/depot/cai161/data/Bike_Share_Data/Station_data/Bay_data/*.csv')
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
	print('write-in successful！')
	print('write-in complete！')


def mLA():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/La_data/*.csv'
	csvx_list = glob.glob(input_path)
	#csvx_list = glob.glob('/depot/cai161/data/Bike_Share_Data/Station_data/La_data/*.csv')
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
	print('write-in successful！')
	print('write-in complete！')


def mBoston():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/Boston_data/*.csv'
	csvx_list = glob.glob(input_path)
	#csvx_list = glob.glob('/depot/cai161/data/Bike_Share_Data/Station_data/Boston_data/*.csv')
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
    
	print('write-in successful！')
	print('write-in complete！')

def mMin():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/Min_data/*.csv'
	csvx_list = glob.glob(input_path)
	#csvx_list = glob.glob('/depot/cai161/data/Bike_Share_Data/Station_data/Min_data/*.csv')
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
	print('write-in successful！')
	print('write-in complete！')

def mNY():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/NY_data/*.csv'
	csvx_list = glob.glob(input_path)
	#csvx_list = glob.glob('/depot/cai161/data/Bike_Share_Data/Station_data/NY_data/*.csv')
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
	print('write-in successful！')
	print('write-in complete！')

def mPhi():
	var = input("Please enter the outputfilename:\n")
	opfilename = outputpath + var
	input_path = srcpath + '/Phi_data/*.csv'
	csvx_list = glob.glob(input_path)

	#csvx_list = glob.glob('/depot/cai161/data/Bike_Share_Data/Station_data/Phi_data/*.csv')
	print('%s csv files were founded\n'% len(csvx_list))
	print("Processing \n")
	for i in csvx_list:
		fr = open(i,'r').read()
		with open(opfilename,'a') as f:
			f.write(fr)
	print('write-in successful！')
	print('write-in complete！')



def main():
	var = input("Plese enter the number of city:\n 1 for Chicago\n 2 for Boston\n 3 for LA\n 4 for NewYork\n 5 for Phi\n 6 for Minisota\n 7 for BayArea\n")
	if var == '1':
		mchicago()
	elif var == '2':
		mBoston()
	elif var == '3':
		mLA()
	elif var == '4':
		mNY()
	elif var == '5':
		mPhi()
	elif var == '6':
		mMin()
	elif var == '7':
		mBay()
	else:
		printl("No input detected!!")


main()
