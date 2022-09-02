import requests


'''
    This function returns a request object
'''
# Saving the respone from the website.
response = requests.get("https://www.geeksforgeeks.org/")

# print(x.text)  # it returns the html page of the page

headers = response.headers  # returns the headers ]

if __name__ == '__main__':
    if headers.get("X-Powered-By") is None:
        print("We couldn't figure out what the website is powered by.")
    else:
        print(headers.get('X-Powered-By'))
