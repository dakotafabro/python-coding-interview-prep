def bubble_sort(my_list): ## sorts the list by "bubbling up" the largest values until everything is sorted
    for i in range(len(my_list) - 1, 0 ,-1): ## for the 6 items in the array, the range is 5, going to zero, decrementing by -1
        for j in range(i): ## this for loop iterates through the array
            if my_list[j] > my_list[j+1]: ## if the number on the left is greater than the next number
                temp = my_list[j] ## set temp to the greater number
                my_list[j] = my_list[j+1] ## set the lesser/next number to the previous spot
                my_list[j+1] = temp ## set temp to the next spot
    return my_list ## return the list

print(bubble_sort([4,2,6,5,1,3]))