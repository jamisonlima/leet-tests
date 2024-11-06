class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        # create trie
        root = {}
        for word in strs:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict["_end"] = "_end"

        #look for biggest dict with len == 1
        prefix = ""
        current_dict = root
        while len(current_dict) == 1:
            key = next(iter(current_dict))
            if key != "_end":
                prefix += key
                current_dict = current_dict[key]
            else: break
        return prefix
