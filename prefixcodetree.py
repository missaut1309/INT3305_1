class Node:
  def __init__(self):
    self.symbol = None
    self.left = None
    self.right = None

  def leftNode(self):
    return self.left
  
  def rightNode(self):
    return self.right

  def addLeft(self):
    if self.left == None:
      self.left = Node()

  def addRight(self):
    if self.right == None:
      self.right = Node()

class PrefixCodeTree:
  def __init__(self):
    self.root = Node()

  def addNode(self, codeword, symbol):
    node = self.root
    for bit in codeword:
      if bit == 1:
        node.addRight()
        node = node.right
      elif bit == 0:
        node.addLeft()
        node = node.left
    node.symbol = symbol

  def decode(self, encodedData, datalen):
    rootNode = self.root
    binArr = []
    result = " "
    
    for i in encodedData:
      binArr += bin(i)[2:].zfill(8)
    binArr = binArr[:datalen]
    
    print(binArr)
    count = 0
    for bit in binArr:
      count += 1
      if bit == '1':
        rootNode = rootNode.right
      elif bit == '0':
        rootNode = rootNode.left 
      if rootNode.symbol != None: 
        result += rootNode.symbol + "    "*count
        rootNode = self.root
        count = 0
    return result

if __name__ == "__main__" :
  codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1],
  }

  codeTree = PrefixCodeTree()

  for symbol in codebook:
    codeTree.addNode(codebook[symbol], symbol)
  
  message = codeTree.decode(b'\xd2\x9f\x20', 21)

  print(message)