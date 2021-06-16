import itertools
# Task 1 Extend UnorderedList Implement append, index, pop, insert methods for UnorderedList. Also implement a slice
# method, which will take two parameters `start` and `stop`, and return a copy of the list starting at the position and
# going up to but not including the stop position.
class Unordered_list:
    def __init__(self):
        self.unorder_list = []

    def append(self, data):
        self.unorder_list.append(data)
        return self.unorder_list

    def __index__(self, element):
        if not element in self.unorder_list:
            return ('Element is absent in list')
        else:
            element_for_index = self.unorder_list.index(element)
        return element_for_index


    def pop(self):
        while len(self.unorder_list) >= 1:
            return self.unorder_list.pop()


    def insert(self, i, x):
        if i <= len(self.unorder_list) - 1:
            self.unorder_list[i] = x
            return self.unorder_list
        raise IndexError


    def slice(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self):
        return str(self.unorder_list)

if __name__ == '__main__':
    unord_list= Unordered_list()
    for i in range(1, 15):
        unord_list.append(i)
    unord_list.insert(5, 10)
    print(unord_list.__index__(7))


#Task 0
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def __repr__(self):
        next_n = self.root
        res = ''

        while next_n:
            res += str(next_n.data) + '->'
            next_n = next_n.next_node
        return res


if __name__ == '__main__':
    my_list = LinkedList()
    list = [[1, 2, 5, 78, 91], [3, 6, 12, 43], [4, 100]]
    all_lists = []
    for i in list:
        all_lists.extend(i)
        all_lists.sort(reverse=True)

    for i in all_lists:
        my_list.add(i)
    print(my_list)

