'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = {}
        for i in range(len(s)-10+1):
            test_string = s[i:i+10]
            if test_string not in res:
                res[test_string] = 1
            else:
                res[test_string] += 1
        ans = []
        for i in res:
            if res[i] > 1:
                ans.append(i)
        return ans
        
