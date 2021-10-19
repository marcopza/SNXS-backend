import subprocess, shlex
from .utils import dsxs


def check_sqli(url, cookie):
    remote_command = shlex.split(f'sqlmap -u "{url}" --cookie="{cookie}" --batch --fresh-queries --flush-session')
    process = subprocess.Popen(remote_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    response = stdout.decode('UTF-8').split('sqlmap identified the following injection point(s) with a ')[1]\
        .split('---')
    return response[1]


def check_nosqli(url):
    remote_command = shlex.split(f'nosqli scan -t {url}')
    process = subprocess.Popen(remote_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    response = stdout.decode("UTF-8").split("Found")
    return response[1:]


def check_xss(url, cookie):
    dsxs.init_options(cookie=cookie)
    result = dsxs.scan_page(url)
    return result
