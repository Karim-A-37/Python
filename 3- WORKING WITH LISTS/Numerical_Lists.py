
#  off-by-one error ---> is a logic error that involves a number that differs from its intended value by 1.
for value in range(1,5):
	print(value)
for value in range(1,6):
	print(value)
for value in range(6):
	print(value)

nums = list(range(1,6))
print(nums)
odd_nums = list(range(1,10,2))
print(odd_nums)

squares = []
for value in range(1,11):
	sqr = value ** 2
	squares.append(sqr)
print(squares)

squares = []
for value in range(1,11):
	squares.append(value ** 2)
print(squares)

numbers = list(range(1,10))
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# List Comprehensions
#name   = [expression on numbers        loop to generate numbers]
squares = [i**2 for i in range(1,11)]
print(squares)

print("		----------##########----------		")

# ex) 1
for i in range(1,21):
	print(i)

# ex) 2
numbers  = list(range(1,1000001))
#for number in numbers : 
#	print(numbers)

# ex) 3
numbers  = list(range(1,1000001))
#print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# ex) 4
odd_numbers = list(range(1,20,2))
for number in odd_numbers : 
	print(number)
print(odd_numbers)

# ex) 5
threes=[i*3 for i in range(3,31)]
print(threes)

threes = []
for i in range(3,31):
	threes.append(i*3)
print(threes)

# ex) 6
cubes = []
for i in range(1,11):
	cubes.append(i ** 3)
print(cubes)

# ex) 7
cubes = [i**3 for i in range(1,11)]
print(cubes)

print("		----------##########----------		")


