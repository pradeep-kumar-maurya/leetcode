class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        map2 = {}
        max_count = 0
        temp_count = 0
        ans = []

        for num in nums:
            if map1.get(num) is None:
                map1[num] = 0
            else:
                map1[num] += 1
            
            if map1[num] > max_count:
                max_count = map1[num]

        for key, value in map1.items():
            if map2.get(value) is None:
                map2[value] = [key]
            else:
                map2[value].append(key)

        while max_count >= 0:
            if map2.get(max_count):
                data = map2.get(max_count)

                for num in data:
                    ans.append(num)
                    temp_count += 1
                    if temp_count == k:
                        return ans
    
            max_count -= 1
        
        return ans
