from bs4 import BeautifulSoup
import requests

urls = ["https://google.com", "https://www.youtube.com", "https://facebook.com"]
# taking respone from each and every url and printing out its title
# for row in urls:


for row in urls:

    response = requests.get(row)
    soup = BeautifulSoup(response.text, "html.parser")
    # printing the tile of the website
    print(soup.title.string)


'''
# We then parse the html page
soup = BeautifulSoup(response.text, "html.parser")

# title from the website
print(f"title: {soup.title.string}")
'''
