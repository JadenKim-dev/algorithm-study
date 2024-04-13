def solution(people, limit):
    people.sort()
    cnt = 0
    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            cnt += 1
        right -= 1
    return len(people) - cnt