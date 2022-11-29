#!/bin/python3

#lab 7
from bs4 import BeautifulSoup
import requests

URL="https://www.amazon.in/deal/fee756d4?showVariations=true&pf_rd_r=8XDEX4BCERTDZK1SHQJZ&pf_rd_p=7f4a3afe-60dd-4be9-828c-5703b1b1238a&pd_rd_r=3dfd884e-ccf2-4fc6-b838-c73f78d65451&pd_rd_w=qEFKq&pd_rd_wg=Fvx3g&ref_=pd_gw_unk"
r = requests.get(URL)

#html content
#print(r.content)


#js/ text from source 
soup = BeautifulSoup(r.content, "html5lib")
#print(soup.text)


#search for specific
t = soup.find('div', attrs= {'id': "octopus-dlp-asin-stream"})
# print(t.prettify())


mydata = []


products = t.find_all_next('li', attrs = {'class': "a-list-normal a-spacing-none no-margin-rightoverflow-hidden octopus-response-li-width"})

for product in products:
    
    data = {}
    
    data['name'] = product.find('a', attrs = {'class': "a-link-normal"})['title']
    data['price'] = product.find('span', attrs = {'class': "a-price-whole"}).text
    data['image'] = product.find('img', attrs = {'class': 'octopus-dlp-asin-image'})['src']
    data['link'] = "https://www.amazon.in" + product.find('a', attrs = {'class': "a-link-normal"})['href']
    print(data, '\n')
    
    mydata.append(data)


