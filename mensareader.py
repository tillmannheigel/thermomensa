import feedparser

myFeedAddress = 'http://www.studentenwerk-marburg.de/?id=416'

parser = feedparser.parse(myFeedAddress)

for item in parser['items']:
	print(str(item['title'].encode('utf-8')))
	print("\n")
