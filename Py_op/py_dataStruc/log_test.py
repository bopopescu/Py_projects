#520

test = dict([('wifi', 2),("bt",3),('AC',4)])

test_1 = [("mu",5),("su",6),("su", 7)]

test.update(test_1)

print(type(test.items()))
test2 = list(test.items())
for i in test2:
    print(i, sep="; ")

#520

#643
def findM(nums,k):
    pass
    nums_len = len(nums)
    if nums_len < 1:
        return 0
    if nums_len <= k:
        return sum(nums) / k
    max_avg = sum(nums[0:k]) / k
    for i in range(1, nums_len-k):
        new_avg = sum(nums[i:i+k]) / k
        max_avg = new_avg if new_avg > max_avg else max_avg
    return max_avg
#645
#def findErrorN(nums):


for i in range(1,2):
    print(i)

moorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","-- ","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]