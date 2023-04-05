class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # null case
        if logs is None:
            return [0]
        
        result = [0 for _ in range(n)]
        stk = []
        prev = 0
        
        for log in logs:
            log_arr = log.split(":")
            task = int(log_arr[0])
            curr = int(log_arr[2])
            
            if log_arr[1] == "start":
                if stk:
                    result [stk[-1]] += curr - prev
                prev = curr
                stk.append(task)
            else:
                result[stk.pop()] += (curr+1) - prev
                prev = curr+1
                
        return result