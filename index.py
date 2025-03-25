from actions.dissect_handler import dissect_keys
from requester import get_number_pages, make_request


def commence_process(url, page_num):
    is_valid = url_checker(url)
    
    if (not is_valid):
        return None
    
    pages = get_number_pages(url, str(page_num))
    
    # for index in range(0, pages):
    #     return None
       
    return None


def url_checker(url):
    if url != "https://keys.lol/bitcoin/":
        return False
    
    return True


commence_process("https://keys.lol/bitcoin/", 1)