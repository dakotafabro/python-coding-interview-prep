## sorts the list by "bubbling up" the largest values until everything is sorted
def bubble_sort(my_list): 
    ## for the 6 items in the array, the range is 5, going to zero, decrementing by -1
    for i in range(len(my_list) - 1, 0 ,-1): 
        ## this for loop iterates through the array
        for j in range(i): 
            ## if the number on the left is greater than the next number
            if my_list[j] > my_list[j+1]: 
                ## set temp to the greater number
                temp = my_list[j] 
                ## set the lesser/next number to the previous spot
                my_list[j] = my_list[j+1] 
                ## set temp to the next spot
                my_list[j+1] = temp 
    ## return the list
    return my_list 

print(bubble_sort([4,2,6,5,1,3]))