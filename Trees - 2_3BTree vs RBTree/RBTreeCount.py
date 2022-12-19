colors = ['Black','Red']
colors_indx = ["\033[30m","\033[31m"]


# Узел дерева
class RBnode():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RBtree():
    def __init__(self):
        # нулевая конечная нода
        self.TNULL = RBnode((0,1))
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

        # счетчики
        self.sravn = 0
        self.vkluch = 0
    
    def printTree(self, node = None, lvl = 0, last=True):
        if node == None:
            node = self.root
            print('Level №: R/L\tKey')
            print('-----------------------------') 
        s_color = colors_indx[node.color]
        if node != self.TNULL:
            print(s_color+'  '*lvl,"Level", lvl, end=": ")
            if last:
                print(s_color+"R- ",end='')
            else:
                print(s_color+"L- ",end='')
            lvl+=1

            
            print(s_color+f"{str(node.key)}")
            self.printTree(node.left, lvl, False)
            self.printTree(node.right, lvl, True)


    def _leftRotate(self, x):
        y = x.right
        self.vkluch+=1
        x.right = y.left
        if y.left != self.TNULL:
            self.vkluch+=1
            y.left.parent = x
            self.vkluch+=1
        y.parent = x.parent
        # Если родитель x равен нулю, то x был корнем, а y будет корнем
        self.vkluch+=1
        if x.parent == None:
            self.root = y
        # Иначе если x был левым дочерним элементом ,  y - левый родитель
        elif x == x.parent.left:
            x.parent.left = y
        # Иначе если x был правым дочерним элементом,  y - правого дочернего элемента родителя
        else:
            x.parent.right = y
        self.vkluch+=2
        y.left = x
        x.parent = y

    def _rightRotate(self, x):
        y = x.left
        self.vkluch+=1
        x.left = y.right
        if y.right != self.TNULL:
            self.vkluch+=1
            y.right.parent = x

        self.vkluch+=1
        y.parent = x.parent
        self.vkluch+=1
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        self.vkluch+=2
        y.right = x
        x.parent = y

    def _fixInsert(self, node):
        # пока цвет родителя красный
        while node.parent.color == 1:
            # Если родитель узла является правым дочерним
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                    self.vkluch+=1
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.vkluch+=1
                        self._rightRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self._leftRotate(node.parent.parent)
            # левый дочерний
            else:
                uncle = node.parent.parent.right

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.vkluch+=1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        self.vkluch+=1
                        node = node.parent
                        self._leftRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self._rightRotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0
    
    #вставка
    def insert(self, key):
        #новая красная нода 
        node = RBnode(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        # Поиск места вставки по дереву
        while x != self.TNULL:
            # Y - указатель на x
            y = x
            if node.key[0] < x.key[0]:
                x = x.left
            else:
                x = x.right

        # Y — указатель на родителя
        node.parent = y
        # Если родителем является none, то это корень
        if y is None:
            self.root = node
        # Помещаем элемент слева или справа
        elif node.key[0] < y.key[0]:
            y.left = node
        else:
            y.right = node
        # Если узел является корнем, цвет - черный, вставка завершена
        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return
        # Если родитель узла красный, проверяем свойства
        self._fixInsert(node)

    def search(self, key, node= None, lvl = 0, last = True):
        if node == None:
            node = self.root

        if key == node.key[0]:
            if last:
                return colors_indx[node.color] + f"{lvl, 'R', node.key, colors[node.color]}"
            else:
                return colors_indx[node.color] + f"{lvl, 'L', node.key, colors[node.color]}"
        if node == self.TNULL:
            return None
        lvl+=1
        if key < node.key[0]:
            return self.search(key,node.left, lvl, False)
        return self.search(key, node.right, lvl, True)

    def searchAndInsert(self, key, node= None, lvl = 0, last = True):
        #новая красная нода 
        node = RBnode(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        # Поиск места вставки по дереву
        while x != self.TNULL:
            # Y - указатель на x
            y = x
            self.sravn+=1
            if node.key == x.key[0]:
                x.key = (x.key[0],x.key[1]+1) # если существует
                return 
            elif node.key < x.key[0]:
                x = x.left
            else:
                x = x.right
        
        node.key=(key,1)
        # Y — указатель на родителя
        node.parent = y
        # Если родителем является none, то это корень
        if y is None:
            self.root = node
        # Помещаем элемент слева или справа
        elif node.key[0] < y.key[0]:
            self.sravn+=1
            self.vkluch+=1
            y.left = node
        else:
            self.sravn+=1
            self.vkluch+=1
            y.right = node
        # Если узел является корнем, цвет - черный, вставка завершена
        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return
        # Если родитель узла красный, проверяем свойства
        self._fixInsert(node)




if __name__ == '__main__':
    rbt = RBtree()

    for i in range(10):
        rbt.searchAndInsert(i)
        
    rbt.printTree()
    print(rbt.sravn,rbt.vkluch)