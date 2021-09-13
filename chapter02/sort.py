
def bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(0,i):
            if list[j] > list[i]:
                tmp = list[j]
                list[j] = list[i]
                list[i] =  tmp
       
    print(list)


list = [1,3,5,7,2,4,6,8]
bubble_sort(list)


