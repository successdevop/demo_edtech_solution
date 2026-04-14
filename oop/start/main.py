from player import Player
from enemy import Enemy, Troll, Vampire, VampyreKing

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(20)
print(dracula)

# tim = Player("Tim")
#
# enemy_1 = Enemy("Basic enemy", 12, 1)
#
# ugly_trol = Troll("Pub")
# print("Ugly troll - {}".format(ugly_trol))
# ugly_trol.take_damage(5)
# print(ugly_trol)
# print()
#
# another_troll = Troll("Ug")
# # print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# # print(brother)
#
# ugly_trol.grunt()
# another_troll.grunt()
# brother.grunt()
# print()
#
# vamp = Vampire("Vlad")
# # vamp.take_damage(13)
# # print(vamp)
#
# vKing = VampyreKing("Putin")
# print(vKing)


# while vKing._alive:
#     vKing.take_damage(1)
#     print(vKing)
