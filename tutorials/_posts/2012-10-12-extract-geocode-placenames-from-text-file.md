--- 
layout: post 
title: Extract and Geocode Placenames from a Textfile
date: 2012-10-12 00:00:00
category: tutorial
---

This tutorial explains how to write a python script to read places from a text file and geolocate them (get latitude and longitude coordinates). It covers how to send requests to the Google Geocoding API and process the JSON response that it returns. 

---

To find coordinates for a place, we can use the [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/). To use it, we need to send it a request like

{% highlight python %}
http://maps.googleapis.com/maps/api/geocode/json?address=1600+pennsylvania+ave&sensor=false
{% endhighlight %}

For now, plug that URL into your browser's URL bar to see the result. You can see that the response sent from the server is just plain text, but formatted in Javascript Object Notation (JSON). Glancing through it, you can see it contains a lot of potentially useful information.

Python makes it very easy to send requests and process the results, especially when using the [requests module](http://docs.python-requests.org/en/latest/). (You may want to read about [installing python modules](../installing-python-modules/ "installing python modules").) A simple example of making a request in python looks like

{% highlight python %}
r = requests.get(URL, params=DICTIONARY)
{% endhighlight %}

In this case, our *URL* will be the base URL of the Google Geocoding API. For our *DICTIONARY*, we have to create a python dictionary to handle at least two bits of information we get from Google. These will be our dictionary keys: &#8216;address&#8217;, which is our place name, and &#8216;sensor&#8217; (which the API requires to be set to true or false). The code to make the request will look like

{% highlight python %}
url = 'http://maps.googleapis.com/maps/api/geocode/json'
payload = {'address':'1600 Pennsylvania Ave', 'sensor':'false'}
r = requests.get(url, params=payload)
{% endhighlight %}

OK. Suppose we have a text file (placelist.txt) with a list of places (say, ones from [extracted from another file](../extract-transform-and-save-csv-data/ "extract, transform, and save CSV data")) that looks like

{% highlight text %}
Charleston County, SC
Norfolk City, VA
Stafford County, VA
Barbour County, WV
York County, VA
{% endhighlight %}

Let's write some code that reads in the placenames from this file, makes an API call for each one, and then extracts and prints the latitude and longitude coordinates from the JSON response that we'll get from the Google server. Notice that for each row we load from the file, we first strip off any whitespace (including new line characters) of the end using the rstrip() method that can be called on any string. It's always good to create and maintain clean data.

{% highlight python %}
import requests

inputfile = open('placelist.txt')

for row in inputfile:
  row = row.rstrip()
  url = 'http://maps.googleapis.com/maps/apis/geocode/json'
  payload = {'address':row, 'sensor':'false'}
  r = requests.get(url, params=payload)
  json = r.json

  lat = json['results'][0]['geometry']['location']['lat']
  lng = json['results'][0]['geometry']['location']['lng']

  print lat,lng
{% endhighlight %}

You can see that we&#8217;ve simply added our code to make an API request to a basic python template that opens a text file and processes each row. The request module that imported allows us to automatically convert the returned JSON response into a python object that we can access with the built-in python dictionary and list functionality. 

Running the above code should result in output like

{% highlight text %}
32.7956561 -79.7848422
36.8507689 -76.2858726
38.4334566 -77.4242972
39.1398692 -80.0087746
37.2103925 -76.3868797
{% endhighlight %}

Obviously, this little bit of Python code can be incredibly handy when you have any more than a few places to geolocate. Even if you only have a few places, it is nice to save the coordinate for places so that we don&#8217;t have to keep looking them up, which is obviously much slower than just reading them from a text file. 

Also, because geocoding services usually have limits to how many you can do per day (like 2,500 in the case of Google), it can be necessary to spread out your geolocating efforts over several days (the subject of a different tutorial) and save the results as you go for cases when you have many thousands of points to geolocate.

Let's modify our python script so that it can save our coordinates to a text file. We just need to write them to a file in the usual way, which means we need to open a file for writing, and write the place name and coordinates to it. But since it's always nice to have well-structured data, let's create a CSV file. This is easily done by using the Python csv module so that it can take care of properly formatting the lines of our CSV file. (the csv module is probably already installed on your computer.) 

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
  json = r.json

  lat = json['results'][0]['geometry']['location']['lat']
  lng = json['results'][0]['geometry']['location']['lng']

  newrow = [row,lat,lng]
  outputfile.writerow(newrow)
{% endhighlight %}

Running this should result in a file (geocoded-placelist.txt) that looks like

{% highlight text %}
'Charleston County, SC',32.7956561,-79.7848422
'Norfolk City, VA',36.8507689,-76.2858726
'Stafford County, VA',38.4334566,-77.4242972
'Barbour County, WV',39.1398692,-80.0087746
'York County, VA',37.2103925,-76.3868797
{% endhighlight %}