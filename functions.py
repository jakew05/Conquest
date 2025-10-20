import os
import random
import variables
import worldtext
import drawEnemies
import worldContents
import worldConnections
import worldEnemies
import classes

def clearTerminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

# shows text for the current area
def displayWorldText():
    print("----World-----------------------------------------")
    print(worldtext.world[variables.room][variables.subroom])
    print("--------------------------------------------------")

# displays list of actions the player can take (when player types 'help')
def displayActionList():
    print("----Basic Actions--------------")
    print("'inv' view inventory\n'stat' view your stats\n'grab [item]' add item to your inventory\n"
        "'inspect [object]' take closer look at object\n'return' return to where you were\n" \
        "'go [region]' go to new region on map (ex: go dead_forest)")
    if variables.mapObtained == True:
        print("'map' view map (once acquired)\n'help' display action list")
    print("-------------------------------")
    
def displayCombatActions():
    print("----Combat Actions-------------")
    print("'strike' strike an enemy while in combat" \
    "\n'item' use an item from your inventory")
    print("-------------------------------")

def displayStats():
    print("----Stats----------------------")
    for stat in variables.stats:
        print(stat + " | " + str(variables.stats[stat]))
    print("-------------------------------")

def displayInventory():
    print("----Inventory------------------")
    for list in variables.inventory:
        print(f"{list}:")
        for item in variables.inventory[list]:
            print(f" ~ {item.name}")
    print("-------------------------------")

def displayLoot(loot):
    print("----Loot-----------------------")
    for item in loot:
        print(item.name)
    print("-------------------------------")

def grabItem(itemToGrab):
    availableItems = worldContents.world[variables.room][variables.subroom]
    itemToRemove = None
    for item in availableItems:
        if item.name == itemToGrab:
            if item.type == 'weapon':
                variables.weapons.append(item)
            elif item.type == 'consumable':
                variables.consumables.append(item)
            elif item.type == 'keyItem':
                variables.keyItems.append(item)
            itemToRemove = item
            break
    availableItems.remove(itemToRemove)

def inspectObject(subroom):
    variables.subroom = subroom

def checkValidObject(room, objectChoice):
    for object in worldtext.world[room]:
        if object == objectChoice:
            return True
    return False

def checkValidItem(itemChoice):
    itemList = worldContents.world[variables.room][variables.subroom]
    for item in itemList:
        if item.name == itemChoice:
            return True
    return False

def checkValidEnemy(enemyChoice):
    for enemy in worldEnemies.world[variables.room][variables.subroom]:
        if enemy.type == enemyChoice:
            return True
    return False

def checkInventoryForKeyItem(itemToCheckName):
    for item in variables.inventory['key items']:
        if item.name == itemToCheckName:
            return True

def invalidInput():
    print("That is not a valid input, please try again. \nType 'help' for a list of permitted actions.")

def returnToMain(room):
    variables.subroom = 'main'

def changeRegion(regionToMoveTo):
    for region in worldConnections.worldGraph[variables.room]:
        if region == regionToMoveTo:
            variables.room = regionToMoveTo
            variables.subroom = 'main'
            return True
    invalidInput()

def displayMap():
    print("----Map---------------------------------------------------")
    print("            dead       helmet                        ")
    print("sorroweive  forest     high                          ")
    print(" [------]   [------]   [--/\--]      ----(*)----     ")
    print(" [ O o o]---[| || |]---[ /  \ ]  The Corrupted Lands ")
    print(" [------]   [------]   [------]      ----(*)----     ")
    print("    |          |                                     ")
    print(" tall       field of               great    corrupted")
    print(" rocks      graves     helmwind    gate      spire   ")
    print(" [------]   [------]   [------]   [------]   [--[]--]")
    print(" [/\/\/\]---[ n n n]---[[][][]]---[ (__) ]---[  ||  ]")
    print(" [------]   [------]   [------]   [------]   [-|^^|-]")
    print("               |          |                          ")
    print(" abandoned  burned     distant            .          ")
    print(" tower      ruins      windlands         /|\         ")
    print(" [--/\--]   [------]   [------]         ( N )        ")
    print(" [  ||  ]---[ _ /-\]   [~_~~_~]      < W  +  E >     ")
    print(" [------]   [------]   [------]           S          ")
    print("                                          V          ")
    print("----------------------------------------------------------")

def displayLocation():
    pass

def getCurrentEnemy(enemyChoice):
    for enemy in worldEnemies.world[variables.room][variables.subroom]:
        if enemy.type == enemyChoice:
            return enemy
        else:
            dummy = classes.enemy(1, 1, 'dummy')
            return dummy

def generateActionList():
    for i in range(0,100):
        val = random.randint(0,1)
        if val == 0:
            variables.enemyActionList.append('attack')
        if val == 1: 
            variables.enemyActionList.append('heal')

def enemyFight(enemy):
    print("----Combat----------------------------")
    if enemy.type == 'skeleton':
        drawEnemies.drawSkeleton()
    print(f"ENEMY HEALTH: {enemy.health} -- ENEMY ATTACK: {enemy.attack}")
    print(f"YOUR HEALTH: {variables.stats['health']} -- MAX HEALTH: {variables.maxHealth}")
    if enemy.health <= 0:
        goldReward = random.randint(20,50)
        variables.stats['gold'] += goldReward
        variables.combat == False
        print(f"enemy defeated, you earned {goldReward} gold.")
    print("--------------------------------------")