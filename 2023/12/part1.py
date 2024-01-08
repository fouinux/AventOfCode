def solve(test, nums):

    if test == '':
        return 1 if nums == () else 0

    if nums == ():
        return 0 if '#' in test else 1

    result = 0

    if test[0] in '.?':
        result += solve(test[1:], nums)

    if test[0] in '#?':
        if nums[0] <= len(test):
            if '.' not in test[:nums[0]]:
                if (nums[0] == len(test)) or (test[nums[0]] != '#'):
                    result += solve(test[nums[0] + 1:], nums[1:])
    return result

result = 0
lines = open("input").readlines()
for l in lines:
    test, nums = l.strip().split(' ')
    nums = tuple(map(int, nums.strip().split(',')))
    result += solve(test, nums)

print(result)
