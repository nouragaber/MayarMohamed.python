import requests
import bs4
text= "geeksforgeeks"
url = 'https://google.com/search?q=' + text
request_result=requests.get( url )
soup = bs4.BeautifulSoup(request_result.text,
                         "html.parser")
heading_object = soup.find_all('h3')
for info in heading_object:
    print(info.getText())
    print("------")


