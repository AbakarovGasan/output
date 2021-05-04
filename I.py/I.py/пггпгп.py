import random

def create_player():
    player = {}
    player["Имя"] = input("Введите имя игрока: ")
    player["health"] = 20
    player["damage"] = 20
    в:str
    в=input("Увеличить жизни - health. Увеличить атаку - damage: ")
    player[в] += 20
    player["health"] *=100
    return player

def hit(agressor, victim):
    damage = agressor["damage"] + random.randint(
        -agressor["damage"],agressor["damage"])
    victim["health"] -= damage
    
    if damage == 0:
        print("Промазал")
    if damage == agressor["damage"] * 2:
        print("Крит!!!")

    print("{0[Имя]} нанес {1[Имя]} {2} урона".format(
        agressor,victim,damage))

def show_params(player):
    print("{0[Имя]}: {0[health]}".format(player))

def fight(player1, player2):
    while True:
        hit(player1, player2)
        hit(player2, player1)
        show_params(player1)
        show_params(player2)
        input()
        if player1["health"] <= 0:
            print(player2["Имя"],"убил", player1["Имя"])
            break
        if player2["health"] <= 0:
            print(player1["Имя"],"убил", player2["Имя"])
            break


player1 = create_player()
player2 = create_player()

print(player1, player2)
fight(player1, player2)


