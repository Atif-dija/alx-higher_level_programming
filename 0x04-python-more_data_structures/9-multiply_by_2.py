#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    list_k = list(dic.keys())
    for i in list_k:
        dic[i] *= 2
    return dic
