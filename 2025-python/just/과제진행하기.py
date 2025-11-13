# 완료한 과제를 담은 배열을 관리, 하나씩 추가해 나감
# 멈춘 과제를 스택으로 관리 -> (과제 이름, 남은 시간)
# plans를 모두 순회하면서, 하나씩 과제를 수행
    # 현재 시간을 과제 시작 시간으로 이동
    # 현재 과제의 종료 시간이 다음 과제 시작 시간 이후일 경우, 남은 시간을 계산해서 현재 과제를 스택에 삽입

def solution(plans):
    tmp = []
    for [name, start, playtime] in plans:
        hour, minute = start.split(':')
        time = int(hour) * 60 + int(minute)
        tmp.append([name, time, int(playtime)])
    plans = sorted(tmp, key=lambda x:x[1])
    
    answer = []
    stack = []
    time = 0
    
    for i, [name, start, playtime] in enumerate(plans):
        time = start
        next_time = plans[i+1][1] if i < len(plans) - 1 else int(1e9)
        if time + playtime > next_time:
            stack.append((name, time + playtime - next_time))
            continue

        time += playtime
        answer.append(name)
        while stack and time < next_time:
            _name, _playtime = stack.pop()
            if time + _playtime <= next_time:
                time += _playtime
                answer.append(_name)
                continue
            else:
                stack.append((_name, time + _playtime - next_time))
                break

    return answer
