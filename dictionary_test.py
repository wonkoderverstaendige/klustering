my_dict = {2: "Hi", 3: "Stas"}

my_value = my_dict[2]
my_value = "Lukas rules"
my_value = my_dict[3]
my_value = "Lukas rules"

for my_key in my_dict.keys():
    my_value = my_dict[my_key]
    my_value = "Lukas rules"

for my_value in my_dict.values():
	my_value = "Lukas rules"

print(my_dict)

###########

my_dict = {2: "Hi", 3: "Stas"}

my_dict[2] = "Lukas rules"
my_dict[3] = "Lukas rules"

for my_key in my_dict:
	my_dict[my_key] = "Lukas rules"
    
for my_key in my_dict.keys():
	my_dict[my_key] = "Lukas rules"

print(my_dict)

###########

distance = {2: (1.25 , 0), 3: (0, 1.25)}

# Manipulate only the first value from the list
#distance[2] = (2.25, 1)


my_tuple = distance[2]
my_list = list(my_tuple)
for i in range(len(my_list)):
    my_list[i] += 1
my_tuple = tuple(my_list)    
# magically create new_tuple that is my_tuple + 1
distance[2] = my_tuple
print(distance)


# Manipulate all values of the list