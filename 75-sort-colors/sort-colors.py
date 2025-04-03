class Solution:
    def sortColors(self, arr: List[int]) -> None:

        length = len(arr)

        for _ in range(len(arr)):

            m = 0
            n = m + 1

            while n < length:

                if arr[m] > arr[n]:  # swap

                    temp = arr[n]
                    arr[n] = arr[m]
                    arr[m] = temp

                m += 1
                n += 1

            # (length - 1) is used to avoid extra iterations because after every iteration, the max no. will be at the end
            length -= 1
        