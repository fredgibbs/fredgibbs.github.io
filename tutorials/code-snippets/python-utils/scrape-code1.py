from bs4 import BeautifulSoup
import requests

# store our URL in a variable
url = 'http://fredgibbs.net/extras/web-scraping-python/simple_page_1.html'

# use the requests module to get the code of the webpage
# we will store the code in a variable called 'r'
# the get method returns a requests object
r  = requests.get(url)

# we can use the text method of the requests object to get the plain HTML
data = r.text

# convert our object to a beautiful soup object for earlier processing
soup = BeautifulSoup(data)

#output to the terminal 
print "our soup:"
print soup

print "about to print all links:"

# grab all of the a tags and print them
for a_tag in soup.findAll("a"):
  href = a_tag.get('href')

	# always good to let our output tell us what's going on
	print "attempting to download: " + href

	# get page and save it with requests
	urllib.urlretrieve(href)