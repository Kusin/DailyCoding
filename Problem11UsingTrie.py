# using Trie Data Structure
# O(nm) preprocess
# O(m) find

# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:

    def __init__(self):
        self.nodes = {} # declaration of instance variable

    def insert(self, word: str) -> None:
        node = self.nodes
        word = word.lower()
        for i,char in enumerate(word):
            if char not in node:
                break
            node=node[char]
        else:
            i+=1
        
        for char in word[i:]:
            node[char]={}
            node=node[char]
        node['#']={} # '#' is a an end sign
        # print(self.nodes)
        
    def search(self, word: str) -> bool:
        node = self.nodes
        word = word.lower()
        for char in word:
            if char not in node:
                return False
            node = node[char]
        if '#' in node:
            return True
        return False
    
    def ExiststartsWith(self, prefix: str) -> bool:
        node = self.nodes
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
    
    def possibleSuffix(self, node) ->list:
        strings=[]
        for char in node.keys():
            if char=='#':
                strings.append('')
            else:
                nextsuffixs = self.possibleSuffix(node[char])
                for string in nextsuffixs:
                    strings.append(char+string)
        return strings
    
    def startsWith(self, prefix : str) -> list:
        node = self.nodes
        for char in prefix:
            if char not in node:
                return ["***No Such String***"]
            node = node[char]
        suffixs = self.possibleSuffix(node)
        return list([prefix+string for string in suffixs])
            
            
def main():
    T = Trie()
    # processing strings into lowercas implemented in Trie.
    # string = "APPLEISGOOD123"
    # T.insert(string.lower())
    T.insert("Apple")
    T.insert("apP")
    T.insert("what")
    T.insert("apishard")
    print(T.startsWith("app"))
    print(T.startsWith("p"))
if __name__=="__main__":
    main()

# Will be called as below
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# List = obj.startsWith(prefix)
    