listOfBrands = ["Apple", "Amazone", "Microsoft", "Microsoft", "Meta",
                "Tesla", "SpaceX", "Oracle", "Netflix", "Nike", "Starbucks", "Marvel", "1+"]

# append() - add a items to the end of the list

listOfBrands.append("Redmi")
print(listOfBrands)


# clear()  - remove the all elements of the list

listOfBrands.clear()
print(listOfBrands)


# copy()  - return the copy of the list

listOfBrands_copy =  listOfBrands.copy()
print(listOfBrands_copy)


# count()   - return the number of the elements with the specified values

listOfBrands_count = listOfBrands.count("Microsoft")
print(listOfBrands_count)


# extendts()  -  add the elements of another list in one firstlist

anotherBrandsOfList = ["Puma", "Nike", "BATA", "Ralph Lauren"]
listOfBrands.extend(anotherBrandsOfList)
print(listOfBrands)


# index()  -  it return the index number of the specified value

indexOfTheItems = listOfBrands.index("Microsoft")
print(indexOfTheItems)


# insert()  - add the item in the list at specified index.

listOfBrands.insert(0, "Peter England")
print(listOfBrands)


# pop()  -  it remove the last item of the list it also remove the specified index item if we pass the index

listOfBrands.pop()
listOfBrands.pop(0)
print(listOfBrands)



# remove()  -  it remove the first itme with the specified value

listOfBrands.remove("Netflix")
print(listOfBrands) 


# reverse()  - it reverse the order of the list

listOfBrands.reverse()
print(listOfBrands)


# sort()  -  it sorted the list by ascending order

listOfBrands.sort()
print(listOfBrands)

listOfNumber = [4,7,-13,15,1552354323524,1243,42,2,82,992,72,62,7,8]
listOfNumber.sort()
print(listOfNumber)


