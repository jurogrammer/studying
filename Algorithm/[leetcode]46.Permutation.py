class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        rstList = []

        def _permute(N, visited, path):
            if visited == (1 << N) - 1:
                temp = []
                for n in path:
                    temp.append(nums[int(n)])
                rstList.append(temp)
                return

            for i in range(N):
                if (visited & 1 << i):
                    continue
                else:
                    _permute(N, visited | 1 << i, path + str(i))

        _permute(N, 0, '')
        return rstList
