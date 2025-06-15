class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        for i in range(numRows):
            a = []
            for j in range(i+1):
                if j == 0 or j == i:
                    a.append(1)
                else:  
                    a.append(li[i-1][j-1] + li[i-1][j])
            li.append(a)
    



        # for i in range(numRows):
        #     l = [1]
        #     ans = 1
        #     for j in range(i):
        #         ans = ans * (i-j)/(j+1)
        #         l.append(int(ans))
        #     li.append(l)

        return li
