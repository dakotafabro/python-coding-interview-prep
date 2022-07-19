## selection sort uses indexes
## sorts by swapping values at specific indexes
## i will move through the number of values
## min_index will be the value being compared to the rest
## j will move from the index after i

## if j is less than i,
## set min_index to j
## if i does not equal min_index --meaning there IS a reason to swap,
## set temp to the value at i
## set i to the min_index
## move min_index to where temp was
## return the list


def selection_sort(my_list):
    for i in range(len(my_list)-1): 
        min_index = i 
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]: 
                min_index = j 
        if i != min_index: 
            temp = my_list[i] 
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp 
    return my_list 

print(selection_sort([4,2,6,5,1,3]))