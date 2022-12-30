import pyshorteners

url = input('enter the url you want to short it : ')

pyshort = pyshorteners.Shortener()

url_short = pyshort.tinyurl.short(url)

print(url_short)
