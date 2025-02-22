class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}
        i = -1
        m = -1

        for char in s1:
            if s1_dict.get(char) is None:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        
        for char in s2:
            m += 1
            if s1_dict.get(char) is None:
                s2_dict = {}
                i = m
                continue

            else:                
                if s2_dict.get(char) is None:
                    s2_dict[char] = 1
                else:
                    s2_dict[char] += 1
                
                if s2_dict.get(char) > s1_dict.get(char):
                    while i < len(s2):
                        
                        i += 1
                        
                        if s2_dict.get(s2[i]):
                            s2_dict[s2[i]] -= 1

                            if s2_dict[s2[i]] == 0:
                                s2_dict.pop(s2[i])
                        
                        if s2_dict[char] == s1_dict[char]:
                            break
                    
                if s1_dict == s2_dict:  # T.C = O(26)
                    return True

        return False
