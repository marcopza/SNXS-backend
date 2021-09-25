import subprocess
from .utils import dsxs


def check_sqli(url, cookie):
    return_code = subprocess.run(f'sqlmap -u "{url}" --cookie="{cookie}" --batch --fresh-queries --flush-session',
                                 shell=True, capture_output=True)
    response = return_code.stdout.decode("UTF-8")
    print(response)
    return response


def check_nosqli(url, cookie):
    lol = None


def check_xss(url, cookie):
    dsxs.init_options(cookie=cookie)
    result = dsxs.scan_page(url)
    return result
