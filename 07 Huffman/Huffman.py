import heapq
from collections import Counter
from numpy import character

class Tree:
    def __init__(self, character, frequency, left = None, right = None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.frequency < other.frequency

def buildTree(text):
    counter = Counter(text)
    pq = [Tree(ch, counter[ch]) for ch in counter]
    heapq.heapify(pq)
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        parent = Tree(None, left.frequency + right.frequency, left, right)
        heapq.heappush(pq, parent)
    return heapq.heappop(pq)


def buildMap(root):
    def dfs(root, code, encodingMap):
        if root.character:
            encodingMap[root.character] = ''.join(code)
        else:
            code.append('0')
            dfs(root.left, code, encodingMap)
            code.pop()
            code.append('1')
            dfs(root.right, code, encodingMap)
            code.pop()
    encodingMap = {}
    dfs(root, [], encodingMap)
    return encodingMap

def encode(text):
    root = buildTree(text)
    encodingMap = buildMap(root)
    print(encodingMap)
    return ''.join([encodingMap[character] for character in text])

def decode(encoded, root):
    if root.character:
        return root.character * len(encoded)
    decoded = []
    node = root
    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.character:
            decoded.append(node.character)
            node = root
    return ''.join(decoded)


x = 'abcbbcaaabcdbcadaacbxyyyy'

arbol = buildTree(x)
encoded = encode(x)
print(encoded)
print(decode(encoded, arbol))