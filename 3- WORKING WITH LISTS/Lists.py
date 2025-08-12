
# for loop ---> automates repetitive tasks.

magicians = ["magician 1","magician 2","magician 3","magician 4"] 
for magician in magicians:
	print(magician.title(),", you have perforemd great trick.")
	print(f"{magician.title()}, we are looking forward for your next trick.\n")
print("Thank You!")

#Indentation Errors

# ex) 1 --->  expected an indented block after 'for' statement
magicians = ["magician 1","magician 2","magician 3","magician 4"] 
#for magician in magicians:
#print(magician)

# ex) 2 ---> logical error
magicians = ["magician 1","magician 2","magician 3","magician 4"]
#for magician in magicians:
#	print(magician.title(),", you have perforemd great trick.")
#print(f"{magician.title()}, we are looking forward for your next trick.\n")

# ex) 3 ---> unexpected indent
message = "Hello"
#	print(message)

# ex) 4 ---> logical error
magicians = ["magician 1","magician 2","magician 3","magician 4"] 
#for magician in magicians:
#	print(magician.title(),", you have perforemd great trick.")
#	print(f"{magician.title()}, we are looking forward for your next trick.\n")
#	print("Thank You!")

# colon ---> tells Python to interpret the next line as the start of a loop.
magicians = ["magician 1","magician 2","magician 3","magician 4"] 
#for magician in magicians
#	print(magician.title(),", you have perforemd great trick.")

print("		----------##########----------		")

# ex) 1
pizzas = ["Margherita","Marinara","Carbonara "]
for pizza in pizzas:
	print(f"Type of pizza is {pizza}")
	print(f"I like {pizza} pizza")
print(f"pizza is one of most delicious food especially {pizzas[0]}, {pizzas[1]} and {pizzas[2]}. ")

# ex) 2
animals = ["lion","tiger","jaguar"]
for animal in animals:
	print(animal)
	print(f"The {animal.title()} is a wild animal.\n")
print("All the three animals are wild animals that can't be a pet.")


