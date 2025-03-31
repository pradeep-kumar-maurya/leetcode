class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        We should not be building the freq_dict ahead, instead, it should be built one by one by calculating the prefix sum in
        each step and then checking if (prefix sum - k) exits in the freq_dict or not. And later, if prefix sum does not exit in
        the freq_dict then add the prefix sum with frequency as 1 or if it exits then increment the frequency by 1.
        '''
        prefix_sum = 0
        freq_dict = {0: 1}  # 0 will be used when the prefix sum is equals to k
        count = 0

        for num in nums:
            prefix_sum += num

            # 1st -> check if we can remove any subarray from back so that we get sum = k
            difference = prefix_sum - k
            if freq_dict.get(difference):
                count += freq_dict.get(difference)

            # 2nd -> if prefix sum is there or not in the freq_dict, just insert/update the value
            if freq_dict.get(prefix_sum):
                freq_dict[prefix_sum] += 1
            else:
                freq_dict[prefix_sum] = 1

        return count
