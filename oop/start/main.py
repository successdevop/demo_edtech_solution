from player import Player
from enemy import Enemy, Troll

tim = Player("Tim")
print(tim)

enemy_1 = Enemy("Basic enemy", 12, 1)
enemy_1.take_damage(6)
print(enemy_1)

enemy_1.take_damage(3)
print(enemy_1)

enemy_1.take_damage(4)
print(enemy_1)

ugly_trol = Troll("Pub")
# print("Ugly troll - {}".format(ugly_trol))

another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
# print(brother)

ugly_trol.grunt()
another_troll.grunt()
brother.grunt()