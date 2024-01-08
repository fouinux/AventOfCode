cache = dict()

def solve(test, nums):

    if test == '':
        return 1 if nums == () else 0

    if nums == ():
        return 0 if '#' in test else 1

    result = 0

    if (test, nums) in cache.keys():
        return cache[(test, nums)]

    if test[0] in '.?':
        result += solve(test[1:], nums)

    if test[0] in '#?':
        if nums[0] <= len(test):
            if '.' not in test[:nums[0]]:
                if (nums[0] == len(test)) or (test[nums[0]] != '#'):
                    result += solve(test[nums[0] + 1:], nums[1:])

    cache[(test, nums)] = result
    return result

result = 0
lines = open("input").readlines()
for l in lines:
    test, nums = l.strip().split(' ')
    test = (test + "?") * 4 + test
    nums = tuple(map(int, nums.strip().split(',')))
    nums = nums * 5
    result += solve(test, nums)

print(result)
