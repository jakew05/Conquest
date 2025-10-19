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
    'attack' : 10,
    'defense' : 0,
    'health' : 50,
    'gold' : 0
}