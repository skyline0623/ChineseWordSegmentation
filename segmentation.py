# -*- coding: utf-8 -*-
import load
import sys
# sentence must be encoded in UNICODE
def segmentation(sentence):
        candidate = []
        cur = 0  #the current parsing position
        pre = 0  #the last possible candidate word's last position
        st = 0   #the current temp word start point
        while cur <= len(sentence):
                temp = sentence[st:cur + 1]
                ret = load.dict.contains_word(temp)
                if ret == -1:
                        if pre != st:
                                candidate.append(sentence[st:pre])
                                cur = pre - 1
                                st = cur + 1
                                pre = st
                        else:
                                candidate.append(sentence[st:cur + 1])
                                st = cur + 1
                                pre = st
                elif ret == 1:
                        candidate.append(sentence[st:cur + 1])
                        st = cur + 1
                        pre = st
                elif ret == 2:
                        pre = cur + 1
                cur += 1
        if st < len(sentence):
                candidate.append(sentence[st:])
        return candidate


