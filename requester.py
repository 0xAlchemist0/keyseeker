import json
import random
import re

import requests
from bs4 import BeautifulSoup


#gotta find a way to bypass are you human in order to continue and  make script run sucessfully
def make_request(url, html, proxies):
    selected_proxy = choose_proxy(proxies)
    print(selected_proxy)
    response = requests.get(url, proxies=selected_proxy) if proxies else requests.get(url)
    print(selected_proxy)
    if(html):
        html = BeautifulSoup(response.content, "html.parser")
        return html
    
    else:
     result = response.json()
     print(result)
     return result['data']

def get_number_pages(url, page_num):
    html = make_request(url + page_num, True, None)
    page_number_element = html.find('h1', class_='flex flex-col text-base break-words text-center')
    pages = int(page_number_element.find_all('span')[3].text)
    return pages

#script has the array of keys
def extract_key_list (html):
    script_collection = html.find_all('script')
    script_found = None
    key_list = None
    match = None
    for script in script_collection:
        if 'const keys = ' in script.text:
            script_found = script
    
    if script_found is not None:
        match = re.search(r'(\[\s*\{.*?\}\s*\])', script_found.string, re.DOTALL)
    
    if match is not None:
        json_str = match.group(1)  # Extracted JSON array as a string
        key_list = json.loads(json_str)  # Convert to Python object
        # print(key_list)  # Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        return key_list
    else:
        print("JSON array not found in script tag")
        return None
    

def choose_proxy(proxies):
    
     print(type(proxies))
    
     
     if(proxies):
          selected = random.choice(proxies)
          print(selected)
          ip, port = selected['ip'], selected['port']
          print(ip)
          return {"http": f"https://{ip}:{port}" }
    
    


# {'_id': '676927d46b79c1e0b57b3ae1', 'ip': '50.63.12.101', 'anonymityLevel': 'elite', 'asn': 'AS398101', 'country': 'US', 'created_at': '2024-12-23T09:05:24.359Z', 'google': False, 'lastChecked': 1743276925, 'latency': 140.569, 'org': 'GoDaddy.com, LLC', 'port': '45801', 'protocols': ['socks4'], 'speed': 2, 'upTime': 91.3963328631876, 'upTimeSuccessCount': 648, 'upTimeTryCount': 709, 'updated_at': '2025-03-29T19:35:25.023Z', 'city': 'Tempe', 'isp': 'GoDaddy.com, LLC', 'responseTime': 76}
               
