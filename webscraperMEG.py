import requests
from bs4 import BeautifulSoup
import pandas as pd

def positions():
    jobs = []
    location= []
    url = 'https://www.indeed.com/cmp/Lockheed-Martin/jobs'
    response = requests.get(url, verify=True)
    soup = BeautifulSoup(response.text, 'html.parser')
    for x in soup.findAll('button', {'class':'css-1w1g3cd eu4oa1w0'}):
        jobs.append(x.text.strip())
    for y in soup.findAll('span', {'class':'css-4p919e e1wnkr790'}):
        location.append(y.text.strip())
    return pd.DataFrame({'Lockheed Martin ':jobs, 'Minneapolis, MN':location})


positions()

print(positions())