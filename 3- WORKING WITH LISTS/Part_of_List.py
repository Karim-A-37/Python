
players = ["vini","belli","rodri","arda","valverdi","camavinga"]
print(players[0:3])
print(players[1:4])
print(players[:4])#starts from the first item
print(players[4:])#ends to last item
print(players[-3:])#print last three items and changes while the length of list is changing
print(players[:-3])
print(players[0:5:2])# the 3rd value indicates the steps
for player in players[:4]:
	print(player.title())
# this doesn't work separately
#cp_players = players  
#print(cp_players)
#players.append("gonzalo")
#cp_players.append("fran")
#print(players)
#print(cp_players)

# this works separately
copied_players = players[:]
print(copied_players)
players.append("gonzalo")
copied_players.append("fran")
print(players)
print(copied_players)

print("		-----#***#-----		")

# ex) 1
players = ["vini","belli","rodri","arda","valverdi","camavinga","rudi"]
print(f"the first three items in the list : {players[:3]}")
print(f"three items from the middle of the list : {players[2:5]}")
print(f"the last three items in the list : {players[-3:]}")

# ex) 2
pizzas = ["Margherita","Marinara","Carbonara"]
friend_pizzas = pizzas[:]
pizzas.append("beef")
friend_pizzas.append("mix cheese")
print(f"original : {pizzas}")
print(f"copy : {friend_pizzas}")

# ex) 3
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("chocolate")
friend_foods.append("ice cream")
for food in my_foods:
	print(f"My food : {food}")
for food in friend_foods:
	print(f"Friend food : {food}")
















