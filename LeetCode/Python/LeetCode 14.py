class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
        return ""

    smallest = min(strs)  # Get the shortest word among the strings

    for letter in range(len(smallest)):
        for last in strs:
            if letter >= len(last) or smallest[letter] != last[letter]:
                return smallest[:letter]  # Return the common prefix found so far
    return smallest 