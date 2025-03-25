import json
import re

import requests
from bs4 import BeautifulSoup


def make_request(url):
    response = requests.get(url)
    html = BeautifulSoup(response.content, "html.parser")
    return html

def get_number_pages(url, page_num):
    html = make_request(url + page_num)
    
    located_section = html.find_all('script')[0]
    extract_array(located_section)


#script has the array of keys
def extract_array (script_text):
    
    # soup = BeautifulSoup(html_doc, "html.parser")
    # # locate the script, get the contents
    # script_text = soup.select_one("script").contents[0]

    # get javascript object inside the script
    model_data = re.search(r"keys = ({.*?});", script_text, flags=re.S)
    model_data = model_data.group(1)

    # "convert" the javascript object to json-valid object
    model_data = re.sub(
        r"^\s*([^:\s]+):", r'"\1":', model_data.replace("'", '"'), flags=re.M
    )

    # json decode the object
    model_data = json.loads(model_data)

    # print the data
    print(model_data)