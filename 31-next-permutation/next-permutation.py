class Solution:
    def nextPermutation(self, arr: List[int]) -> None:

        i = len(arr) - 1
        break_index = None

        # We need to find the index of the element that breaks the descending order condition in the array from right to left.
        while i >= 1:

            if arr[i] > arr[i - 1]:
                break_index = i - 1
                break  # we can break as soon as we find the breaking index

            i -= 1

        if break_index is not None:

            index = -1

            '''
            We need to iterate from right to left and find the first element which is greater than arr[break_index].
            We do this because right part of the break_index will always be sorted in the descending order and therefore,
            we just need to find the first element from right which is > than arr[break_index] and swap both of them and
            then reverse the arr from (break_index + 1 till N - 1). Reversing the arr from (break_index + 1 till N - 1)
            will basically sort the array and hence we will get the next lexicographically greater permutation.
            '''
            for i in range(len(arr) - 1, break_index, -1):

                if arr[break_index] < arr[i]:
                    index = i
                    break  # break as soon as arr[i] is > than arr[break_index]

            temp = arr[index]
            arr[index] = arr[break_index]
            arr[break_index] = temp
            
            i = break_index + 1
            j = len(arr) - 1       


        # case where everything was sorted in descending order, i will be 0 and j will be N - 1
        else:
            i = 0
            j = len(arr) - 1

        # Swap all the elements, basically, sort the array in the ascending order from index i till j.
        # This swapping will be performed in both the cases.
        while i < j:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

            i += 1
            j -= 1
