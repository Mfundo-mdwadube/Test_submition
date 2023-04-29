class AnagramGrouper:
    """
    Class to group anagrams in a list of strings.

    Attributes:
        None

    Methods:
        group_anagrams: Groups anagrams in a list of strings.

    Example Usage:
        >>> ag = AnagramGrouper()
        >>> ag.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    def group_anagrams(self, strs):
        """
        Groups anagrams in a list of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            List[List[str]]: A list of lists of strings, where each list contains anagrams.
        """
        anagram_groups = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s].append(s)
            else:
                anagram_groups[sorted_s] = [s]
        return list(anagram_groups.values())

ag = AnagramGrouper()
print(ag.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
