first_tuple = ("R.D.J", 55, "Iron Man", "Jarvis", "R.D.J")


# NOTE :- we can not change the tuple when it once is created. tuples are unchangeble or immutable.
# but there is a taqniue or workarounds. we can convert the tuple into a list, change the list, and
# convert into a tuple

converted_into_list = list(first_tuple)
converted_into_list[0] = "Tony Stark"
converted_into_tuple = tuple(converted_into_list)
print(converted_into_tuple)



# count()  -  it returns the number of the specified values in the tuple


number_of_name = first_tuple.count("R.D.J")
print(number_of_name)


# index()  -  it return the index number of the metching specified values in the tuple

indexOfIronMan = first_tuple.index("Iron Man")
print(indexOfIronMan)
