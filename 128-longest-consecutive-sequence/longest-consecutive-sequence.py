class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        freq_set = set()
        consecutive_set = set()
        max_size = 0

        for num in nums:
            freq_set.add(num)

        for num in nums:

            temp1 = num
            temp2 = num
            size = 0

            while ((temp1 - 1) in freq_set) and ((temp1 - 1) not in consecutive_set):
                size += 1
                consecutive_set.add(temp1 - 1)
                temp1 -= 1

            while ((temp2 + 1) in freq_set) and ((temp2 + 1) not in consecutive_set):
                size += 1
                consecutive_set.add(temp2 + 1)
                temp2 += 1
            
            if size + 1 > max_size:
                max_size = size + 1

        return max_size
