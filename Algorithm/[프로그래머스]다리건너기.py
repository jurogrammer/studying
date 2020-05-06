from collections import deque
def solution(bridge_length, weight, truck_weights):
    answwer = 0
    truck_weights[::-1]
    time = 1

    bridge = deque([]) # 원소 : weight,inTime   무게 들어간 시간
    remainWeight = weight
    while truck_weights:
        if bridge and (bridge[-1][1] + bridge_length) == time :
            remainWeight += bridge.pop()[0]
            spanTime = 1

            if remainWeight >= truck_weights[-1]:
                truckWeight = truck_weights.pop()
                bridge.appendleft([truckWeight,time])
                remainWeight -= truckWeight

        else:
            if remainWeight >= truck_weights[-1]:
                truckWeight = truck_weights.pop()
                bridge.appendleft([truckWeight, time])
                remainWeight -= truckWeight
                spanTime = 1
            else:
                spanTime = bridge[-1][1] + bridge_length - time
        time += spanTime

    if bridge :
        time = bridge[0][1] + bridge_length

    answer = time
    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))