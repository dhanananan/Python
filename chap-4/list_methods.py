# list methods examples
# sort() method, reverse() method, append(value ) method, insert() method, remove() method, pop(index) method,remove(value)
# list is mutable in the python

# sort()  method sorts the list
numbers = [1, 2, 3, 4, 5]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]

# reverse() method reverses the list
number = [1, 2, 3, 4, 5]
number.reverse()
print(number) # [5, 4, 3, 2, 1]

# append() method adds a value to the end of the list
number = [1, 2, 3, 4, 5]   
number.append(6)
print(number) # [1, 2, 3, 4, 5, 6]


# insert() method inserts a value at a specified position in the list
number = [1, 2, 3, 4, 5]   
number.insert(2, 6)
print(number) # [1, 2, 6, 3, 4, 5]


# remove() method removes the first occurrence of the value in the list
number = [1, 2, 3, 4, 5]   
number.remove(3)
print(number) # [1, 2, 4, 5]  

  
# pop() method removes the item at the specified position in the list and returns the removed item
number = [1, 2, 3, 4, 5]   
number.pop(2)
print(number) # [1, 2, 4, 5] 


