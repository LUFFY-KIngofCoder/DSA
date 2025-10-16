
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nse_i = [0]*n
        pse_i = [0]*n
        stn = []
        stp = []
        
        for i in range(n):
            while stn != [] and arr[stn[-1]] >= arr[n-i-1]:
                stn.pop()
            while stp != [] and arr[stp[-1]] > arr[i]:
                stp.pop()
            
            nse_i[n-i-1] = stn[-1] if stn!=[] else n
            pse_i[i] = stp[-1] if stp!=[] else -1

            stn.append(n-i-1)
            stp.append(i)

        print(nse_i)
        print(pse_i)

        total = 0

        for i in range(n):

            ps = i - pse_i[i]
            ns = nse_i[i] - i

            c = ps*ns
            total += c*arr[i]
            print(total)
        mod = 10**9 + 7
        return total%mod

        

