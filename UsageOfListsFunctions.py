fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)   # ['apple', 'banana', 'mango']
fruits.insert(1,"Grapes")
print(fruits) #['apple', 'Grapes', 'banana', 'mango']
fruits.extend(["Cherry","Pineapple"])
print(fruits) #['apple', 'Grapes', 'banana', 'mango', 'Cherry', 'Pineapple']
fruits.remove("banana")
print(fruits) #['apple', 'Grapes', 'mango', 'Cherry', 'Pineapple']
fruits.pop(3)
print(fruits)  #['apple', 'Grapes', 'mango', 'Pineapple']
fruits.clear()
print(fruits)  #[] prints empty List



lists_num = [1, 2, 3, 4, 5, 2, 3]
print(lists_num.count(2)) # Counts how many times 2 appears in the list

lists_num.sort()
print(lists_num) # Sorts the list in ascending order

lists_num.reverse()
print(lists_num) # Reverses the order of the list

lists_num.copy()
print(lists_num) # Creates a shallow copy of the list
