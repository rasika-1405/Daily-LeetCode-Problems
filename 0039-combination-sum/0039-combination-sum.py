class Solution:
    result = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        
        # null case
        if candidates is None:
            return self.result
        
        self.helper(candidates, 0, target, [])
        return self.result
        
    def helper(self, candidates, i, amount, path):
        # base case
        if amount < 0 or i == len(candidates):
            return
        if amount == 0:
            self.result.append(path)
            return
        
        # logic
        # not choose
        temp = path.copy()
        self.helper(candidates, i+1, amount, temp)
        # choose
        path.append(candidates[i])
        temp = path.copy()
        self.helper(candidates, i, amount-candidates[i], temp)