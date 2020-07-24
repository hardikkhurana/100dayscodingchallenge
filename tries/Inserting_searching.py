# Tries are really efficient for string range queries
# Let's suppose we have records :
# ['Tea', 'slice', 'tree', 'poker', 'thapar'....]
# searching for some strings => "to", "Tea" etc....
# Hashing is an important idea which can be efficient, there is a tradeoffs between
# time and space for small records and large records.
# We will use idea of HashMaps to Create Tries where each node contains HashMaps which maps
# chars (the children of current root) to their corresponding Node.
# This will help in searching efficiently, as we are just going to search long down the tree.
# TIME for serching will be at best 0(M), M is length of string.

# So, every node has its own hashtable which contains keys as the char it holds, and the
# nodes address it points to.
# So, it can be seen that while searching is faster for set of larger records as there is no
# scope for hash collisions, or computing time for hashing is not required, but one of the cons
# of using Trie is higher space requirements (as we are storing each char in separate node)
# unlike hash which generally allocates whole chunk to the complete key instead of char by char.

# FOR WORDS LIKE "THE", "A", "THERE".....
#     ROOT
#     |  |
#     T  A
#     H
#     E
#      R
#      E
#
# If only the queries are needed, then we have shown here, HashTables using dict in python.
# BUT IF ANYWHERE ORdering is also important, then we need to keep a List names as
# CHILDREN[MAX] , where MAX will be 26 if considering only lower case, or 256 in general.
# and also we can keep an mapping using ord().

class TrieNode:

    def __init__(self, data):
        self.data = data
        self.children = {}
        self.terminal = False


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, key):

        ptr = self.root
        for i in range(len(key)):
            ch = key[i]

            if ch not in ptr.children:
                ptr.children[ch] = TrieNode(ch)

            ptr = ptr.children[ch]

        ptr.terminal = True

    def search(self, key):

        ptr = self.root
        for i in range(len(key)):

            ch = key[i]
            if ch not in ptr.children:
                return False

            ptr = ptr.children[ch]

        return ptr.terminal

    def isEmpty(self, ch):
        if len(self.root.children[ch]):
            return False

        return True

    def search_root(self):
        print(self.root.children)

    def Pretty_print(self, keys):
        for i in range(len(keys)):
            ptr = self.root.children[keys[i][0]]
            print(f"{ptr.data} ", end = "")
            for j in range(1, len(keys[i])):
                ptr = ptr.children[keys[i][j]]
                print(f"{ptr.data} ", end = "")
            print()

if __name__ == '__main__':

    t = Trie()
    keys = ["the", "a", "there", "answer", "any", "by", "their", "sourav"]
    for i in keys:
        t.insert(i)
    print(t.search('sourav'))
    t.search_root()
    t.Pretty_print(keys)
