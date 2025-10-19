import classes
import variables

# weapons
bloodScythe = classes.weapon('blood-scythe', 5, 20, 5, 'weapon')
thornCloak = classes.weapon('thorn-cloak', 7, 14, 6, 'weapon')
stormChain = classes.weapon('storm-chain', 10, 11, 4, 'weapon')

# one use weapons
throwingDagger = classes.consumableWeapon('throwing-dagger', 10, 5, 'consumable')
woodenSpear = classes.consumableWeapon('wooden-spear', 12, 6, 'consumable')
fireStone = classes.consumableWeapon('firestone', 20, 8, 'consumable')
iceBomb = classes.consumableWeapon('icebomb', 30, 10, 'consumable')

# one use heals
apple = classes.comsumableHeal('apple', 5, 3, 'consumable')
carrot = classes.comsumableHeal('carrot', 4, 2, 'consumable')
bandages = classes.comsumableHeal('bandages', 15, 5, 'consumable')
redPotion = classes.comsumableHeal('red-potion', 30, 8, 'consumable')
healingStone = classes.comsumableHeal('healing-stone', 45, 10, 'consumable')

# key items
map = classes.keyItem('map', 'keyItem')

# area item lists

# white hall
white_hall_main = [bloodScythe, thornCloak, stormChain]

# field of graves
field_of_graves_grave = [bandages, apple]
field_of_graves_crate = [throwingDagger, woodenSpear, carrot]
field_of_graves_monument = [map]
