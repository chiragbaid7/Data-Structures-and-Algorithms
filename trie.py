'''
Trie is a prefix based tree data structure used to store strings 
each node represent character
from each node we create a link of nodes
the op for insert/search/delete - O(l), lookup for prefix, autocomplete
'''

class TrieNode:
  def __init__(self):
    self.children = {} #char to node mapping
    self.isEnd = False

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word):
    #Because we want to insert each character, we need traverse and check its presence in the child nodes and follow the path, if not present
    #then we create new till compelete
    node = self.root
    for ch in word:
      if ch not in node:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.isEnd = True #last node represents end of word

  def search(self, word):
    #Traverse each character if not found on that node return None or if just prefix is present and the node returned is not True(end) then return None
    node = self.__find_node(word)
    return node is not None and node.isEnd

  def __find_node(self, word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        return None
      node = node.children[ch]
    return node
  
  def delete(self, word):
    #DFS -> we reach the end of word and then we mark isEnd and remove the nodes if apt
    #BASE CASE:- complete word no children -> safe to remove the key
    def __delete(node, word, depth):
      # end of word case
      if depth == len(word):
        if not node.isEnd:
          return False #edge case word not present
        node.isEnd = False #no the word doesn't exist, as we have marked the 
        return len(node.children) == 0 #can delete this node as there are no children (cde only word, cdefnot there)
      #recursion + work
      ch = word[depth]
      if ch not in node.children:
        return False
      should_delete = __delete(node.children[ch], word, depth + 1)
      if should_delete:
        #remove the character
        del node.children[ch]
        return not node.isEnd and len(node.children) == 0 #case which tells if we want to remove this node as well
      return False
      
      
      
