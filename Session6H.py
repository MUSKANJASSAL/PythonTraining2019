def squareOfNumbers(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    print("nums is:",nums)

numbers = [10, 20, 30, 40, 50]
squareOfNumbers(numbers)
print("Numbers is:",numbers)