class BinarySearch:
    def __init__(self, numbers):
        self.numbers = sorted(numbers)

    def search(self, key):
        left = 0
        right = len(self.numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.numbers[mid] == key:
                return mid
            elif self.numbers[mid] > key:
                right = mid - 1
            else:
                left = mid + 1

        return -1


nums = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter target: "))

obj = BinarySearch(nums)
result = obj.search(key)

print(result)