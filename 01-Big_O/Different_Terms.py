def print_items(a, b):
    for i in range(a):
        print(a)

    for i in range(b):
        print(b)

# The above function might look like O(n) because at first glance, 
# there are two for loops. We might be inclined to say "the first
# for loop is O(n) and the second loop is O(n) so I'll just add them
# together to get O(2n), drop the constant, and it becomes O(n)".
# This is incorrect. a and b are two different variables/values. In order
# to simplify this, it would become O(a + b). 

def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)

# The above example would simplify to O(a * b) and NOT O(n^2) for the same 
# reason as the previous example. a and b are two separate values.