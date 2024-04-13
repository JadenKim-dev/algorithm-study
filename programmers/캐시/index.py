from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = deque(maxlen=cacheSize)
    total = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            total += 1
            cache.remove(city)
            cache.append(city)
        else :
            total += 5
            cache.append(city)
    return total