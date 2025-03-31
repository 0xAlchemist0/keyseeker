
import time

from actions.file_writer import write_to_file
from actions.key_validator import analyze_list
from requester import extract_key_list, get_number_pages, make_request

proxy_url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
def commence_process(base_url, page_num):
    is_valid = url_checker(base_url)
    if (not is_valid):
        return None
    
    proxy_collection = make_request(proxy_url, False, None)

    pages = get_number_pages(base_url, str(page_num))
    print(f"Pages: {pages}")
    for index in range(50, pages):
        print(f"#{index}")
        html = make_request(base_url + str(index), True, proxy_collection)
        key_list = extract_key_list(html)
        if(key_list is not None):
            analysis = analyze_list(key_list)
            write_to_file(analysis)

        
        #handle writing hits to file
    return None



def url_checker(url):
    if url != "https://keys.lol/bitcoin/":
        return False
    
    return True


commence_process("https://keys.lol/bitcoin/", 70)