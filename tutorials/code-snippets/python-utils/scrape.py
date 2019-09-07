from bs4 import BeautifulSoup
import os
import requests

url = 'https://repository.unm.edu/handle/1928/21936/recent-submissions?offset=0'

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)


for div in soup.findAll("div", { "class" : "artifact-title" }):
	#print div

	for link in div.findAll("a"):
		print(link.get('href'))

		url = link.get('href')

		r  = requests.get('https://repository.unm.edu' + url)

		data = r.text

		soup2 = BeautifulSoup(data)

		print ("i'm here")
		
		#for link in soup2.findAll('a'):
			#print "this " + str(link)
		
		for link in soup2.findAll("meta", { "name" : "citation_pdf_url" }):
			pdfurl = link.get('content')
			print 'now getting: ' + str(pdfurl)
			os.system('wget ' + str(pdfurl))