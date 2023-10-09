#!/usr/bin/python3
def no_c(my_string):
    cp = ""
    for j in range(len(my_string)):
        if my_string[j] != 'c' and my_string[j] != 'C':
            cp += my_string[j]
    return (cp)
