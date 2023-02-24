class Solution:
    def isValid(self, s: str) -> bool:
        mirror = {"(": ")", "{":"}", "[": "]" }
        
        class Node:
            def __init__(self, data = None, next = None):
                self.data = data
                self.next = next

        class Stack:
            def __init__(self):
                self.head = None
                

            def push(self, data):
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            
            def pop (self):
                if self.head:
                    temp = self.head.data
                    self.head = self.head.next
                    return temp
                return False

            def __str__(self):
                if self.head:
                    return self.head.data
                else:
                    return "None"

        stack = Stack()
        for char in s:
            # if char is a left item put on top of stack
            if char in mirror:
                stack.push(char)
            # if stack has an item and the char is a right item
            # check if they are mirrors
            elif stack.head and char == mirror[stack.head.data]:
                    stack.pop()
            else:
                return False
        #if we get to end of input return True only if stack is empty 
        return not stack.head