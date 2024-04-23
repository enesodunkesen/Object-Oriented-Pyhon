# from player import Player
#
# enes = Player("enes")
# print(enes)
#
# enes.level = 3
# print(enes)
# enes.level = -10
# print(enes)
# enes.level = 5
# print(enes)

from enemy import Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Urg")
print("Another - {}".format(Troll("Urg")))

brother = Troll("Burg")
print("Brother - {}".format(brother))

brother.grunt()

print("*"*40)

immortal = Vampyre("Vlad")
print(immortal)
while immortal.alive:
    immortal.take_damage(2)
