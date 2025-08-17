# immutable ---> values that can't change
# Tuple is immutable list that uses  parentheses
dim = (100,30)
print(dim[0])
print(dim[1])

#dim[0] = 200

#If you want to define a tuple with one element, you need to include a trailing comma.
tup = (3,)
print(tup[0])

dims =  (100,50)
for dim in dims:
	print(dim)

#you can assign a new value to a variable that represents a tuple.
dims =  (100,50)
print(f"original dims : ")
for dim in dims :
	print(dim)
dims = (200,60)
print(f"modified dims : ")
for dim in dims :
	print(dim)

print("		-----#****#-----	")
foods = ('falafel','pizza','fish','chicken','beef')
for food in foods : 
	print(food)
#foods[0] = 'chips'
print("The Menu is modified")
new_menu = ('salamon','pizza','fish','chicken','fruits')
print(new_menu)
for food in new_menu :
	print(food)










