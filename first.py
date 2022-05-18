import sys
import time
from bs4 import BeautifulSoup
import requests
try:
    page = requests.get('https://scholar.google.com/')
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print('Error for link:')
    print(error_type,'Line:' , error_info.tb_lineno)

time.sleep(2)
s=BeautifulSoup(page.text,'html.parser')
links = s.find_all('span',attrs={'class':'gs_hlt'})
# print(page)
print(s)
print(links)
for i in links:
    print(i.text)
    print("/n")
    