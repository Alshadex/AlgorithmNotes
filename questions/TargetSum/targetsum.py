
nums = [4,2,1]
target = 1

dp = {}

def foo(i, total):
    if i == len(nums):
        return 1 if total == target else 0
    if (i, total) in dp:
        return dp[(i, total)]
    dp[(i, total)] = foo(i + 1, total + nums[i]) + foo(i + 1, total - nums[i])
    return dp[(i, total)]

print(foo(0, 0))
