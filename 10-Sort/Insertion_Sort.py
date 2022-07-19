## insertion sorts compare the values prior
## Big O: O(n^2) in worst case
## Almost sorted data is best case - time complexity of O(n)
## Space complexity of O(1) means it sorts the list in place and does not make a copy of the list

def insertion_sort(my_list):
    ## start at the index of 1
    for i in range(1, len(my_list)): 
        ## temp equals the value at index of i
        temp = my_list[i] 
        ## j equals the value prior to i
        j = i-1 
        ## while temp is less than the value at index of j AND j is greater than -1
        while temp < my_list[j] and j > -1: 
            ## move j one index over to the right
            my_list[j+1] = my_list[j] 
            ## set j to temp
            my_list[j] = temp 
            ## move j one spot over to the left
            j -= 1 
    ## return the list
    return my_list 

print(insertion_sort([4,2,6,5,1,3]))
