## if you have two sorted lists, it is easy to combine them into a new sorted list
## Merge Sort splits two sorted lists up until you have lists of single values
## then the lists of single values are sorted and combined until you are left with 
## one list containing all the values

## merge is considered a "helper function" because it only does part of what you need it to do

## Big(O) space complexity is O(n) because is creates new lists
## Big(O) time complexity is O(log n) when splitting
## Big(O) time complexity is O(n) when putting it back together
## Merge Sort time complexity is O(n log n)

def merge(list1, list2):
    ## create an empty list
    combined = [] 
    i = 0
    j = 0
    ## while there are items in each list,
    while i < len(list1) and j < len(list2): 
    ## if value of i is less than value of j
        if list1[i] < list2[j]: 
            ## append i to combined
            combined.append(list1[i]) 
             ## move i over to the right by 1
            i += 1
        else:
            ## else, append j to combined
            combined.append(list2[j]) 
            ## move j over to the right by 1
            j += 1 

    ## once one of the lists is empty, code moves to the following lines:

    ## while i is less than the length of the list
    while i < len(list1): 
        ## append i to combined
        combined.append(list1[i]) 
        ## move i over to the right by 1
        i += 1 

    ## while j is less than the length of the list
    while j < len(list2): 
        ## append j to combined
        combined.append(list2[j]) 
        ## move j over to the right by 1
        j += 1 

    ## return the list
    return combined 

## now that merge has been created, merge sort can use it
## merge_sort uses recursion

def merge_sort(my_list):
    ## if the length of the list is 1
    if len(my_list) == 1:
        ## return the list
        return my_list 
    ## mid is the length of the list split in half, but turned into an integer so that we don't end up with a decimal
    mid = int(len(my_list) / 2) 

    ## left of the list is from index of 0 to the middle of the list
    left = my_list[:mid] 

    ## right of the list is from middle of list to end of list
    right = my_list[mid:] 

    ## the following line is the recursive part
    ## merge the merge sorted lists until they are all split into single values and then recombined
    return merge(merge_sort(left), merge_sort(right)) 


print(merge_sort([3,1,4,2]))
