class Solution:
    @classmethod
    def is_anagram(cls, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash_map = {}
        t_hash_map = {}
        for i in range(len(s)):
            s_hash_map[s[i]] = 1 + s_hash_map.get(s[i], 0)
            t_hash_map[t[i]] = 1 + t_hash_map.get(t[i], 0)

        return s_hash_map == t_hash_map 
