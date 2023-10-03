class Mob:
    def __init__(self, hp, base_damage):
        self.hp = hp
        self.base_damage = base_damage

class Zombie(Mob):
    def __init__(self,hp,base_damage,armor):
        super().__init__(hp,base_damage)
        self.armor = armor

class Skeleton(Mob):
    def __init__(self,hp,base_damage,ammo):
        super().__init__(hp,base_damage)
        self.ammo = ammo


John = Zombie(20,4,4)
print(John)
