class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count, t_count = {}, {}

        for sl in s:
            if sl not in s_count:
                s_count[sl] = 1
            else:
                s_count[sl] += 1

        for tl in t:
            if tl not in t_count:
                t_count[tl] = 1
            else:
                t_count[tl] += 1

        return s_count == t_count