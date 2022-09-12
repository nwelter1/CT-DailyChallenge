class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:
    
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None]*self.capacity
        
    def hashIt(self, key):
        return hash(key) % self.capacity
    
    def put(self, key: int, value: int) -> None:
        idx = self.hashIt(key)
        node = self.buckets[idx]
        if not node:
            self.buckets[idx] = Node(key, value)
            return
        while node:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def get(self, key: int) -> int:
        idx = self.hashIt(key)
        node = self.buckets[idx]
        if not node:
            return -1
        while node and node.key != key:
            node = node.next
        return node.value if node else -1

    def remove(self, key: int) -> None:
        index = self.hashIt(key)
        node = self.buckets[index]
        prev = None
		# 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
		# Now, node is either the requested node or none
        if node is None:
			# 3. Key not found
            return None
        else:
			# 4. The key was found.
            self.size -= 1
            result = node.value
			# Delete this element in linked list
            if prev is None:
                self.buckets[index] = node.next # May be None, or the next match
            else:
                prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result 
            return result