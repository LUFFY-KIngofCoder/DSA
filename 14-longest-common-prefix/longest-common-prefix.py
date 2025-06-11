class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(1,len(strs)):
            l = strs[i]
            while not l.startswith(pre):
                pre = pre[:-1]
            if pre == []:
                return ""
            
        return pre
