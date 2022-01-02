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
    combined = [] ## create an empty list
    i = 0
    j = 0
    while i < len(list1) and j < len(list2): ## while there are items in each list,
        if list1[i] < list2[j]: ## if value of i is less than value of j
            combined.append(list1[i]) ## append i to combined
            i += 1 ## move i over to the right by 1
        else:
            combined.append(list2[j]) ## else, append j to combined
            j += 1 ## move j over to the right by 1

    ## once one of the lists is empty, code moves to the following lines:

    while i < len(list1): ## while i is less than the length of the list
        combined.append(list1[i]) ## append i to combined
        i += 1 ## move i over to the right by 1

    while j < len(list2): ## while j is less than the length of the list
        combined.append(list2[j]) ## append j to combined
        j += 1 ## move j over to the right by 1

    return combined ## return the list

## now that merge has been created, merge sort can use it
## merge_sort uses recursion

def merge_sort(my_list):
    if len(my_list) == 1: ## if the length of the list is 1
        return my_list ## return the list
    mid = int(len(my_list) / 2) ## mid is the length of the list split in half, but turned into an integer so that we don't end up with a decimal
    left = my_list[:mid] ## left of the list is from index of 0 to the middle of the list
    right = my_list[mid:] ## right of the list is from middle of list to end of list

    ## the following lines is the recursive part
    return merge(merge_sort(left), merge_sort(right)) ## merge the merge sorted lists until they are all split into single values and then recombined


print(merge_sort([3,1,4,2]))
