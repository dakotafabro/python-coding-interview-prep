def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

print_items(10)

# When there is a dominant Big O, drop the non-dominant Big O
# In this case the nested for loop runs at O(n^2) whereas the k for loop is running at O(n)
# We can drop the O(n) because in the percentage of the function, it is insignificant in the time it takes up