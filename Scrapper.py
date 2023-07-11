import requests
from bs4 import BeautifulSoup

URL = "https://coomer.party/onlyfans/user/amouredelavie"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("small")

# for je in job_elements:
print(job_elements[0].text.replace('\n',''))
