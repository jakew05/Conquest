import classes
import variables

# weapons
fists = classes.weapon('fists', 2, 99999, 2, 'weapon')
bloodScythe = classes.weapon('blood-scythe', 5, 20, 5, 'weapon')
thornCloak = classes.weapon('thorn-cloak', 7, 14, 6, 'weapon')
stormChain = classes.weapon('storm-chain', 10, 11, 4, 'weapon')

# one use weapons
throwingDagger = classes.consumableWeapon('throwing-dagger', 10, 5, 'consumable-wpn')
woodenSpear = classes.consumableWeapon('wooden-spear', 12, 6, 'consumable-wpn')
fireStone = classes.consumableWeapon('firestone', 20, 8, 'consumable-wpn')
iceBomb = classes.consumableWeapon('icebomb', 30, 10, 'consumable-wpn')

# one use heals
apple = classes.comsumableHeal('apple', 5, 3, 'consumable-heal')
carrot = classes.comsumableHeal('carrot', 4, 2, 'consumable-heal')
bandages = classes.comsumableHeal('bandages', 15, 5, 'consumable-heal')
redPotion = classes.comsumableHeal('red-potion', 30, 8, 'consumable-heal')
healingStone = classes.comsumableHeal('healing-stone', 45, 10, 'consumable-heal')

# key items
map = classes.keyItem('map', 'keyItem')

# area item lists

# white hall
white_hall_main = [bloodScythe, thornCloak, stormChain]

# field of graves
field_of_graves_grave = [bandages, apple]
field_of_graves_crate = [throwingDagger, woodenSpear, carrot]
field_of_graves_monument = [map]
