class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self

        

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        new_node = Node(data)
        if self.count > 0:
            new_node.previous = self.end
            self.end.next = new_node
            self.head.previous = new_node
            new_node.next = self.head
        else:
            self.head = new_node
        self.end = new_node
        self.count += 1
        return True

    def add_at_head(self, data) -> bool:
        new_node = Node(data)
        if self.count > 0:
            new_node.next = self.head
            new_node.previous = self.end
            self.head.previous = new_node
            self.end.next = new_node
        else:
            self.end = new_node
        self.head = new_node
        self.count += 1
        return True

    def add_at_index(self, index, data) -> bool:
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            return self.add_at_head(data)
        if index == self.count:
            return self.add_at_tail(data)
        new_node = Node(data)
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next
        new_node.previous = curr_node.previous
        new_node.next = curr_node
        curr_node.previous.next = new_node
        curr_node.previous = new_node
        self.count += 1
        return True

    def get(self, index) -> int:
        if index < 0 or index >= self.count:
            return -1
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next
        return curr_node.data

    def delete_at_index(self, index) -> bool:
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            temp = self.head
            temp.next.previous = self.end
            self.end.next = temp.next
            self.head = temp.next
            self.count -= 1
            return True
        
