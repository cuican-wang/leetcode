class Solution(object):
    def fizzBuzz(self, n):
        l = list(range(1,n+1))
        for i in range(n):
            if l[i]%3==0 and l[i]%5==0:
                l[i]="FizzBuzz"
            elif l[i]%3==0 and not l[i]%5==0:
                l[i]="Fizz"
            elif l[i]%5==0 and not l[i]%3==0:
                l[i]="Buzz"
            else:
                l[i]=str(l[i])
        return l
# test
x= Solution()
print(x.fizzBuzz(n=16))
