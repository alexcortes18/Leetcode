class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        characters_map = {}
        visited_t = set()
        for i, char in enumerate(s):
            if char not in characters_map:
                characters_map[char] = t[i]
                if t[i] not in visited_t:
                    visited_t.add(t[i])
                else: return False
            if char in characters_map:
                if t[i] != characters_map[char]: return False
        return True
    
# my solution, only with ChatGpt suggestion of using a set() rather than a list [].
    
