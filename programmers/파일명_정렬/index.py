from functools import cmp_to_key

def solution(files):
    files.sort(key=cmp_to_key(compare))
    return files

def compare(a, b):
    h1, n1 = split_file(a)
    h2, n2 = split_file(b)
    if h1 < h2:
        return -1
    elif h1 > h2:
        return 1
    elif n1 < n2:
        return -1
    elif n1 > n2:
        return 1
    else:
        return 0
    

def split_file(file):
    idx, result = 0, []
    while not file[idx].isdigit():
        idx += 1
    result.append(file[:idx].lower())
    tmp = idx
    while idx<len(file) and file[idx].isdigit() and idx < tmp+5:
        idx += 1
    result.append(int(file[tmp:idx]))
    return result