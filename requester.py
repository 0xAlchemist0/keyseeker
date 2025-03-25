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
    page_number_element = html.find('h1', class_='flex flex-col text-base break-words text-center')
    pages = int(page_number_element.find_all('span')[3].text)
    return pages

#script has the array of keys
def extract_key_list (html):
    script_collection = html.find_all('script')
    script_found = None
    key_list = None
    for script in script_collection:
        if 'const keys = ' in script.text:
            script_found = script
    
    if script_found:
        match = re.search(r'(\[\s*\{.*?\}\s*\])', script_found.string, re.DOTALL)
    
    if match:
        json_str = match.group(1)  # Extracted JSON array as a string
        key_list = json.loads(json_str)  # Convert to Python object
        # print(key_list)  # Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        return key_list
    else:
        print("JSON array not found in script tag")
        return None
    