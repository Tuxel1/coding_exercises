import feedparser

URL = "https://tooltime.substack.com/feed"

feed = feedparser.parse(URL)

print(feed.feed.title)
print(feed.feed.description)
print("\n ---------- \n")

for item in feed.entries:
    print(item.title)
    print(item.description)
    print(item.link)
    print("\n")