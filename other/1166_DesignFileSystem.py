from collections import defaultdict

# The TrieNode data structure.
class TrieNode(object):
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name = name
        self.value = -1

class FileSystem:

    def __init__(self):
        
        # Root node contains the empty string.
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        
        # Obtain all the components
        components = path.split("/")
        
        # Start "curr" from the root node.
        cur = self.root
        
        # Iterate over all the components.
        for i in range(1, len(components)):
            name = components[i]
            
            # For each component, we check if it exists in the current node's dictionary.
            if name not in cur.map:
                
                # If it doesn't and it is the last node, add it to the Trie.
                if i == len(components) - 1:
                    cur.map[name] = TrieNode(name)
                else:
                    return False
            cur = cur.map[name]
        
        # Value not equal to -1 means the path already exists in the trie. 
        if cur.value!=-1:
            return False
        
        cur.value = value
        return True

    def get(self, path: str) -> int:
        
        # Obtain all the components
        cur = self.root
        
        # Start "curr" from the root node.
        components = path.split("/")
        
        # Iterate over all the components.
        for i in range(1, len(components)):
            
            # For each component, we check if it exists in the current node's dictionary.
            name = components[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value