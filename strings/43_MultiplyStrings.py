class Solution(object):
    def multiply(self, num1, num2):
        res = 0 # output
        carry1 = 1 # carry1 takes care of num1
        
        for i in num1[::-1]: # this goes over num1 from right to left as we do normal multiplication, in the above example first 3 and then 2. 
            carry2 = 1 # takes care of num2
            for j in num2[::-1]:  # this goes over num2 from right to left as we do normal multiplication, in the above example first 6 and then 3. 
                res += int(i)*int(j)*carry1*carry2 # this is each component calculated separately and added to res
                carry2 *= 10 # after first iteration (number 6 is covered), it goes to the next number from right, which is 3 here, actually 30, right? That's why it multiplies the carry2 by 10. Similar for carry1. 
            carry1 *= 10
        return str(res)

solution = Solution()
num1, num2 = "2", "3"
print(solution.multiply(num1, num2))
num1, num2 = "123", "456"
print(solution.multiply(num1, num2))