
def solution(n, t, m, timetable):
    time_list = []
    for time in timetable:
        hh, mm = map(int, time.split(":"))
        time_list.append([hh, mm])
    time_list.sort()

    now = [9, 0]

    def next_time():
        now[1] += t
        if now[1] >= 60:
            now[0] += 1
            now[1] -= 60

    curr_time_idx, curr_passenger = 0, 0
    for i in range(n):
        curr_passenger = 0
        while curr_time_idx < len(time_list) and curr_passenger < m and is_prev(time_list[curr_time_idx], now):
            curr_time_idx += 1
            curr_passenger += 1
        if i < n-1:
            next_time()
    curr_time_idx -= 1
    
    if curr_passenger < m:
        return convert(now)
    else:
        while time_list[curr_time_idx] == time_list[curr_time_idx-1] and curr_time_idx >= 1:
            curr_time_idx -= 1
        result = one_minute_before(time_list[curr_time_idx])
        return convert(result)


def is_prev(time, now):
    if time[0] != now[0]:
        return time[0] < now[0]
    else:
        return time[1] <= now[1]


def one_minute_before(time):
    if time[1] == 0:
        time[0] -= 1
        time[1] = 59
    else:
        time[1] -= 1
    return time


def convert(time):
    def padding(num):
        num = str(num)
        return num if len(num) == 2 else "0"+num
    return padding(time[0]) + ":" + padding(time[1])