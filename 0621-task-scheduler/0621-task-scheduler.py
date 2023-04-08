class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # null case
        if tasks is None:
            return 0
        
        freq_map = defaultdict(int)
        max_freq = 0
        
        for task in tasks:
            if task in tasks:
                freq_map[task] += 1
                max_freq = max(max_freq, freq_map[task])
        
        max_count = 0
        for key in freq_map:
            if freq_map[key] == max_freq:
                max_count += 1
        
        # Maths
        partitions = max_freq - 1
        available_slots = partitions * (n-(max_count-1))
        pending_tasks = len(tasks) - (max_freq*max_count)
        empty_slots = max(0, (available_slots-pending_tasks))
        return len(tasks) + empty_slots