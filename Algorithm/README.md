# algorithm 중요

#### 1.while (left < right) :
left와 right가 차이 날 때 while문을 동작한다.

#### 2.QuickSort :
C++은 while (arr[i] <= arr[p]) i++;
위 코드에서 인덱스에러는 안남. 다음 메모리값참조하고 while문 빠져나감. (pointer이기 때문이고 다음 메모리가 할당받은 메모리내에 있나봄)
따라서 python은 위 부분 수정할 필요있음. 코드가 좀 복잡해진다.
```
def QuickSort(l,r):
    if l<r:
        i = l + 1
        j = r
        p = l
        while i<j:
            while nums[i] < nums[p] and i<j:
                i+=1
            while nums[j] >= nums[p] and i<=j:
                j -= 1

            if i < j:
                nums[i],nums[j] = nums[j],nums[i]

        if nums[p] > nums[j]: # 2 9 케이스 때문에.
            nums[p],nums[j] = nums[j], nums[p]
        QuickSort(l,j-1)
        QuickSort(j+1,r)
```
