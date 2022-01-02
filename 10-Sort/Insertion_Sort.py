## insertion sorts compare the values prior
## Big O: O(n^2) in worst case
## Almost sorted data is best case - time complexity of O(n)
## Space complexity of O(1) means it sorts the list in place and does not make a copy of the list

def insertion_sort(my_list):
    for i in range(1, len(my_list)): ## start at the index of 1
        temp = my_list[i] ## temp equals the value at index of i
        j = i-1 ## j equals the value prior to i
        while temp < my_list[j] and j > -1: ## while temp is less than the value at index of j AND j is greater than -1
            my_list[j+1] = my_list[j] ## move j one index over to the right
            my_list[j] = temp ## set j to temp
            j -= 1 ## move j one spot over to the left
    return my_list ## return the list

print(insertion_sort([4,2,6,5,1,3]))
