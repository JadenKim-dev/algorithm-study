import datetime as dt

def solution(lines):
start*list, end_list = [], []
for line in lines:
*, end_time, duration = line.split()
end_time = dt.datetime.strptime(end_time, "%H:%M:%S.%f")
duration = dt.timedelta(seconds=(float(duration[:-1]) - 0.001))
start_time = end_time - duration
start_list.append(start_time)
end_list.append(end_time)

    max_process = 1
    for i in range(len(lines)-1):
        curr_end = end_list[i]
        curr_process = 1
        for j in range(i+1, len(lines)):
            if start_list[j] < curr_end + dt.timedelta(seconds=1):
                curr_process += 1
        max_process = max(max_process, curr_process)
    return max_process
