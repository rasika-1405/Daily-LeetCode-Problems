class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # null case
        if gas is None:
            return -1
        
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        start_station = 0
        total_cost = 0
        
        for i in range(n):
            total_cost += gas[i] - cost[i]
            # condition to go to next station
            if total_cost < 0:
                start_station = i+1
                total_cost = 0
        
        return start_station if total_cost>= 0 else -1