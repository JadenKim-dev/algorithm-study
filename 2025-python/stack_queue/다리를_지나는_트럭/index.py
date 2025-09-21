from collections import deque

def solution(bridge_length, weight, truck_weights):
    weights_queue = deque(truck_weights)
    queue = deque([(weights_queue.popleft(), 0)])
    time = 0
    sum = 0
    
    while weights_queue:
        for i in range(len(queue)):
            w, cnt = queue[i]
            queue[i] = (w, cnt+1)
            sum += w
        print(sum)
        if len(queue) > 0 and queue[0][1] == bridge_length:
            queue.popleft()

        if sum + weights_queue[0] < weight:
            queue.append((weights_queue.popleft(), 0))
        
        time += 1
    
    return time

print(solution(2, 10, [7,4,5,6]))