# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    li = []
    count = 0
    def __init__(self, nestedList: [NestedInteger]):
        # self.ni = NestedInteger()
        self.li = []
        self.dfs(nestedList)
    
    def dfs(self, nested_list):        
        # logic
        for nl in nested_list:
            if nl.isInteger():
                self.li.append(nl.getInteger())
            else:
                self.dfs(nl.getList())
    
    def next(self) -> int:
        result = self.li[self.count]
        self.count += 1
        return result
        
    
    def hasNext(self) -> bool:
         return self.count != len(self.li)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())