import string
from urllib.parse import urlparse


def to_base_62(deci):       # deci (ID of the url in table) -> integer
    s = string.digits + string.ascii_letters 
    hash_str = ''
    while deci > 0:
        hash_str = s[deci % 62] + hash_str
        deci //= 62  
    return hash_str


def is_valid_url(url):      # url -> string
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc != '':
        return True
    return False
