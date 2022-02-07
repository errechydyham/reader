import urllib.request, urllib.parse, urllib.error 

t = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

for line in t: 
    print(line.decode().strip()) 