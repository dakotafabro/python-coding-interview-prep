## selection sort uses indexes

def selection_sort(my_list): ## sorts by swapping values at specific indexes
    for i in range(len(my_list)-1): ## i will move through the number of values
        min_index = i ## min_index will be the value being compared to the rest
        for j in range(i+1, len(my_list)): ## j will move from the index after i
            if my_list[j] < my_list[min_index]: ## if j is less than i,
                min_index = j ## set min_index to j
        if i != min_index: ## if i does not equal min_index --meaning there IS a reason to swap,
            temp = my_list[i] ## set temp to the value at i
            my_list[i] = my_list[min_index] ## set i to the min_index
            my_list[min_index] = temp ## move min_index to where temp was
    return my_list ## return the list

print(selection_sort([4,2,6,5,1,3]))