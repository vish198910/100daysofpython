from bs4 import BeautifulSoup
import requests

#prettify() method to make your html look some sort of idented and arranged
#find() method to find first of the matching tags, classes for you from the above html text we have scrapped
#find_all() to search them all 

html_text = requests.get('https://webscraper.io/test-sites/e-commerce/allinone').text
soup = BeautifulSoup(html_text,'lxml')
products = soup.find_all("div",class_ ="col-sm-4 col-lg-4 col-md-4")
for product in products:
    print(product.a.text)



