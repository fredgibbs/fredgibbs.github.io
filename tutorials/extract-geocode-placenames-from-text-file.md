---
layout: post 
title: Extract and Geocode Placenames from a Text File
date: 2012-10-12 00:00:00
category: tutorial
---

This tutorial explains how to write a python script to parse a text file with placenames and geolocate them (get latitude and longitude coordinates). It covers how to send requests to the Google Geocoding API and process the JSON response that it returns.

This kind of script can be extraordinarly beneficial in making a quick map of places from a list of places that you've been recording.  

---

If you have a list of places you'd like to visualize on a map, one crucial first step is to find the latitude and longitude coordinates for those places. A number of mapping tools or websites can do this for you---behind the scenes---in the process of putting dots on a map for you. But there are many limitations to relying on other tools to do the geocoding for you. (1) Most do not scale very well. Many free services will only geolocate around 100 points for you at a time. (2) Geocoding the places yourself also gives you the chance to fix any places that are difficult to geolocate, or simply find the coordinate yourself as needed. (3) With free services, rarely do you get the actual coordinates of the places that you can resuse with other tools. You'll have far more flexibility in what the kinds of maps you can create if you can find and record the geographic coordinates for your places yourself. With a little bit of python scripting, it's rather straightforward.

To find coordinates for a place, we can use an Application Programming Inferface (API). Just as when you type in Google.com to your URL bar in your browser and you get the familiar Google search page, you can use an API the same way. But instead of getting a webpage, you get information that you requested via the URL. We are going to use the [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/). To use it, we need to send it a request like

{% highlight python %}
http://maps.googleapis.com/maps/api/geocode/json?address=Albuqueruque+NM&sensor=false
{% endhighlight %}

For now, plug that URL into your browser's URL bar to see the result. This is equivalent to "making a request" to the API. You can see that the response sent from the server is plaintext (there is no formatting like a nice looking webpage would have), but it is nicely organized using Javascript Object Notation (JSON). Glancing through it, you can see it contains a lot of potentially useful information.

{% highlight python %}
{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "Albuquerque",
               "short_name" : "Albuquerque",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Bernalillo County",
               "short_name" : "Bernalillo County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "New Mexico",
               "short_name" : "NM",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            }
         ],
         "formatted_address" : "Albuquerque, NM, USA",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 35.2180539,
                  "lng" : -106.4711629
               },
               "southwest" : {
                  "lat" : 34.9467659,
                  "lng" : -106.881796
               }
            },
            "location" : {
               "lat" : 35.110703,
               "lng" : -106.609991
            },
            "location_type" : "APPROXIMATE",
            "viewport" : {
               "northeast" : {
                  "lat" : 35.2180539,
                  "lng" : -106.4711629
               },
               "southwest" : {
                  "lat" : 34.9467659,
                  "lng" : -106.881796
               }
            }
         },
         "types" : [ "locality", "political" ]
      }
   ],
   "status" : "OK"
}
{% endhighlight %}


Python makes it very easy to send API requests (like the one above) and to process the results, especially when using the [requests module](http://docs.python-requests.org/en/latest/). (You may want to read about [installing python modules](../tutorials/install-python-modules "installing python modules").) A simple example of making a request in python looks like

{% highlight python %}
r = requests.get(URL, params=DICTIONARY)
{% endhighlight %}

In this case, our **URL** will be the base URL of the Google Geocoding API (as stated above). For our **DICTIONARY**, we have to create a [python dictionary](http://www.tutorialspoint.com/python/python_dictionary.htm) that will hold at least two bits of information that the API expects us to send: **address** (in this case our place name), and **sensor** (which the API requires to be set to true or false). The code to make the request will look like

{% highlight python %}

// define our URL
url = 'http://maps.googleapis.com/maps/api/geocode/json'

// set the required variables that the API is expecting
myaddress = 'Albuquerque, NM'
mysensor = 'false'

// put the required variables in a dictionary (arbitrarily called "payload")
payload = {'address':myaddress, 'sensor':mysensor}

// send the request to the API.
r = requests.get(url, params=payload)
{% endhighlight %}

The last line

{% highlight python %}
r = requests.get(url, params=payload)
{% endhighlight %}

is the equivalent of typing

{% highlight python %}
http://maps.googleapis.com/maps/api/geocode/json?address=Albuqueruque+NM&sensor=false
{% endhighlight %}

in your URL bar. But in this case rather than display the result on the screen, we store in in the 'r' variable. 'r' is arbitrary; you could call it 'google-answer' or 'api_response' or 'blueMonkey'.

It's easy to extract information from the object that we get back from the Google Maps API--like the geocoordinates.

{% highlight python %}
json = r.json()
lat = json['results'][0]['geometry']['location']['lat']
lng = json['results'][0]['geometry']['location']['lng']
{% endhighlight %}



If we string together everything we've covered so far, we have:

{% highlight python %}
import requests

url = 'http://maps.googleapis.com/maps/api/geocode/json'
myaddress = 'Albuquerque, NM'
mysensor = 'false'
payload = {'address':myaddress, 'sensor':mysensor}
r = requests.get(url, params=payload)

json = r.json()
lat = json['results'][0]['geometry']['location']['lat']
lng = json['results'][0]['geometry']['location']['lng']

print lat,lng
{% endhighlight %}

When you run this code, your output will be the latitude and longitude of ABQ. You can double check that it's working by pasting the coordinates into Google Maps.

{% highlight bash %}
35.110703 -106.609991
{% endhighlight %}

This code works fine for a single place, but we really want to process a list of places. Suppose we have a text file (placelist.txt) with a list of places (say, ones from [extracted from another file](/tutorials/extract-transform-save-csv "extract, transform, and save CSV data")) that looks like

{% highlight text %}
Albuquerque, NM
Santa Fe, NM
Abiquiu, NM
Silver City, NM
Taos, NM
{% endhighlight %}

Ultimately, we want some code that reads in the placenames from this file, and for each place, does what we did above for Albuquerque: make an API call, extract the latitude and longitude coordinates from the JSON response that we'll get from the Google server. 

If you're just reading in lines of texts from a file, the basic skeleton looks like

{% highlight python %}

// open our file of places
inputfile = open('placelist.txt')

// for each row in the file, do something
for row in inputfile:
  #do something

{% endhighlight %}

The 'something' that we want to do is to make an API call and process the request---meaning extract the latitude and longitude from the JSON response, just as we did before. Let's put our earlier code to get and print our geocoordinates within the loop that will read through all the places in our file

{% highlight python %}
import requests

inputfile = open('placelist.txt')

for row in inputfile:
  row = row.rstrip()
  url = 'http://maps.googleapis.com/maps/api/geocode/json'
  payload = {'address':row, 'sensor':'false'}
  r = requests.get(url, params=payload)
  json = r.json()

  lat = json['results'][0]['geometry']['location']['lat']
  lng = json['results'][0]['geometry']['location']['lng']

  print lat,lng
{% endhighlight %}

Notice that for each row we load from the file, we first strip off any whitespace (including new line characters) of the end using the rstrip() method that can be called on any string. It's always good to create and maintain clean data whenever possible.

The request module that we imported allows us to automatically convert the returned JSON response into a python object that we can access with the built-in python dictionary and list functionality. 

Running the above code should result in output like

{% highlight text %}
35.110703 -106.609991
35.6869752 -105.937799
36.207241 -106.3186397
32.770075 -108.280326
36.4072485 -105.5730665
{% endhighlight %}

Printing the coordiantes to our screen is helpful in that we can see the script is working. But that isn't particularly helpful for a larger goal of making this coordinates more portable. Let's modify our python script so that it can save our coordinates to a text file. 

To do this, since it's always nice to have well-structured data, let's create a CSV file. This will allow us to easily import our list of places into a number of mapping tools. This is best done by using the Python csv module so that it can take care of properly formatting the lines of our CSV file. The csv module is probably already installed on your computer.

The python method that we'll use write a line to the file requires that we pass it a python list, where each item of the list is a value to be separated by commas in the resulting CSV file. For example running this code

{% highlight python %}
  import csv
  outputfile = csv.writer(open('geocoded-placelist.txt','w'))

  newrow = ['1600 Pennsylvania Ave',38.89508698029150,-77.02255291970850]
  outputfie.writerow(newrow)
{% endhighlight %}

will give us a file that looks like

{% highlight text %}
'1600 Pennsylvania Ave',38.89508698029150,-77.02255291970850
{% endhighlight %}

Integrating the above statements into our existing code yields our final version of the script:

{% highlight python %}
import requests
import csv

inputfile = open('placelist.txt','r')
outputfile = csv.writer(open('geocoded-placelist.txt','w'))

for row in inputfile:
  row = row.rstrip()
  url = 'http://maps.googleapis.com/maps/api/geocode/json'
  payload = {'address':row, 'sensor':'false'}
  r = requests.get(url, params=payload)
  json = r.json()

  lat = json['results'][0]['geometry']['location']['lat']
  lng = json['results'][0]['geometry']['location']['lng']

  newrow = [row,lat,lng]
  outputfile.writerow(newrow)
{% endhighlight %}

Running this should result in a file (geocoded-placelist.txt) that looks like

{% highlight text %}
"Albuquerque, NM",35.110703,-106.609991
"Santa Fe, NM",35.6869752,-105.937799
"Abiquiu, NM",36.207241,-106.3186397
"Silver City, NM",32.770075,-108.280326
"Taos, NM",36.4072485,-105.5730665
{% endhighlight %}

That's all there is to it! Now you have a nicely formatted CSV file of your places and their geocoordinates that can be imported into most any mapping tool.