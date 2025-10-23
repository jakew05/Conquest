import items

# game control variables
begin = None
action = None

# position trackers
room = 'white_hall'
subroom = 'main'

# game state trackers
combat = False
gameOver = False
currentEnemy = None

# combat objects
enemyActionList = []
enemyActionCounter = 0
currentWeapon = items.fists

# preference trackers
keepHelpOn = True
keepInvOn = True

# player progress variables
mapObtained = False
compassObtained = False
maxHealth = 50
maxGold = 999

# player objects
weapons = []
consumables = []
keyItems = []

inventory = {
    'weapons' : weapons,
    'consumables' : consumables,
    'key items' : keyItems
}

stats = {
    'weapon' : currentWeapon.name,
    'weapon damage' : currentWeapon.damage,
    'weapon durability' : currentWeapon.durability,
    'defense' : 0,
    'health' : 50,
    'max health' : maxHealth,
    'gold' : 0,
    'max gold' : maxGold
}