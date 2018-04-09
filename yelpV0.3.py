# -*- coding: utf-8 -*-
"""
Yelp Fusion API code sample.
This program demonstrates the capability of the Yelp Fusion API
by using the Search API to query for businesses by a search term and location,
and the Business API to query additional information about the top result
from the search query.
Please refer to http://www.yelp.com/developers/v3/documentation for the API
documentation.
This program requires the Python requests library, which you can install via:
`pip install -r requirements.txt`.
Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import csv
import numpy
import urllib



try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode



API_KEY= "57EBwb8evSlYVWBevjZkIk9PSD5HJU6xE9ofdNYaM5I7H49mLQr_6A6sWvnBuLlPpFyyd6pBRoNDpa41X1b9wCCWohpXl8B1ucKev2BZC2D6BI8B0agi6i-DVx2WWnYx"


# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

sriptname = ''
# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 50
glob_la = 0
glob_lo = 0
result_rating = 0
result_r_count = 0
result_price = 0
std_rating = 0
std_price = 0
std_r_count = 0
price = 0
rating = 0
r_count = 0
b_count = 0
count = 0
scriptname = ''
term = ''

def takecsvinput():
    #let user to enter the filename they want to auto process.
	#read locations of each station in the file into global lists
	#double check the index before deplorement
    global glob_la
    global glob_lo
    global count
    global inputfilename
    global outputfilename
    global cityname
    global station_id
    global price
    global r_count
    global rating
    global radius
    global constumkey
    global  std_rating
    global std_price
    global std_r_count
    global  result_price
    global  result_rating
    global  result_r_count
    file = open(scriptname,"r")
    inputfilename = file.readline().rstrip('\n')
    outputfilename = file.readline().rstrip('\n')
    cityname = file.readline().rstrip('\n')
    radius = file.readline().rstrip('\n')
    if int(radius) > 50000:
        print("Wrong input detected\n Exiting program\n")
        exit(1)
    term = file.readline().rstrip('\n')
    constumkey = file.readline().rstrip('\n')
    count = len(open(inputfilename,'rU').readlines())#get the line number of  current open filename
    initial_value = 0
    glob_la = [ initial_value for i in range(count)] #inilized the global list before using
    glob_lo = [ initial_value for i in range(count)]
    rating = [ initial_value for i in range(50)]
    price = [ initial_value for i in range(50)]
    r_count = [ initial_value for i in range(50)]
    result_r_count = [ initial_value for i in range(count)]
    result_rating = [ initial_value for i in range(count)]
    result_price = [ initial_value for i in range(count)]
    std_price = [ initial_value for i in range(count)]
    std_r_count = [ initial_value for i in range(count)]
    std_rating = [ initial_value for i in range(count)]

    station_id = [ initial_value for i in range(count)]
    with open(inputfilename) as f:
        reader = list(csv.reader(f))
        for x in range (0,count):
            glob_la[x] = reader[x][1]
            glob_lo[x] = reader[x][2]
            station_id[x] = reader[x][0]


def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, latitude,longtidue):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'latitude': longtidue,
        'longtitude':longtidue,
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(term,latitude,longtitude):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    global price
    global rating
    global  r_count
    global b_count
    response = search(API_KEY, term, latitude,longtitude)
    
    with open("test.json", "w") as fd:
        json.dump(response,fd)

    businesses = response.get('businesses')
    if not businesses:
        print(u'No businesses for {0} in {1},{2} found.'.format(term, latitude,longtitude))
        return

    business_id = businesses[1]['id']
    b_count = len(businesses)
    for x in range (0,b_count):
        if businesses[x]['price'] == "$":
            price[x] = 1
        elif businesses[x]['price'] == "$$":
            price[x] = 2
        elif businesses[x]['price'] == "$$$":
            price[x] = 3
        elif businesses[x]['price'] == "$$$$":
            price[x] = 4
        rating[x] = businesses[x]['review']
        r_count[x] = businesses[x]['review_count']


    #print(u'{0} businesses found, querying business info ' \
     #   'for the top result "{1}" ...'.format(
      #      len(businesses), business_id))
    #response = get_business(API_KEY, business_id)

    #print(u'Result for business "{0}" found:'.format(business_id))
    #pprint.pprint(response, indent=2)


def main():
    for i in range (0,count):
        try:
            query_api(term,glob_la[i],glob_lo[i])
        except HTTPError as error:
            sys.exit(
                'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                    error.code,
                    error.url,
                    error.read(),
                )
            )
        result_r_count[i] = sum(result_r_count)/float(len(b_count))
        result_price[i] = sum(result_price) / float(len(b_count))
        result_rating[i] = sum(result_rating)/float(len(b_count))
        data1 = numpy.array(result_rating)
        data2 = numpy.array(result_price)
        data3 = numpy.array(result_r_count)
        std_price[i] = numpy.std(data2)
        std_rating[i] = numpy.std(data1)
        std_r_count[i] = numpy.std(data3)



if __name__ == '__main__':
    main()