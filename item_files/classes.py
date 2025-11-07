class weapon():
    def __init__(self, name, damage, durability, healAmount, type):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.healAmount = healAmount
        self.type = type

    def strike(self, enemy):
        enemy.health -= self.damage
        self.durability -= 1

    def heal(self, playerHealth):
        playerHealth += self.healAmount

class enemy():
    def __init__(self, health, healAmount, attack, type):
        self.health = health
        self.healAmount = healAmount
        self.attack = attack
        self.type = type

    def heal(self):
        self.health += self.healAmount

class consumableWeapon():
    def __init__(self, name, damage, size, type):
        self.name = name
        self.damage = damage
        self.size = size
        self.type = type

    def use(self, enemy):
        enemy.health -= self.damage

class comsumableHeal():
    def __init__(self, name, healAmount, size, type):
        self.name = name
        self.healAmount = healAmount
        self.size = size
        self.type = type

    def use(self, playerHealth, maxPlayerHealth):
        if playerHealth < maxPlayerHealth:
            if playerHealth + self.healAmount <= maxPlayerHealth:
                playerHealth += self.healAmount
            else:
                playerHealth = maxPlayerHealth

class keyItem():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        