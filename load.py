import trie_tree

dict = trie_tree.trie_tree()

def dic_load(dir):
        file = open(dir)
        str = file.readline().decode('utf-8')
        while str != "":
                strs = str.split(",")
                dict.add_word(strs[0])
                str = file.readline().decode('utf-8')
        file.close()
       

