import random

inventory = []
lowercaseInventory = []

swordDmg = 10

global playerHP 
playerHP = 100

global goblinHP
goblinHP= 30

inventory.append("Sword")
lowercaseInventory.append("sword")
print("gained sword")
print(inventory)

print("goblin encounter")

turn = 1
while goblinHP > 1 or playerHP > 1:
    if turn == 1 and goblinHP > 1:
        print(inventory)
        weapon = input("what weapon? ")
        if weapon in inventory or weapon in lowercaseInventory:
            print(weapon, "equipped")
            goblinHP = goblinHP - swordDmg
            print(goblinHP) 
            if goblinHP > 1:
                turn = 2
        else:
            print("weapon not found")

    if turn == 2 and playerHP > 1:
        print("goblin attack")
        playerHP = playerHP - 10
        print(playerHP)
        turn = 1
        
print("killed")