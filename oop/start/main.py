from player import Player
from enemy import Enemy, Troll, Vampire

tim = Player("Tim")

enemy_1 = Enemy("Basic enemy", 12, 1)

ugly_trol = Troll("Pub")
print("Ugly troll - {}".format(ugly_trol))
ugly_trol.take_damage(5)
print(ugly_trol)
print()

another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
# print(brother)

ugly_trol.grunt()
another_troll.grunt()
brother.grunt()
print()

vamp = Vampire("Vlad")
# vamp.take_damage(13)
# print(vamp)

while vamp.alive:
    vamp.take_damage(2)
    print(vamp)