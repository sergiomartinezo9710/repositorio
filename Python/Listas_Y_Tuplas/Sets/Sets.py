#Sets
my_set = {} 
print(type(my_set))

my_set ={"Python","JavaScript","C++"} 
print(type(my_set)) 


my_set.add("C++") 
print(my_set) 
my_set.add("C#")
print(my_set)


my_set2 = {"Python","JavaScript","C++"}
my_set.difference_update(my_set2)
print(my_set)