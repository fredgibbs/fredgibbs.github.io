--- 
layout: post 
title: Create a KML file with Python
date: 2012-10-26 00:00:00
category: tutorial
---

If you want a quick and dirty way to visualize datapoints on a map, python makes it easy to create a [KML file](https://developers.google.com/kml/documentation/kml_tut) that you can overlay on a map embedded on a webpage or on Google Earth.

---

Let's say you've [extracted placenames](../extract-transform-and-save-csv-data/ "extract, transform, and save CSV data") from somwhere, and [geocoded them](../geocoding-a-list-of-places/ "geocoding a list of places"), and now have a file that looks like:

{% highlight text %}
'Charleston County, SC',32.7956561,-79.7848422
'Norfolk City, VA',36.8507689,-76.2858726
'Stafford County, VA',38.4334566,-77.4242972
'Barbour County, WV',39.1398692,-80.0087746
'York County, VA',37.2103925,-76.3868797
{% endhighlight %}

Using the python [simplekml module](http://simplekml.readthedocs.org/en/latest/index.html) makes creating a KML file of these points unfairly easy.

If you haven't already, you'll first need to get the [simplekml module](../installing-python-modules/ "installing python modules").

There are really only three crucial lines of code needed to use simplekml. 1) Create a simplekml object; 2) Add points to it; 3) Write the object to a file. 

Let's start by reading the lines of our CSV file in our usual way

{% highlight python %}
import csv

inputfile = csv.reader(open('geocoded-placenames.csv','r'))

for row in inputfile:
  #do something
{% endhighlight %}


Now, let's add the necessary simplekml bits:

{% highlight python %}
import csv
import simplekml

inputfile = csv.reader(open('geocoded-placenames.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
  kml.newpoint(name=row[0], coords=[(row[2],row[1])])

kml.save('battleplaces.kml')
{% endhighlight %}


The simplekml newpoint method requires that we send it a NAME and a COORDS, each of which we can easily pull directly from the CSV file that we&#8217;ve opened via our csv reader. Because csv.reader returns a list, we can access elements of that list by their numerical index. For the first row of our CSV file, row[0] refers to &#8220;Charleston County, SC&#8221;, and row[1] refers to 32.7956561.

We saved our coordinates as lat,long but simplekml wants them in the reverse order (long, lat), which is why we need to create the list like [(row[2],row[1])] as seen above.

So for each row in our CSV file, we create new point via the newpoint method of the kml object. Once we&#8217;ve finished with the file, we just need to call the save method on the kml object, and it will create a perfect KML file (&#8216;battleplaces.kml&#8217;) for us. 
