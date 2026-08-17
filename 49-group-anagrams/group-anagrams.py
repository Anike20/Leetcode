from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary to hold lists of anagrams, default value is a new list
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a canonical key for the anagram group
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists from the dictionary
        return list(anagram_map.values())