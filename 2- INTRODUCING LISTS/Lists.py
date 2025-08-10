# Lists allow you to store sets of information in one place.
# A list is a collection of items in a particular order.
# You can put anything into a list.

# index  ->      0       1        2
footballers = ['vini','belli','benzema']
print(footballers)
print(footballers[0])
print(footballers[1])
print(footballers[2])
print(footballers[-1]) #last element

print(footballers[0].title())
print(footballers[0].upper())

message = f"{footballers[-1].title()} has ballon d'or."
print(message)

print("-------------****************-------------")

# ex) 1
names = ["name 1","name 2","name 3"]
print(names[0])
print(names[1])
print(names[2])

# ex) 2
message_1=f"Hello {names[0].title()} !"
message_2=f"Hello {names[1].title()} !"
message_3=f"Hello {names[2].title()} !"
print(message_1)
print(message_2)
print(message_3)

# ex) 3
cars = ["bmw","mercedes","ferari","porsche"]
series = f"I love to ride {cars[0].upper()}, but if i want luxury car i will choose {cars[1].title()}, my dream cars is {cars[2].title()} and also {cars[3].title()}. "
print(series)

print("-------------****************-------------")

# Modifying
cars = ["bmw","mercedes","ferari","porsche"]
print(cars)
cars[1] = "Honda"
print(cars)

# Adding
cars = ["bmw","mercedes","ferari","porsche"]
cars.append("skoda")
print(cars)
players = []
players.append("vini")
players.append("belli")
players.append("zidane")
print(players)

cars = ["bmw","mercedes","ferari","porsche"]
cars.insert(1,"skoda")
print(cars)

# Removing
cars = ["bmw","mercedes","ferari","porsche"]
del cars[0]
print(cars)
# pop ---> comes from thinking of a list as a stack
cars = ["bmw","mercedes","ferari","porsche"]
poped_car=cars.pop()
print(cars)
print(poped_car)
cars = ["bmw","mercedes","ferari","porsche"]
last_one = cars.pop()
print(f"the last car i have bought is {last_one.title()}")

cars = ["bmw","mercedes","ferari","porsche"]
poped_car = cars.pop(1)
print(cars)
print(f"i have poped {poped_car.title()}")

cars = ["bmw","mercedes","ferari","porsche"]
cars.remove("bmw")
print(cars)

cars = ["bmw","mercedes","ferari","porsche"]
too_expensive = "ferari"
cars.remove(too_expensive)
print(cars)
print(f"{too_expensive.title()} is too expensive.")

print("-------------****************-------------")

# ex) 1
persons = ["person 1","person 2","person 3"]
print(f"Nice to meet you {persons[0].title()}")
print(f"Nice to meet you {persons[1].title()}")
print(f"Nice to meet you {persons[2].title()}")

# ex) 2
persons = ["person 1","person 2","person 3"]
print(persons)
dropped_person = persons.pop(1)
print(f"{dropped_person.title()} can't attend.")
persons.insert(1,"person 4")
print(persons)
print(f"{persons[1].title()} will attend instead of {dropped_person.title()}.")
print(f"Nice to meet you {persons[0].title()}")
print(f"Nice to meet you {persons[1].title()}")
print(f"Nice to meet you {persons[2].title()}")

# ex) 3
print(persons) 
print("I have found a bigger table.")
persons.insert(0,"person 5")
persons.insert(2,"person 6")
persons.append("person 7")
print(persons)
print(f"Nice to meet you {persons[0].title()}")
print(f"Nice to meet you {persons[1].title()}")
print(f"Nice to meet you {persons[2].title()}")
print(f"Nice to meet you {persons[3].title()}")
print(f"Nice to meet you {persons[4].title()}")
print(f"Nice to meet you {persons[5].title()}")

# ex) 4
print(persons)
print("Sorry but i can only invite two persons only!")
first = persons.pop()
print(f"Sorry {first.title()}")
second = persons.pop()
print(f"Sorry {second.title()}")
third = persons.pop()
print(f"Sorry {third.title()}")
fourth = persons.pop()
print(f"Sorry {fourth.title()}")
print("Now I can say ...")
print(f"Nice to meet you {persons[0].title()}")
print(f"Nice to meet you {persons[1].title()}")
del persons[0]
del persons[0]
print(persons)

print("-------------****************-------------")

# Sorting

# sort() --->  Permanently
cars = ["bmw","mercedes","ferari","porsche","audi"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted() --->  Temporarily
cars = ["bmw","mercedes","ferari","porsche","audi"]
print(f"orginal : {cars}")
print(f"sorted : {sorted(cars)}")
print(f"reverse sorted : {sorted(cars,reverse=True)}")
print(f"orginal again : {cars}")

# reverse()---> Permanently
cars = ["bmw","mercedes","ferari","porsche","audi"]
print(cars)
cars.reverse()
print(cars)

# len 
cars = ["bmw","mercedes","ferari","porsche","audi"]
print(f"lenght : {len(cars)}")

print("-------------****************-------------")

# ex) 1
locations = ["estonia","norway","denmark","uk","germany"]
print(f"original -> {locations}")
print(f"sorted -> {sorted(locations)}")
print(f"original -> {locations}")
print(f"reverse sorted -> {sorted(locations,reverse=True)}")
print(f"original -> {locations}")
locations.reverse()
print(f"reverse -> {locations}")
locations.reverse()
print(f"reverse again == original -> {locations}")
locations.sort()
print(f"sort -> {locations}")
locations.sort(reverse=True)
print(f"reverse sort -> {locations}")

# ex) 2
persons = ["person 1","person 2","person 3"]
print(f"number of guests is {len(persons)}")

# ex) 3
countries = []
countries.append("mexico")
countries.append("usa")
countries.append("indonesia")
countries.insert(1,"china")
countries.insert(3,"australia")
countries.insert(4,"brazil")
print(f"Countries => {countries}")
del countries[0]
print(f"Countries => {countries}")
countries.remove("brazil")
print(f"Countries => {countries}")
countries.pop(-1)
print(f"Countries => {countries}")
print(f"Sorted Countries => {sorted(countries)}")
print(f"Reverse Sorted Countries => {sorted(countries,reverse=True)}")
countries.reverse()
print(f"reverse Countries => {countries}")
countries.reverse()
print(f"reverse Countries again == original countries => {countries}")
countries.sort()
print(f"sort Countries => {countries}")
countries.sort(reverse=True)
print(f"reverse sort Countries => {countries}")
print(f"Number of Countries => {len(countries)}")

print("-------------****************-------------")

persons = ["person 1","person 2","person 3"]
#print(persons[3]) # error out of range 
print(persons[1])
print(persons[-1]) # last element
test = []
#print(test[-1]) # it gives error only when the list is empty
