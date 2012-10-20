#if you want to add a Chinese word,please insure it is encoded in Unicode.
class trie_tree:
        def __init__(self):
                self._tree = [False, {}]
                self._num = 0
        
        def add_word(self, word):
                cur = self._tree
                for c in word:
                        if c in cur[1]:
                                cur = cur[1][c]
                        else:
                                cur[1][c] = [False, {}]
                                cur = cur[1][c]
                if cur[0]:
                        return True
                else:
                        cur[0] = True
                        self._num += 1
                        return False
        #when word is contained and there is childs,return 2.when word is contained,return 1 when word is not contained but there is childs for the current node,return 0.Ohterwise,return -1
        def contains_word(self, word):
                cur = self._tree
                for c in word:
                        if c in cur[1]:
                                cur = cur[1][c]
                        else:
                                return -1
                if cur[0] and len(cur[1]) > 0:
                        return 2
                elif cur[0]:
                        return 1
                return 0

        def size(self):
               return self._num
