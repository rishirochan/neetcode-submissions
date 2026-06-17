class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter1 = Counter(s1)
        window = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if window == counter1:
                return True
            else:
                window[s2[i]] += 1
                left_val = i - len(s1)
                window[s2[left_val]] -= 1
                if window[s2[left_val]] == 0:
                    del window[s2[left_val]]
        return window == counter1