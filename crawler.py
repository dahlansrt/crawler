import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


url = 'http://www.fccsingapore.com'
r = requests.get(url + '/membership/directory/')

# Make sure we got a result 200
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')


df = pd.DataFrame(
	columns=['uid','company_name','company_description','company_industry','company_address','company_website'])
print(df)

for company in soup.findAll('div', id=re.compile("^account-\d+")):	
	print(url + company.get('onclick'))
	print(company.get('id'))
	break