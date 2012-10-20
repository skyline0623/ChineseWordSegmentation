import load, segmentation
load.dic_load('dict.txt'.decode('utf-8'))


sen = raw_input("Input:")
while sen != 'Q':
        res = segmentation.segmentation(sen.decode('gbk'))
        for w in res:
            print w.encode('gbk') 
        sen = raw_input("Input:")
    
