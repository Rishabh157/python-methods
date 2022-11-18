actorDict = {"name": "Chris", "lastName": "Evans", "age": 45,
             "played_char": "Ceptain America", "Studio": "Marvel"}


# clear()  - it removes all the key in the dict.

actorDict.clear()
print(actorDict)


# copy()  -  it return the copy of the dict.

actorDict_copy = actorDict.copy()
print(actorDict_copy)


# fromkeys()  -  it return the dict with the specified keys and value.

nameOfActor = dict.fromkeys(("name", "age"), "Rishabh")
print(nameOfActor)



# get()    -   it return the value of the specified key. if it return None that means the key is not exist in the dict

get_age = actorDict.get("age")
print(get_age)



# items()  -  it return a list contaning a tuple with key value pair

keys_and_values = actorDict.items()
print(keys_and_values)




# keys()   -   it return a list contaning all the keys in the dict.

all_keys = actorDict.keys()
print(all_keys)



# pop()   -  it remove the given key in the pop()

actorDict.pop("name")
print(actorDict)




# popitem()  -  it removes the last key value pair item in the dict

actorDict.popitem()
print(actorDict)



# update()  -  it update the dict with specified key value pair

actorDict.update({"next_movie":"The Gray Man"})
print(actorDict)



# values()  -  return the list of all the values in the dict

all_values_of_dict = actorDict.values()
print(all_values_of_dict)









