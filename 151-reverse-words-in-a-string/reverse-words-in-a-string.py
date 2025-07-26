class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        new = []
        for i in t:
            if i!="":
                new.append(i)

        return " ".join(new[::-1]) 