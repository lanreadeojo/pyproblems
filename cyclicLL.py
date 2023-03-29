def cyclicLL(node):
    if node.next is None:
        return False
    slow = node
    fast = node
    while node.next and node.next.next:
        slow = node.next
        fast = node.next.next
        if slow == fast:
            return True
    return False

def compBinaryTrees(node1, node2):
    if node1 is None and node2 is None:
        return True
    if (node1.left and node2.left and node1.right and node2.right) != None:
            if (node1.val == node2.val):
                if (compBinaryTrees(node1.left,node2.left) and compBinaryTrees(node1.right,node2.right))==False:
                    return False
                else:
                    return True
    else:
        return False

                
        



        
    
        
    
        
        
         
