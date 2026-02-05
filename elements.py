
def count_elements(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return counts


print(count_elements([1, 2, 2, 3, 3, 3]))

