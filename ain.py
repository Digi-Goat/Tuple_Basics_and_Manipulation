#SECTION 1
fruit_tuple = ("apple", "banana", "cherry", "date")
print(fruit_tuple[0])
print(fruit_tuple[3])
slice_tuple = fruit_tuple[1:2+1]
print(slice_tuple)

#SECTION 2
num_table = (3, 5, 3, 2, 8, 3, 7)
print(num_table.count(3))
print(num_table.index(8))

#SECTION 3
person_info = ("Alice", 28, "Engineer")
name, age, profession = person_info
print(name)
print(age)
print(profession)