fruits = ["apples", "banana", "cherry"]
x,y,z = fruits; # multiple assignment to list items 
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # it adds space

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # it does not add space


ist2 = [1, 4, 5, 2, 1, 7]
ist2.sort()         # Sorting ist2
print(ist2)         # Output: [1, 1, 2, 4, 5, 7]
ist2.remove(1)      # Removes first occurence
print(ist2)         # Output: [1, 1, 2, 5, 7]
