class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:

        '''
        The intuition is to maintain two majority elements because at max there can be only two nos in the array that appears
        for more than N/3 times. As soon as we get a nos which is neither equal to ME1 and ME2, we reduce the count of both ME1
        and ME2 by 1. At last, we will have ME1 and ME2 with us. We will iterate over the array again and count the frequency of
        ME1 and ME2 and check if it is greater than N/3. If both are > than N/3 then return both. If one of them is > N/3 then
        return that one. If none follows then return an empty array.
        '''
        ME1 = None
        ME2 = None
        count1 = 0
        count2 = 0
        threshold = (len(arr) // 3) + 1

        for num in arr:

            if num == ME1:  # increment count1 by 1 when num is equal to ME1
                count1 += 1

            elif num == ME2:  # increment count2 by 1 when num is equal to ME2
                count2 += 1

            elif ME1 is None:  # we are setting ME1 first
                ME1 = num
                count1 += 1
            
            elif ME2 is None:  # after setting ME1 we will set ME2
                ME2 = num
                count2 += 1

            else:  # if num is neither equal to ME1 nor ME2 then reduce their count by 1
                count1 -= 1
                count2 -= 1

                if count1 == 0:  # if ME1 count becomes 0 then set ME1 to None again
                    ME1 = None
                if count2 == 0:  # if ME2 count becomes 0 then set ME2 to None again
                    ME2 = None

        count1 = 0
        count2 = 0

        for num in arr:  # iterate over the array again and count ME1 and ME2 frequencies
            if ME1 == num:
                count1 += 1
            elif ME2 == num:
                count2 += 1

        if count1 >= threshold and count2 >= threshold:  # if both are > than N/3 then return both
            return [ME1, ME2]
        elif count1 >= threshold and count2 < threshold:  # if ME1 count is > than N/3 then return ME1
            return [ME1]
        elif count1 < threshold and count2 >= threshold:  # if ME2 count is > than N/3 then return ME2
            return [ME2]
        else:  # if none of them follows then return an empty array
            return []
