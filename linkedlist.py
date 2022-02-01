# binary tree insertion

class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None

class BinaryTree :
    def __init__ ( self ) : self.root = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        parent = self.root
        temp = self.root
        
        while temp :
            parent = temp
            
            if temp == None : 
                temp = Node ( data )
                return
        
            if temp.data == data : return # data exists
        
            if temp.data < data : 
                temp = temp.right
                if temp == None : 
                    parent.right = Node ( data )
                    return
            elif temp.data > data : 
                temp = temp.left
                if temp == None :
                    parent.left = Node ( data )
                    return
            else : print ( " something unfathomable happened! " )
        return

    def printList ( self , node ) :
        if node == None : return
        if node.data : print ( node.data ) #data exists
        if node.left : 
            print ( " --- L of" , node.data , ":")
            self.printList ( node.left )
        if node.right : 
            print ( " --- R of" , node.data )
            self.printList ( node.right )
        return
    
    def balanceLHS ( self , node ) :
        # bring heavy node up
        parent = self.parent ( node )
        if parent == None : print ("parent not found")
        
        # case I : node has 2 children
        if node.left != None and node.right != None :
            node.right.left = node
            parent.left = node.right
            node.right = None
            
        # case II : node has left child
        elif node.left != None and node.right == None : pass
        
        # case III : node has right child
        elif node.left == None and node.right != None :
            if parent.left == node :
                parent.left = node.right
                node.right.left = node
                node.right = None
                
        return
        
    def balanceRHS ( self , node ) :
        # bring light node up
        parent = self.parent ( node )
        if parent == None : print ("parent not found")

        # case I : node has 2 children
        if node.left != None and node.right != None :
            parent.right = node.left
            if node.left.right != None : node.left = node.left.right
            else : node.left = None
            parent.right.right = node

        # case II : node has left child
        elif node.left != None and node.right == None :
            if parent.right == node :
                parent.right = node.left
                node.left.right = node
                node.left = None

        # case III : node has right child
        elif node.left == None and node.right != None : pass

        return
    
    def parent ( self , node ) :
        if node == None : return None
        temp = self.root
        parent_node = self.root
        while temp :
            if temp == node : return parent_node
            parent_node = temp
            if temp.data > node.data : temp = temp.left
            elif temp.data < node.data : temp = temp.right
            if temp == parent_node : print ("check parent")

    def toLinkedList ( self ) :
        if self.root == None : return
        
        # finding leaf node
        temp = self.root
        node = self.root
        while temp :
            if temp == None : break
            node = temp
            temp = temp.left
        
        # balancing L.H.S
        while node :
            if node == self.root : break
            self.balanceLHS ( node )
            node = self.parent ( node )
        
        # balancing R.H.S
        node = self.root.right
        parent = self.root
        while node :
            if node == None : break
            parent = node
            self.balanceRHS ( node )
            self.balanceRHS ( parent )
            node = parent.right
        
        # shifting root to smallest node
        node = self.root.left
        parent = self.root
        while node != None :
            node.right = parent
            parent.left = None
            parent = node
            node = node.left
        self.root = parent

        # the tree is now a sorted linked list with all left nodes as None


Obj = BinaryTree ()
arr = [ 5 , 3 , 8 , 2 , 6 , 4 , 9 , 1 , 7 ]
for index , value in enumerate ( arr ) : Obj.insert ( value )

print ( "values in the tree are inserted as :")
Obj.printList ( Obj.root )
Obj.toLinkedList()

print (" ")
print ( "the linked list of the tree is as :")
Obj.printList ( Obj.root )
