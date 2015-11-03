---
layout: post 
title: Extract, Transform, and Save CSV data
date: 2012-10-19 00:00:00
category: tutorial
---
Sometimes you&#8217;ll have a CSV file that contains lots of useful information, but where some of the information isn&#8217;t exactly in the form that you need. Moreover, it is often useful to extract a subset of information from a large and complex file to a separate file that you use for other experimental purposes.

This tutorial explains how to extract place names from a CSV file, clean them up a bit, and save them to a regular text file using python.

---

I have a CSV file of civil war battles that looks like this:

{% highlight python %}
Battle,Other Names,Location 1
Fort Sumter,,'Charleston County,SC'
Sewell's Point,,'Norfolk City,VA'
Aquia Creek,,'Stafford County,VA'
Philippi,Philippi Races,'Barbour County,WV'
Big Bethel,'Bethel Church,Great Bethel','York County,VA'
{% endhighlight %}

Ultimately, I want to map all of these battle sites, but I first need to geolocate all of the locations as listed in the CSV file. Rather than trying to geolocate from the places in the original CSV file (which is quite long), I want to isolate the places in a separate file so I can work with just those. Python makes this a cinch.

The first thing to do is to open my original CSV and read it. A standard way of opening files for reading (hence the &#8220;r&#8221; below) is like so:

{% highlight python %}
inputfile = open('civil-war-battles.csv','r')
{% endhighlight %}

This is not useful in itself, so let&#8217;s loop through all the lines in that file and print them, just to make sure we can do something with them.

{% highlight python %}
inputfile = open('civil-war-battles.csv','r')

for row in inputfile:
    print row
{% endhighlight %}

This of course prints out our original CSV file. Now, we really just want to extract our place, which we could do in any number of ways. Fortunately, Python makes it very easy to read and write CSV files that can do a lot of hard work for us. Let&#8217;s use the csv module, which we can import at the beginning of the file, and use to read in the CSV file.

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))

for row in inputfile:
    print row
{% endhighlight %}

If we inspect the output of this file, we can see that it looks like

{% highlight python %}
['Battle','Other Names','Location 1']
['Fort Sumter','','Charleston County , SC']
['Sewell's Point','','Norfolk City , VA']
['Aquia Creek','','Stafford County , VA']
['Philippi','Pilippi Races','Barbour County , WV']
['Big Bethel','Bethel Church, Great Bethel','York  County, VA']
{% endhighlight %}

This is very convenient because the csv.reader method that we called has automatically converted each row of the file into a Python list. This makes it easy to access particular elements of the CSV file. If we use the usual Python syntax for accessing an element of the list&#8211;here our location is the 3rd column, but computers always count starting with 0&#8211;so row[2] should give us our locations. We can print just the locations as we did the entire lines of the CSV file.

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))

for row in inputfile:
    print row[2]
{% endhighlight %}

This yields:

{% highlight python %}
Location 1
Charleston County , SC
Norfolk City , VA
Stafford County , VA
Barbour County , WV
York County, VA
{% endhighlight %}

Progress. But it&#8217;s annoying that the original data has inconsistencies, like the space (or not) before the comma. Problems like this are quite common. It&#8217;s easy to fix them. Let&#8217;s just find every instance of a space and a comma together (&#8216; ,&#8217;) and replace it with a singe comma (&#8216;,&#8217;). 

We can use the replace method that is built into string objects in Python, which is used like:

{% highlight python %}
your-string.replace(X,Y)
{% endhighlight %}

In our case, X is the literal string of a space and comma; Y is the literal string of only a comma:

{% highlight python %}
your-string.replace(' ,',',')
{% endhighlight %}

Integrating this into our code, we have:

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))

for row in inputfile:
	place = row[2].replace(' ,',',')
	print place
{% endhighlight %}

So far so good. But just printing the locations is not that helpful, though it is an easy way for us to see that things are working so far. Let&#8217;s write the locations to a file instead. We only need to add two lines of code: one to open the file for writing, and one to actually write the location.

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))
outputfile = open('placelist.txt','w')

for row in inputfile:
	place = row[2].replace(' ,',',')
	print place
	outputfile.write(place+'\n')
{% endhighlight %}

Notice that we are not opening the output file with the csv module, just with regular Python because we aren&#8217;t making a CSV file, just a text file. Also notice that we want to append a newline character &#8220;\n&#8221; to each line in the file so that each location gets its own line in the file. 

Check your placelist.txt file to make sure it looks good

{% highlight python %}
Location 1
Charleston County, SC
Norfolk City, VA
Stafford County, VA
Barbour County, WV
York County, VA
{% endhighlight %}

We could clean this up a bit more by skipping over the line in the CSV file that contains the headers, like &#8220;Location 1&#8243;. One easy way to do this is to keep track of which row of the file we are on while we&#8217;re looping through it, and skip the first one (which will be row 0).

To implement a counter, we need to define a variable before our loop begins, and increment it by one each time we go through the loop (= each row in the file)

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))
outputfile = open('placelist.txt','w')

i=0

for row in inputfile:
    place = row[2].replace(' ,',',')
    print place
    outputfile.write(place+'\n')
    i+=1
{% endhighlight %}

To skip the first row, we just need to test if we are on line 0 or not. Another way of thinking about it is that we only want to write to our file if we are on line 1 or greater (ie not 0). 

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))
outputfile = open('placelist.txt','w')

i=0

for row in inputfile:
    if (i &gt; 0):	
        place = row[2].replace(' ,',',')
        print place
        outputfile.write(place+'\n')
    i+=1
{% endhighlight %}

Notice the importance of indentation. We don&#8217;t want our i+=1 code to part of the if block, or it will never run!

You can use this same logic to help yourself work with more manageable files. Let&#8217;s say you have a big CSV file, and you are hoping to geolocate all the places. Rather than test your code on a big file that can take a lot of time and introduce hard to find errors, it&#8217;s often easier to just extract a subset of the data and go back to the big file later.  Especially for messy historical data, it is good practice to make sure your logic and general process works on well-formed data, then try bigger subsets and deal with problems that the messy data will introduce (and it will!). In other words, get everything working for a small amount of data, then scale up.

In our case, we can limit the size of our output file by not writing to the file if our counter gets past some threshold. So if we only wanted to write the first 2 lines, we can add that constraint to our existing &#8220;if&#8221; statement (line 11) that checks to see if we are on line 0 of our CSV file. 

{% highlight python %}
import csv

inputfile = csv.reader(open('civil-war-battles.csv','r'))
outputfile = open('placelist.txt','w')

i=0

for row in inputfile:
    if (i > 0 and i < 2):	
        place = row[2].replace(' ,',',')
        print place
        outputfile.write(place+'\n')
    i+=1
{% endhighlight %}