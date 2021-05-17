'''
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

'''

class Solution:
    def frequencySort(self, s: str) -> str:
        d =  {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        sorted_dict = {k:v for k,v in sorted(d.items(),key = lambda item : item[1] ,reverse = True)}
        res = ''
        for i in sorted_dict:
            res += i * sorted_dict[i]
        return res
        
