from bs4 import BeautifulSoup
import requests
import os
import urllib

r = requests.get("https://repository.unm.edu/handle/1928/3347/recent-submissions?offset=0")
data = r.text
soup = BeautifulSoup(data)
divs = soup.find_all("div", attrs={"class": "artifact-title"})
i=0

for div in divs:
	links = div.find_all('a')	

	for link in links:
		#print(link.get('href'))
		url = 'http://repository.unm.edu' + link.get('href')
		print "fetching: " + url

		r2 = requests.get(url)
		metapage = r2.text
		#print metapage

		metasoup = BeautifulSoup(metapage)

		pdflink = metasoup.find("meta", attrs={"name": "citation_pdf_url"})
		print pdflink.get('content')
		pdfurl = pdflink.get('content')
		#os.system('wget %s' % pdfurl)

		#urllib.urlretrieve(pdfurl, pdfurl)
		f = open(str(i) + '.pdf','wb')
		f.write(requests.get(pdfurl).content)
		f.close()
		i = i + 1