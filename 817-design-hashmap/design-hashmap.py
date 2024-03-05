# Helper function to encapsulate bucket's functionality of the HashMap
class Bucket:
    def __init__(self):
        # Initialize your bucket data structure here, e.g., a list to hold the key-value pairs
        self.bucket = []
    
    def get(self, key):
        # Iterate over the bucket to find the key-value pair and return the value
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        # Update the value for the key if it exists, otherwise add the key-value pair
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))

    def remove(self, key):
        # Remove the key-value pair from the bucket if it exists
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]
                break


class MyHashMap:

    def __init__(self):
        self.key_space = 1024 # A prime number for better distribution (Slightly bigger than 10^4) (constraint*)
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)