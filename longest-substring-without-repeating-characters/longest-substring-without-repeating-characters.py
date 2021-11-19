class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        output = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r - left + 1)
                
            else:
                if seen[s[r]] < left:
                    output = max(output, r - left + 1)
                else:
                    left = seen[s[r]] + 1
            seen[s[r]] = r
        return output
                
                