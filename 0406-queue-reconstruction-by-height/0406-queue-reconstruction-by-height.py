class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        
        for person in sorted_people:
            result.insert(person[1], person)
        
        return result
