import subprocess, shlex
from .utils import dsxs


def check_sqli(url, cookie):
    remote_command = shlex.split(f'sqlmap -u "{url}" --cookie="{cookie}" --batch --fresh-queries --flush-session')
    process = subprocess.Popen(remote_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    decoded = stdout.decode('UTF-8')
    if 'sqlmap identified' in decoded:
        response = decoded.split('sqlmap identified the following injection point(s) with a ')[1].split('---')
        return response[1]
    return 'No SQL injection points were found'


def check_nosqli(url):
    remote_command = shlex.split(f'nosqli scan -t {url}')
    process = subprocess.Popen(remote_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    decoded = stdout.decode("UTF-8")
    if 'Found' in decoded:
        response = decoded.split("Found")
        return response[1:]
    return 'No NoSQL injection points were found'


def check_xss(url, cookie):
    dsxs.init_options(cookie=cookie)
    result = dsxs.scan_page(url)
    if 'appears to be XSS vulnerable' in result:
        return result
    return 'No XSS vulnerabilities were found'
