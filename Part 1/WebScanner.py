import requests

x = requests.get("https://youtube.com")

# print(x.text)  # it returns the html page of the page

headers = x.headers # returns the headers ]

if headers.get("X-Powered-By") is None:
    print("We couldn't figure out what the website is powered by.")
else:
    print(headers.get('X-Powered-By'))
