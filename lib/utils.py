import re

def find_memtions(content):
    regex = re.compile(r"@(?P<username>)(\s|$)", re.I)
    return [m.group("username") for m in regex.finditer(content)]

