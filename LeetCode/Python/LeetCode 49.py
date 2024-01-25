# Medium Problem
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list) # Create the hashmap
    result = [] # Create the result list

    for s in strs:
      sorted_s = tuple(sorted(s)) # Sort the word (ex: "bta" -> "abt") and put it in a tuple
      anagram_map[sorted_s].append(s)

    for value in anagram_map.values():
      result.append(value)
    
    return result