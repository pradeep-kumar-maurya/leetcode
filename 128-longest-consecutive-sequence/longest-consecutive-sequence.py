class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The idea here is to just use a set and iterate over the set using a for loop and then find the consecutive
        elements using a while loop inside the for loop. The overall T.C is O(N)
        """
        num_set = set()
        max_count = 0
        for i in nums:  # create the set that would be iterated
            num_set.add(i)
        for i in num_set:  # we need to iterate over the set and not the array
            """
            If i-1 is already there in the set then we don't need to check for the consecutive elements because going
            further we would get a case where i-1 is not in the set and then our while loop will calculate all the
            consecutive elements. This steps brings down the T.C
            """
            if i-1 not in num_set:
                count = 1  # count will always start from 1
                while True:  # if i-1 is not there in the set then while loop calculates the executive elements
                    if i+1 in num_set:  # we need to check i+1 in the set
                        count += 1
                        i += 1
                    else:  # else break from the while loop
                        break
                max_count = max(count, max_count)  # calculate the max
        return max_count

        # OR

        '''
        The idea is to create two sets. One set will store the elements from the arr and the other set will store the consecutive
        elements from the arr. If element is already present in the consecutve set then skip that element. If not, first go through
        all the elements left to the current element and check if they are all there in the arr set and then go through all the
        elements right to the current element and check if they are all there in the arr set. All these left and right elments
        will be added in the consecutive set.
        '''
        # arr_set = set()
        # consecutive_set = set()
        # max_size = 0

        # for num in arr:
        #     arr_set.add(num)  # create the arr set

        # for num in arr:

        #     temp1 = num
        #     temp2 = num
        #     size = 0

        #     # go through all the elements left to the current num and all the left elements must be present in the array set but
        #     # not present in the consecutive_set
        #     while ((temp1 - 1) in arr_set) and ((temp1 - 1) not in consecutive_set):
        #         size += 1
        #         consecutive_set.add(temp1 - 1)  # keep on adding elements to the consecutive set
        #         temp1 -= 1

        #     # go through all the elements right to the current num and all the right elements must be present in the array set but
        #     # not present in the consecutive_set
        #     while ((temp2 + 1) in arr_set) and ((temp2 + 1) not in consecutive_set):
        #         size += 1
        #         consecutive_set.add(temp2 + 1)  # keep on adding elements to the consecutive set
        #         temp2 += 1
            
        #     if size + 1 > max_size:
        #         max_size = size + 1

        # return max_size