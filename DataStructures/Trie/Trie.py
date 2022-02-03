class Node:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.is_ending = False
        
    def append(self, char):
        self.children[char] = Node(char)
        
    def get_child(self, char):
        return self.children[char]

    def contains(self, char):
        return char in self.children
    
    def set_end(self):
        self.is_ending = True

    def is_end(self):
        return self.is_ending



class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        '''
        Insertion is O(m) wher m is the length of the string being inserted.
        Worst case is we need to insert a new node for every character in string,
        hence O(m).
        '''
        temp = self.root
        for i in word:
            if not temp.contains(i):
                temp.append(i)
            temp = temp.get_child(i)
        temp.set_end()


    def search(self, word):
        '''
        
        '''
        temp = self.root
        for i in word:
            if not temp.contains(i):
                return False
            else:
                temp = temp.get_child(i)
        return temp.is_end()
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if not temp.contains(i):
                return False
            temp = temp.get_child(i)
        return True



if __name__ == "__main__":
    import argparse
    CLI=argparse.ArgumentParser()
    CLI.add_argument('-s', '--string',
                    action='store',
                    dest='string')
    args = CLI.parse_args()
    
    print(f'Array to sort: {args.string}')
    t= Trie()
    t.insert(args.string)
    print(t.search(args.string))
    print(t.search('random'))
    print(t.startsWith(args.string[0]))
