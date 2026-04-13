from player import Player
from enemy import Enemy

tim = Player("Tim")
print(tim)

enemy_1 = Enemy("Basic enemy", 12, 1)
enemy_1.take_damage(6)
print(enemy_1)

enemy_1.take_damage(3)
print(enemy_1)

enemy_1.take_damage(4)
print(enemy_1)