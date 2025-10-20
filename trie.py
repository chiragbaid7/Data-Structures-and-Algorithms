'''
Trie is a prefix based tree data structure used to store and retrive strings efficiently
the op for insert/search/delete - O(l), lookup for prefix, autocomplete
https://chatgpt.com/c/68f5cc49-022c-8323-ae3f-b799e9701de1
'''

class TrieNode:
  def __init__(self):
    self.children = {} #map each character to node(children)
    self.isEnd = False
  def insert(self, word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.isEnd = True
  def search(self, word):
    



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
      if ch not in node.children:
        node.children[ch] = TrieNode()
      node = node.children[ch]
    node.isEnd = True #last probably empty node represents end of word

  def search(self, word): # we need to search the complete word not the prefix
    node = self.__find_node(word)

  def __find_node(self, word):
    node = self.root
    for ch in word:
      if ch not in node.children:
        return None
      node = node.children[ch]
    return node

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

  def delete(self, word, index):
    #base case -> when we reach the end of word expidiation
    if len(word) == depth:
      if not node.isEnd:
        return False
      node.isEnd = True
      return len(node.children) == 0 
    ch = word[index]
    if ch not in node.children:
      return False
    should_delete = 
    if should_delete:
      del node.chlidren[ch]
        
  
  def delete(self, word):
    #DFS -> we reach the end of word and then we mark isEnd and remove the nodes if apt
    #BASE CASE:- complete word no children -> safe to remove the key
    def __delete(node, word, index):
      # end of word case,  # catab , but word -> cat
      if index == len(word):
        if not node.isEnd:
          return False #edge case word not present
        node.isEnd = False #no the word doesn't exist, as we have marked the 
        return len(node.children) == 0 #can delete this node as there are no children (cde only word, cdefnot there)
      #recursion + work
      ch = word[depth]
      if ch not in node.children:
        return False
      should_delete = __delete(node.children[ch], word, index + 1)
      if should_delete:
        #remove the character
        del node.children[ch]
        return not node.isEnd and len(node.children) == 0 #case which tells if we want to remove this node as well
      return False
    return __delete(self.root, word, 0)
  
  def autoComplete(self, prefix):
    #lets say this function is called for each search - app
    #follow the path till isEnd not encountered
    node = self.__find_node(prefix)
    if not node:
      return []
    search_results = []
    def dfs(node, currentPath):
      #B.C for a word
      if node.isEnd:
        search_results.append("".join(currentPath)) #['a', 'p', 'p', 'l']
      #traverse from current node and append each character
      for ch, child in node.children.items():
        #[a,p,p] + [l, e], [a,p,p] + ['c,', a
        dfs(child, currentPath + [ch])
    dfs(node, list(prefix))
    return search_results

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")
    trie.insert("bat")
    trie.insert("ball")

    print(trie.search("apple"))        # True
    print(trie.search("appl"))         # False
    # print(trie.starts_with("app"))     # True
    print(trie.autoComplete("app"))    # ['app', 'apple', 'application']

    trie.delete("apple")
    print(trie.search("apple"))        # False
    print(trie.autoComplete("app"))    # ['app', 'application']
        
    
      
      
