import requests
from bs4 import BeautifulSoup

URL = "https://www.komplett.se/product/1158205/gaming/spelutrustning/gamingskarmar/lg-34-curved-gamingskarm-ultragear-34gn850-b#"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")