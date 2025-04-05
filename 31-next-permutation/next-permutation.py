class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        i = len(arr) - 1
        break_index = None
        max = arr[-1]
        max_ele_index = -1
        diff = float('inf')
        second_max_ele_index = -1

        while i >= 1:

            if arr[i] > max:
                max = arr[i]
                max_ele_index = i

            temp_diff = max - arr[i]

            if temp_diff < diff and arr[i] != max:
                diff = temp_diff
                second_max_ele_index = i

            if arr[i] > arr[i - 1]:
                break_index = i - 1
                break

            i -= 1

        if break_index is not None:

            index = -1
            for i in range(len(arr) - 1, break_index, -1):

                if arr[break_index] < arr[i]:
                    index = i
                    break

            temp = arr[index]
            arr[index] = arr[break_index]
            arr[break_index] = temp
            
            arr[break_index + 1: ] = sorted(arr[break_index + 1: ])


        else:  # case where everything was sorted in descending order
            i = 0
            j = len(arr) - 1

            while i < j:  # swap all the elements, basically sort the array in the ascending order
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

                i += 1
                j -= 1
        