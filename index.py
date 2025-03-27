
from actions.key_validator import analyze_list
from requester import extract_key_list, get_number_pages, make_request


def commence_process(base_url, page_num):
    is_valid = url_checker(base_url)
    if (not is_valid):
        return None
    
    pages = get_number_pages(base_url, str(page_num))
    print(f"Pages: {pages}")
    for index in range(1, pages):
        html = make_request(base_url + str(index))
        key_list = extract_key_list(html)
        analysis = analyze_list(key_list)
        
        #handle writing hits to file
    
       
    return None



def url_checker(url):
    if url != "https://keys.lol/bitcoin/":
        return False
    
    return True


commence_process("https://keys.lol/bitcoin/", 1)