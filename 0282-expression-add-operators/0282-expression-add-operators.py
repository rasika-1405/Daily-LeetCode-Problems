class Solution:
    result = []
    def addOperators(self, num: str, target: int) -> List[str]:
        self.result = []
        self.helper(num, 0, target, "", 0, 0)
        return self.result
    
    
    def helper(self, num, pivot, target, path, calculated_val, tail_val):
        # base case
        if pivot == len(num):
            if calculated_val == target:
                self.result.append(path)
        
        # logic - for loop recursion
        for i in range(pivot, len(num)):
            # preceding 0
            if num[pivot] == "0" and i!= pivot:
                continue
            length = len(path)
            curr = int(num[pivot:i+1])
            # need to handle first level separation (no operators)
            if pivot == 0:
                #action
                path = "".join(path + str(curr))
                self.helper(num, i+1, target, path, curr, curr)
                path = path[:length]
            else:
                # case +
                path = path + "+"
                path = "".join(path + str(curr))
                self.helper(num, i+1, target, path, calculated_val+curr, +curr)
                path = path[:length]
                # case -
                path = path + "-"
                path = "".join(path + str(curr))
                self.helper(num, i+1, target, path, calculated_val-curr, -curr)
                path = path[:length]
                # case *
                path = path + "*"
                path = "".join(path + str(curr))
                self.helper(num, i+1, target, path, calculated_val-tail_val+tail_val*curr, tail_val*curr)
                path = path[:length]