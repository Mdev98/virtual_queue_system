from User import User

class Node:
    def __init__(self, data:User | dict) -> None:
        self.data = data
        self.next:Node | None = None

class Queue:
    def __init__(self):
        self.first:Node | None = None
        self.last:Node | None = None
        self.size:int = 0
        self.capacity:int = 10


    def add(self, data:User | dict) -> bool:
        
        if self.capacity == 0:
            return False
        
        new_node = Node(data)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            last = self.last
            if last is not None:
                last.next = new_node
                self.last = new_node

        self.size += 1
        self.capacity -= 1

        return True

    def remove(self) -> bool:
        if self.size == 0:
            return False
        
        if self.size == 1:
            self.last = None

        current = self.first

        if current is not None:
            next = current.next if current.next is not None else None
            self.first = next

        # Function to notify the current user

        self.size -= 1
        self.capacity += 1

        return True


if __name__ == "__main__":
    user = {
        "id" : 1,
        "name" : "Mamour",
        "email" : "mamour@example.com"
    }

    user_2 = {
        "id" : 2,
        "name" : "Amadou",
        "email" : "amadou@example.com"
    }

    user_3 = {
        "id" : 3,
        "name" : "Alice",
        "email" : "alice@example.com"
    }

    queue = Queue()
    queue.add(user)
    queue.add(user_2)
    queue.add(user_3)

    print(queue.capacity)

    queue.remove()
    queue.remove()
    queue.remove()
