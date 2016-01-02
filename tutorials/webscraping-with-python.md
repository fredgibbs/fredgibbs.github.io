---
layout: post 
title: Introduction to Webscraping with Python
date: 2014-11-02 00:00:00
category: tutorial
---

# Getting Sources from the Web
Digital history is way more fun when you have digital sources to work with. As much as you might want to map, mine, or visualize your sources, or work at larger-than-usual scales, one of the first calculations is often whether the work to create or collect them is worth the potential payoff.

The good news is that we have relatively easy access to more digital data on the web than ever before; the bad news is that it's not always easy to get it beyond lots of downloading of individual documents. There are many archives of various kinds with lots of links to PDFs of sources one might be interested in. You *could* simply click through each link and download the file, which is the best way when you only have a few dozen sources. 

But what if you need 100 documents? Or 1000? or 10,000? Then you'd have carpel tunnel. And less time for actually analyzing your sources. 

In a perfect digital world, all websites would have nice back-end interfaces (APIs) that allow us to get data easily without having to deal with often messy HTML. But we don't live in that world.

Why not create a small python script to do the work for you? Computers are really good at mindless drudgery. Provided that the page you're interested in getting text or files from has a more or less regular structure (as most do, since they are generated programatically), it's actually fairly straightforward to automate the process of copying and pasting or downloading files.

The process of automating the process you might go through with your mouse on a webpage is called web scraping. It sounds weird, but it's less weird than "automating the process of manually clicking through websites and downloading stuff". This tutorial walks through the process of figuring out how to extract certain page elements like PDFs.


# PART I: A Simple Example
Rather than get distracted by a "real" webpage that has lots of code and other features that aren't important to us, we're going to use a dummy page so that we can highlight the technique. Then we'll look at some actual webpages for various archives to show how to apply the general technique explained here.

In the first case, we have a very basic webpage with a list of PDFs that we want to download. There are 10, but there could be 10,000.

As a flexible scripting language, Python is very useful here. Particularly if we employ the help of two modules. See an introduction to modules and how to install them, see python modules.

Please be sure you have installed these successfully before continuing!


Let's put them to use in a simple way to just make sure we can get everything working.

```python

from bs4 import BeautifulSoup
import requests

# store our URL in a variable
url = 'http://fredgibbs.net/extras/web-scraping-python/simplescrape1.html'

# use the requests module to get the code of the webpage
# we will store the code in a variable called 'r'
# the get method returns a requests object
r  = requests.get(url)

# we can use the text method of the requests object to get the plain HTML
data = r.text

# convert our object to a beautiful soup object for earlier processing
soup = BeautifulSoup(data)

# output to the terminal to see what we grab.
# it should be all of the source code.
print "our soup:"
print soup

print "about to print all links:"

# grab all of the a tags and print them
for link in soup.findAll("a"):
	print link
```

This will generate output like:

~~screenshot1~~

Here we have printed out the entire object. In reality, we usually just want part of what's contained in the &lt;a&gt; tag, like the hyperlink text, or perhaps the href attribute in the anchor tag, which tells us how to access the PDF online. To do this, let's change out loop code (note the change of variable name to help us be more precise with our labeling) to be

```python
for a_tag in soup.findAll("a"):
	# to get a particular attribute of a tag, the BeautifulSoup documentation tells us to use this format:
	href = a_tag.get('href')
	print href
```

~~screenshot1~~

Once we collect the hrefs, then we can add a bit more code to grab from the web all the PDFs.

```python
for a_tag in soup.findAll("a"):
	href = a_tag.href
		
	# always good to let our output tell us what's going on
	print "attempting to download: " + href

	# get page and save it with requests
	urllib.urlretrieve(href)
```

After you run all the code, you will see you now have all the PDF files in your directory. 

~~screenshot~~

Congratulations! You've reached first base of webscraping!!


# PART II: getting to buried links    
Of course real webpages aren't always quite so straightforward. Let the above example illustrate the virtues of clean code, and not burying useful data behind unnecessary pages! 

Let's look at the source code of a messier page.

<page with extra a tags, and useful ones in a div tag>

Let's look at the code. These sites are usually highly standardized, meaning that blocks of code follows predictable patterns. In this case we can see that our anchor links are always enclosed within a DIV tag with a class name of "artifact-title".

Let's modify our strategy a little. First, get all the DIV tags with that class, and for each one, pull out the A tag within it. The built-in functionality of Beaultiful Soup makes it easy to target our search for tags with a specific class name.

```python
from bs4 import BeautifulSoup
import os
import requests

url = 'morecomplexpage.html'

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)


for div in soup.findAll("div", { "class" : "artifact-title" }):
	#print div

	for link in div.findAll("a"):
		print(link.get('href'))
```


Notice that we've modified our findAll call to look for specific class of div tag. 

Inspecting the output, we see that this gives us just the links we're looking for. Perfect! Again, while the "artifact-title" class name is unique to this example, this strategy is usable on most any website; you just need to recognize what the source code will allow you to do. Perhaps you need to grab all the text with in a parent DIV container. It is rare, but you may encounter code that simply doesn't provide easy access to the links you want; strategies for that case must be saved for another tutorial.


# PART III: a more complicated page
Another common situation is when the PDFs you want are described on a separate pages, as illustrated in this example.

Even though it might seem like a totally different kind of situation, our strategy will be to simply extend the code we've already written to conduct two rounds of scraping, one for each page we have to deal with.

Let's just get the links of the pages on the first page.

Now we have a list of all the pages that contain the actual links to the PDFs. So all we have to do now is visit those pages, scrape them to extact the link to the PDF. This might sound complicated, but is no different than what we've already done. 

```python
from bs4 import BeautifulSoup
import os
import requests

url = 'abstractexample1.html'

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for div in soup.findAll("div", { "class" : "artifact-title" }):

	for link in div.findAll("a"):
		url = link.get('href')
		print url

		# get the code of our the second of our two pages
		r  = requests.get('http://programminghistorian.org' + url)

		data = r.text

		soup2 = BeautifulSoup(data)
		
		# from the code, let's pull out all the links with the proper class id
		for link in soup2.findAll("meta", { "name" : "citation_pdf_url" }):
			pdfurl = link.get('content')
			print 'found filename: ' + str(pdfurl)
			
			# os.system('wget ' + str(pdfurl))
```


You can see here that we've added a loop within our existing loop. Let's step through the code a bit. 

First, we grab all the links to item pages on the main page. For each one, we get all the relevant &lt;a&gt; tag from the item page, pull off the link to the actual PDF.

We can see from the URLs that we've scraped that they look a little weird. They don't like full URLs because they are relative paths. In order for us to use these effectively, we need to full, complete URLs. But these aren't on the page, you say! So we'll make them. We can construct the absolute URL by simply making our relative links look more like whatever's in the URL bar. 
Now that we've gotten a list of URLs that point to files that we want to download, how do we automate the process of downloading them? The urllib library makes this very easy.

import urllib
myurl = 'http://someurl.com'
urllib.urlretrieve(url, "file.txt")

Integrating this into the code we used above, we have

```python
from bs4 import BeautifulSoup
import urllib
import requests

# let's modularize our URL so we can access certain parts of it later.
urlbase = "http://programminghistorian.org/assets/"
page = 'abstractexample1.html'

r  = requests.get(urlbase + page)

data = r.text

soup = BeautifulSoup(data)

for div in soup.findAll("div", { "class" : "artifact-title" }):

	for link in div.findAll("a"):
		url = link.get('href')
		print url

		# get the code of our the second of our two pages
		r  = requests.get('http://programminghistorian.org' + url)

		data = r.text

		soup2 = BeautifulSoup(data)
		
		# from the code, let's pull out all the links with the proper class id
		for link in soup2.findAll("meta", { "name" : "citation_pdf_url" }):
			pdfurl = link.get('content')
			print 'found filename: ' + str(pdfurl)
			urllib.urlretrieve(url, urlbase + pdfurl)
```

