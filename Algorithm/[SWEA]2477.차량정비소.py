import collections

testCase = int(input())


class Customer:
    def __init__(self):
        self.customerNumber = None
        self.receptionNumber = None
        self.maintenanceNumber = None
        self.remainProcessingTime = None

    def setCustomerNumber(self, n):
        self.customerNumber = n

    def setReceptionNumber(self, n):
        self.receptionNumber = n

    def setMaintenanceNumber(self, n):
        self.maintenanceNumber = n

    def setRemainProcessingTime(self, t):
        self.remainProcessingTime = t

    def getCustomerNumber(self):
        return self.customerNumber

    def getReceptionNumber(self):
        return self.receptionNumber

    def getMaintenanceNumber(self):
        return self.maintenanceNumber

    def getRemainProcessingTime(self):
        return self.remainProcessingTime

def findCounter(counter,x):
    for i in range(1,x+1):
        if counter[i] != 0:
            return True
    return  False

def comeInReceptionQueue(t, comeInTime, receptionQueue, k):
    while comeInTime and comeInTime[0] == t:
        k += 1
        customer = Customer()
        customer.setCustomerNumber(k)
        receptionQueue.appendleft(customer)
        comeInTime.popleft()
    return k


def proccessReceptionCounter(receptionCounter, receptionQueue, maintenanceQueue, receptionCounterProcessingTime, n):
    for i in range(1, n + 1):
        if receptionCounter[i] != 0:
            customer = receptionCounter[i]
            customerRemainTime = customer.getRemainProcessingTime()
            customerRemainTime -= 1

            # 딱 0이 되면!
            if customerRemainTime == 0:
                maintenanceQueue.appendleft(customer)
                if receptionQueue:
                    addedCustomer = receptionQueue.pop()
                    addedCustomer.setReceptionNumber(i)
                    addedCustomer.setRemainProcessingTime(receptionCounterProcessingTime[i])
                    receptionCounter[i] = addedCustomer
                else:
                    receptionCounter[i] = 0
            else:
                customer.setRemainProcessingTime(customerRemainTime)

        else:
            if receptionQueue:
                addedCustomer = receptionQueue.pop()
                addedCustomer.setReceptionNumber(i)
                addedCustomer.setRemainProcessingTime(receptionCounterProcessingTime[i])
                receptionCounter[i] = addedCustomer
            else:
                receptionCounter[i] = 0


def proceessMaintenanceCounter(maintenanceCounter, maintenanceQueue, maintenanceCounterProcessingTime, m, a, b, answer):
    for j in range(1, m + 1):
        if maintenanceCounter[j] == 0:
            if maintenanceQueue:
                addedCustomer = maintenanceQueue.pop()
                addedCustomer.setMaintenanceNumber(j)
                addedCustomer.setRemainProcessingTime(maintenanceCounterProcessingTime[j])
                maintenanceCounter[j] = addedCustomer
            continue

        customer = maintenanceCounter[j]
        customerRemainTime = customer.getRemainProcessingTime()
        customerRemainTime -= 1

        if customerRemainTime == 0:
            if customer.getReceptionNumber() == a and customer.getMaintenanceNumber() == b:
                answer += customer.getCustomerNumber()

            if maintenanceQueue:
                addedCustomer = maintenanceQueue.pop()
                addedCustomer.setMaintenanceNumber(j)
                addedCustomer.setRemainProcessingTime(maintenanceCounterProcessingTime[j])
                maintenanceCounter[j] = addedCustomer
            else:
                maintenanceCounter[j] = 0
        else:
            customer.setRemainProcessingTime(customerRemainTime)

    return answer


for test in range(1, testCase + 1):
    n, m, k, a, b = map(int, input().split())

    # 초기화
    receptionCounterProcessingTime = list(map(int, input().split()))
    receptionCounterProcessingTime.insert(0, 0)
    maintenanceCounterProcessingTime = list(map(int, input().split()))
    maintenanceCounterProcessingTime.insert(0, 0)

    # 도착 시간
    comeInTime = collections.deque(list(map(int, input().split())))

    # 창구 및 대기줄 초기화
    receptionCounter = [0 for _ in range(n + 1)]
    maintenanceCounter = [0 for _ in range(m + 1)]
    receptionQueue = collections.deque([])
    maintenanceQueue = collections.deque([])

    # 매초마다.
    answer = 0
    k = 0
    for t in range(2300):
        k = comeInReceptionQueue(t, comeInTime, receptionQueue, k)
        proccessReceptionCounter(receptionCounter, receptionQueue, maintenanceQueue, receptionCounterProcessingTime, n)
        answer = proceessMaintenanceCounter(maintenanceCounter, maintenanceQueue, maintenanceCounterProcessingTime, m,
                                            a, b,
                                            answer)

        if not comeInTime and not findCounter(receptionCounter,n) and not findCounter(maintenanceCounter,m):
            break

    if answer == 0:
        answer = -1

    print("#{} {}".format(test, answer))


