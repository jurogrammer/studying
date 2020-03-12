def QuickSort(l,r):
    if l<r:
        i = l + 1
        j = r
        p = l
        while i<j:
            while nums[i] < nums[p] and i<j:
                i+=1
            while nums[j] >= nums[p] and i<=j:
                geek          j-=1

            if i < j:
                nums[i],nums[j] = nums[j],nums[i]

        if nums[p] > nums[j]:
            nums[p],nums[j] = nums[j], nums[p]
        QuickSort(l,j-1)
        QuickSort(j+1,r)


for _ in range(100):
    myList = []
    for _ in range(5):
        myList.append(random.randint(1,10))


    com1 = sorted(myList)

    nums = myList[:]
    QuickSort(0,len(nums)-1)

    if com1 != nums :
        print("망함")
        print("inputList :",myList)
        print("sort():",com1)
        print("quick():",nums)