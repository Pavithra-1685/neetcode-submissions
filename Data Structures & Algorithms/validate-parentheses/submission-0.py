class Solution:
    def isValid(self, s: str) -> bool:
        map = {
           ")":"(" ,
           "}": "{", 
           "]": "["
        }
        stack = []
        for i in s:
            if i in map:
                if not stack: 
                    return False
                
                top_element = stack.pop() 
                if map[i] != top_element:
                    return False
            else:
                stack.append(i) 

        
        return len(stack) == 0

        