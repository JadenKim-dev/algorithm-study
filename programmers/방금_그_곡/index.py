def solution(m, musicinfos):
    my = ""
    for i in range(len(m)):
        if i+1 < len(m) and m[i+1] == '#':
            my += "*"
        my += m[i]
        
    names, candidates = [], []
    for i in range(len(musicinfos)):
        info = musicinfos[i]
        tmp = info.split(',')
        names.append(tmp[2])

        h1, m1 = map(int, tmp[0].split(":"))
        h2, m2 = map(int, tmp[1].split(":"))
        minutes = (h2 - h1) * 60 + m2 - m1

        melodies = to_array(tmp[3])
        full_melodies = ''.join(melodies * (minutes//len(melodies)) + melodies[:minutes%len(melodies)])
        if my in full_melodies:
            candidates.append((i, minutes))
    if candidates:
        candidates.sort(key=lambda x : -x[1])
        return names[candidates[0][0]]
    else:
        return "(None)"

def to_array(m):
    arr = []
    for i in range(len(m)):
        if m[i] == '#':
            continue
        elif i < len(m)-1 and m[i+1] == '#':
            arr.append("*" + m[i:i+2])
        else:
            arr.append(m[i])
    return arr