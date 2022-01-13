from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode{'{'}val: {self.val}, next: {self.next}{'}'}"

def listtollist(array: List) -> ListNode:
    
    if array:
        temp = []
        
        for arr in array:
            temp.append(ListNode(val=arr))
        
        for i in range(len(temp)-1, 0, -1):
            temp[i-1].next = temp[i]

        return temp[0]
    else:
        return None

if __name__ == "__main__":
    #print(listtollist(array = [1,2,4])) 
    print(listtollist(array = [])) 