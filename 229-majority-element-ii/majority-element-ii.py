class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:

        ME1 = None
        ME2 = None
        count1 = 0
        count2 = 0
        threshold = (len(arr) // 3) + 1

        for num in arr:

            if num == ME1:
                count1 += 1

            elif num == ME2:
                count2 += 1

            elif ME1 is None:
                ME1 = num
                count1 += 1
            
            elif ME2 is None:
                ME2 = num
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1

                if count1 == 0:
                    ME1 = None
                if count2 == 0:
                    ME2 = None

        count1 = 0
        count2 = 0

        for num in arr:
            if ME1 == num:
                count1 += 1
            elif ME2 == num:
                count2 += 1

        if count1 >= threshold and count2 >= threshold:
            return [ME1, ME2]
        elif count1 >= threshold and count2 < threshold:
            return [ME1]
        elif count1 < threshold and count2 >= threshold:
            return [ME2]
        else:
            return []
