# Узел дерева
from random import randint


class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.parent = None
        self.children = []

# Класс дерева
class BTree:
    def __init__(self, n):
        self.root = Node(True)  # корневой узел
        self.n = n # размерность

        # счетчики
        self.sravn = 0
        self.vkluch = 0
    
    #Отрисовка дерева
    def printTree(self, node = None, lvl=0):
        if node == None:
            node = self.root
            print('Level №: Node\tIsLeaf\tParent')
            print('-----------------------------') 
        print('  '*lvl,"Level", lvl, end=": ")
        
        for i in node.keys:
            print(i, end=" ")
        print('\t', node.leaf, end='\t')
        if node.parent==None:
            print(None)
        else:
            print([x[0] for x in node.parent.keys])

        lvl += 1
        if len(node.children) > 0:
            for i in node.children:
                self.printTree(i, lvl)

    #Поиск индекса дихтомией
    def _dichSearch(self, node, k):
        if len(node.keys)==0:
                return 0
        i, end = -1, len(node.keys)
        while True:
            self.sravn+=1 
            if k >= node.keys[(i+end)//2][0]:
                    i=(i+end)//2
            else:
                end = (i+end)//2 
                    
            if abs(i-end)<=1:
                break
        return i
    
    #Поиск 
    def search(self, k, node=None):
        if node is None:
            return self.search(k, self.root)
        else:
            #Поиск дихтомией
            i = self._dichSearch(node,k)
            if i < len(node.keys) and k == node.keys[i][0]:
                return [x[0] for x in node.keys], i
            elif node.leaf:
                return None
            else:
                return self.search(k, node.children[i+1])

    def insertInNode(self,node,element):
        i = self._dichSearch(node,element[0])+1
        self.vkluch+=1
        node.keys.insert(i,element)

        #node.keys.append(element)
        #node.keys.sort(key=lambda v: v[0])

    def searchAndInsert(self, k, node=None):
        if node is None:
            return self.searchAndInsert(k, self.root)
        else:
            #Поиск дихтомией
            i = self._dichSearch(node,k)
            self.sravn+=1
            if i < len(node.keys) and k == node.keys[i][0]:
                node.keys[i] = (node.keys[i][0],node.keys[i][1]+1) #уже существует
                return None
            elif node.leaf:
                self.insertInNode(node,(k,1))
                if len(node.keys) > (self.n) - 1 :
                    self._insertUp(node, (k,1))
                return None
            else:
                return self.searchAndInsert(k, node.children[i+1])

    #вставка наверх
    def _insertUp(self,  node = None , k = 0):
        #print('insertUp', node.keys)
        parent = node.parent

        if parent == None:
            #балансировка наследства
            self.vkluch+=1 
            self.root = Node()
            self.root.children.insert(0, node)
            
            #расщепление страницы
            result = self._splitChild(self.root, 0)
            parent = self.root
            
                 
        else:
            i = self._dichSearch(parent,k[0]) +1
            #расщепление страницы
            result = self._splitChild(parent, i)
        
        #делегат наверх 
        self.insertInNode(parent,result)
        
        #балансировка наследства
        for child in parent.children:
                child.parent = parent
                for y in child.children:
                    y.parent = child  
        
        #Если больше элементов, повторяем
        if len(parent.keys) > ( self.n) - 1:
                self._insertUp(parent, result)
           
    #вставка вниз
    def insertDown(self, k, node = None):
        #print('insertDown', node.keys)
        if node == None:
            node = self.root

        #Если лист
        if node.leaf:
            self.insertInNode(node,k)
            if len(node.keys) > (self.n) - 1 :
                self._insertUp(node, k)
                
        else:
            #иначе спускаемся в нужное поддерево
            i = self._dichSearch(node,k[0])+1
            self.insertDown(k, node.children[i])
                    
    #расщепление
    def _splitChild(self, node, i):
        #print('splitChild', i)
        self.vkluch+=1 
        n = self.n
        # y - старая нода, которую мы делим
        y = node.children[i]
        # z - новая нода, которую мы создаем
        z = Node(y.leaf)
        z.parent = node
       
        result =  y.keys[n//2 ]
        z.keys = y.keys[n//2+1: n ]
        y.keys = y.keys[0: n//2 ]
        
        node.children.insert(i + 1 , z)  
        if not y.leaf:
            z.children = y.children[n//2+1: n +1 ]
            y.children = y.children[0: n//2+1 ]
        
        return result


if __name__ == '__main__':
    B = BTree(8)
    for i in range(1,100):
        # randint(1,100)   
        #C.insertDown(i)
        B.searchAndInsert(randint(1,100))
        #B.printTree()        
    #C.printTree()
    B.printTree()