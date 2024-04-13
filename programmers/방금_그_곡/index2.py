def solution(m, musicinfos):
    m = transform(m)
    answer = (0, '(None)')
            
    for info in musicinfos:
        tmp = info.split(',')
        name = tmp[2]

        h1, m1 = map(int, tmp[0].split(":"))
        h2, m2 = map(int, tmp[1].split(":"))
        minutes = (h2 - h1)*60 + m2 - m1

        melodies = transform(tmp[3])
        full_melodies = melodies * (minutes // len(melodies)) + melodies[:minutes % len(melodies)]
        if m in full_melodies and minutes > answer[0]:
            answer = (minutes, name)

    return answer[1]

def transform(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')