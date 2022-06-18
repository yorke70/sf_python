class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child =  BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value) # процедура обработки

        if self.left_child is not None: # если левый потомок существует
            self.left_child.pre_order() # рекурсивный вызов функции

        if self.right_child is not None: # если правый потомок существует
            self.right_child.pre_order() # аналогично левому

    def post_order(self):
        if self.left_child is not None: # если левый потомок существует
            self.left_child.post_order() # рекурсивный вызов функции

        if self.right_child is not None: # если правый потомок существует
            self.right_child.post_order() # аналогично левому
        print(self.value) # процедура обработки

    def in_order(self):
        if self.left_child is not None:
            self.left_child.in_order()

        print(self.value)

        if self.right_child is not None:
            self.right_child.in_order()


first_node = BinaryTree(2).insert_left(7).insert_right(8)
node_7 = first_node.left_child.insert_left(1).insert_right(6)
node_6 = node_7.right_child.insert_left(5).insert_right(11)
node_8 = first_node.right_child.insert_right(9)
node_9 = node_8.right_child.insert_left(4)

first_node.in_order()
