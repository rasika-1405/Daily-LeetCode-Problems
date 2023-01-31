class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        for each_string in strs:
            sorted_key = ""
            sorted_key = sorted_key.join(sorted(each_string))
            # print(sorted_key)
            if sorted_key not in group_map:
                group_map[sorted_key] = []
            group_map[sorted_key].append(each_string)
        return group_map.values()
            