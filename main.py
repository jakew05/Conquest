import sys
import functions
import variables
import worldContents

# beginning
print("Welcome to CONQUEST")
functions.displayActionList()

# prompt for player to begin their adventure
while variables.begin != 'y' and variables.begin != 'n':
    variables.begin = input("would you like to begin your adventure? (y/n)")
    if variables.begin == 'n':
        sys.exit("quitting CONQUEST")
    elif variables.begin == 'y':
        print("starting your adventure...")

functions.clearTerminal()

while variables.gameOver == False:
    # remind player to ask for help
    print("type 'help' for a list of actions")

    # perform actions

    # basic actions
    if variables.action != None and variables.combat == False:
        if variables.action == 'help':
            functions.displayActionList()

        elif variables.action == 'inspect':
            functions.invalidInput()
        elif variables.action.split()[0] == 'inspect':
            objectChoice = variables.action.split()[1]
            if functions.checkValidObject(variables.room, objectChoice):
                functions.inspectObject(objectChoice)

        elif variables.action == 'return':
            functions.returnToMain(variables.room)

        elif variables.action == 'grab':
            functions.invalidInput()
        elif variables.action.split()[0] == 'grab':
            itemChoice = variables.action.split()[1]
            if functions.checkValidItem(itemChoice):
                functions.grabItem(itemChoice)
            else:
                functions.invalidInput()

        elif variables.action.replace(" ", "") == 'equip':
            functions.invalidInput()
        elif variables.action.split()[0] == 'equip':
            weaponChoice = variables.action.split()[1]
            if functions.checkValidWeapon(weaponChoice):
                variables.currentWeapon = functions.getValidWeapon(weaponChoice)
                functions.updateWeaponStats()
                print(f"*** equipped {variables.currentWeapon.name} ***")
            else:
                functions.invalidInput()

        elif variables.action == 'fight':
            functions.invalidInput()
        elif variables.action.split()[0] == 'fight':
            enemyChoice = variables.action.split()[1]
            if functions.checkValidEnemy(enemyChoice):
                variables.combat = True
                variables.action = 'help'
                variables.currentEnemy = functions.getCurrentEnemy(enemyChoice)
            else:
                functions.invalidInput()

        elif variables.action == 'inv':
            functions.displayInventory()

        elif variables.action == 'stat':
            functions.displayStats()

        elif variables.action == 'go':
            functions.invalidInput()
        elif variables.action.split()[0] == 'go':
            functions.changeRegion(variables.action.split()[1])

        elif variables.action == 'map' and variables.mapObtained == True:
            functions.displayMap()
            if variables.compassObtained == True:
                functions.displayLocation()

        else:
            functions.invalidInput()

    # combat actions
    if variables.action != None and variables.combat == True:
        while variables.combat == True:
            functions.clearTerminal()

            if variables.action == 'help':
                functions.displayCombatActions()
            elif variables.action == 'strike':
                variables.currentEnemy.health -= variables.currentWeapon.damage
            elif variables.action == 'item':
                functions.useConsumable()
            else:
                variables.action = 'help'
                continue

            functions.enemyFight(variables.currentEnemy)
            if variables.currentEnemy:
                variables.action = input("an enemy attacks: what will you do?: ")

    # check if player obtained key item
    if variables.mapObtained == False and functions.checkInventoryForKeyItem('map'):
        variables.mapObtained = True
        print("Map obtained. Type 'map' to view.\n")

    # check if player has selected a weapon in white hall and move them to field of graves
    if variables.room == 'white_hall' and variables.inventory['weapons']:
        variables.currentWeapon = variables.inventory['weapons'][0]
        functions.updateWeaponStats()
        variables.room = 'field_of_graves'

    # display world text
    functions.displayWorldText()

    # display loot if available
    if worldContents.world[variables.room][variables.subroom]:
        subroomLoot = worldContents.world[variables.room][variables.subroom]
        functions.displayLoot(subroomLoot)

    # prompt for action
    variables.action = input("what will you do?: ")
    
    # clear terminal
    functions.clearTerminal()