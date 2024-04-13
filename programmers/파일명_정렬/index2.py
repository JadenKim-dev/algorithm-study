import re

def solution(files):
    files.sort(key=lambda file : int(re.findall('\d{1,5}', file)[0]))
    return sorted(files, key=lambda file : re.split('\d+', file)[0].lower())