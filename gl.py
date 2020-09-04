
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(abs(v-i) <= 1 for i,v in enumerate(A))
val=Solution()
m=int(input())
arr=list(map(int,input().split()))
print(val.isIdealPermutation(arr))
