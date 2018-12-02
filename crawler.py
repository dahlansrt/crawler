from requests import get
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'http://www.fccsingapore.com'
r = get(url + '/membership/directory/')

# Make sure we got a result 200
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')

result_array = np.empty((0, 6))

counter = 0
for company in soup.findAll('div', id=re.compile("^account-\d+")):
	counter += 1
	uid = url + company.get('onclick')	
	desc = company.select_one("div.list_company_description").get_text()
	r_company = get(uid)
	soup_company = BeautifulSoup(r_company.content, 'html.parser')
	name = soup_company.find(id="fccs_directory_cmp_name_title").get_text()
	industry = "ABC"
	address = soup_company.select_one("p.fccs_directory_detail_info").get_text()
	website = soup_company.select_one("div.iconwebsitedetail").a['href']

	result = [uid, name, desc, industry, address, website]
#	print(url + company.get('onclick'))
#	print(company.get('id'))
	result_array = np.append(result_array, [result], axis=0)
	if not counter % 5:
	 	break

df = pd.DataFrame(data=result_array,
	index_col='uid'
	columns=['uid','company_name','company_description','company_industry','company_address','company_website'])

#df.set_index('uid', inplace=True)
print(df.company_address)	