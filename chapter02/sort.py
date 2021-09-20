import random
from typing import TYPE_CHECKING

def bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(0,i):
            if list[j] > list[i]:
                tmp = list[j]
                list[j] = list[i]
                list[i] =  tmp
       
    print(list)
###
#def simple_choice_sort(list):
#    for i in range(0,len(list)):
#        list[i]
        #for j in range(0,i):
          
def heap_sort(list,):
    i = 0
    n = len(list)

    while(i < n):

        unheap(list,i)
        i += 1

    while(i > 1):

        i -= 1
        tmp = list[0]
        list[0] = list[i]
        list[i] = tmp
        
        downheap(list, i-1)

def unheap(list, n):
    while n != 0:
        parent = int ((n - 1) / 2)
        if list[n] > list[parent]:
            # if larger than parent, trade that and parent
            tmp = list[n]
            list[n] = list[parent]
            list[parent] = tmp
            n = parent
        else:
            break

def downheap(array,n):
    if n == 0 : return
    parent = 0

    while True:
        child = 2 * parent + 1 # array[n]の子要素
        if child > n: break
        if (child < n) and array[child] < array[child + 1]:
            child += 1
        if array[parent] < array[child]: # 子要素より小さい場合スワップ
            tmp = array[child]
            array[child] = array[parent]
            array[parent] = tmp
            parent = child; # 交換後のインデックスを保持
        else:
            break

# デバッグ
if __name__ == "__main__":
    array = [1,2,3,4,5,3,2,1,4,3,4,5,0]
    print("before", array)
    heap_sort(array)
    print("after ", array)
    

list = [1,3,5,7,2,4,6,8]
randList = random.sample(range(100),10)
#bubble_sort(list)
#heap_sort(list,len(list) - 1,1)
print(randList)
bubble_sort(randList)


