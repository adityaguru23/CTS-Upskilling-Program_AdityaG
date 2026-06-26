class MergeSorter:

    def merge(self, arr, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def sort(self, arr):
        if len(arr) <= 1:
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        self.sort(left)
        self.sort(right)

        self.merge(arr, left, right)


numbers = list(map(int, input().split()))

obj = MergeSorter()
obj.sort(numbers)

print("Sorted array:", numbers)