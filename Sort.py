import re
import time
import sys

def bubble_sort__string(list_to_sort):
    list_len = len(list_to_sort)
    #change list to len (to number)

    for a in range(list_len): # to this many times (list_len)
        for b in range(list_len-a-1): #subtract a and do this this many times every time less and less (-a)
            #-1 cuz balcaning equasion in list_to_sort[+1]
            if  list_to_sort[b] > list_to_sort[b+1]:#there we pic position on list and nex postion and coparing ascii
                list_to_sort[b], list_to_sort[b+1] =  list_to_sort[b+1], list_to_sort[b] #if yes chaning places

    return list_to_sort #return sorted list


def animated_text_words(text):
    anim_text = text.split() # default it make sapces every word
    for word in anim_text:
        sys.stdout.write(word + " ") # stdout adding char on comand promt and not adding new line
        sys.stdout.flush() #king this instant - clar buffor
        time.sleep(0.3)
    print()
    print()

print()
time.sleep(0.2)
animated_text_words("this program will sort all letters that u type")
time.sleep(2.5)
list_to_sort = input("Type something to sort: ")
list_to_sort1 = []

for x in list_to_sort:
    if re.match("^[a-zA-Z0-9]$", x):
        list_to_sort1.append(x)
Reday_sorted_letters = bubble_sort__string(list_to_sort1)
print(Reday_sorted_letters)