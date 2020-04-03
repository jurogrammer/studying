def solution(cacheSize, cities):
    answer = 0
    cache = []
    length = 0

    for city in cities:
        city = city.lower()
        if length < cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1

            else:
                cache.append(city)
                length += 1
                answer += 5
        else:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                cache.pop(0)
                cache.append(city)
                answer += 5

    return answer

cacheSize = 2
cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
print(solution(cacheSize,cities))