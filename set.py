fruit_set = {"Apple", "Banana", "Orange", "Cherry", "Mango", "Pineapple", "Banana", "Apple"}


# add()   -  add the element in the set.

fruit_set.add("Papaya")
print(len(fruit_set))



# update()  -  it add the another set into the first set. it does not have to be add set it can add any itrable object.

second_fruit_set = ["Grapefruit", "Cranberry", "Coconut", "Gooseberries", "Apple"]
fruit_set.update(second_fruit_set)
print(fruit_set)




# remove()  - it remove the set item in the set if item exist in the set. or it can throw the key error.

fruit_set.remove("Apple")
print(fruit_set)



# discard()  - it also remove the set iems. if item exist in the set it can not raise the error.

fruit_set.discard("apple")
print(fruit_set)




# pop()   - this methods also remove the the item at the end. but as we know set are unordered so we can not sure what item has been deleted.

fruit_set.pop()
print(fruit_set)



# clear()   - this methods return the empty the set

fruit_set.clear()
print(fruit_set)



# del-   del keyword will delete the set completely and throw an error

del fruit_set
print(fruit_set)



# union()  -  this methods retrun a new set containing all items for both sets 

another_set = {"Apple", "Orange", "Papaya"}
union_set = fruit_set.union(another_set)
print(union_set)

 


# copy()  -  return a copy of the set
newFruit = fruit_set.copy()
print(newFruit)



# pop()   -  remove the last elements of the set

fruit_set.pop()
print(fruit_set)

















                   