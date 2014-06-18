import requests

# Open a file
f = open("placelist.txt", "r+")

content = f.readlines()

print "Read String is : ", content[0]

url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + content[0]

print "Read String is : ", url

r = requests.get(url)
json = r.json()

print json['results'][0]['geometry']['location']['lat']
print json['results'][0]['geometry']['location']['lng']

# Close opend file
f.close()