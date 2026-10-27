# class Monster:
#     def __init__(self, name = "Неизвестный", species = "Упырь", hp = 50):
#         self.name = name
#         self.species = species
#         self.hp = hp

# # dracula = Monster("Дракула", "Вампир", 100)
# # lycan = Monster("Люкан", "Оборотень", 250)

class Monster:
    def __init__(self, name = "Неизвестный", hp = 100, damage = 0):
        self.name = name
        self.hp = hp
        self.damage = damage

data1 = input().split()
m1 = Monster(data1[0], int(data1[1]), int(data1[2]))

data2 = input().split()
m2 = Monster(data2[0], int(data2[1]), int(data2[2]))

print(f"Монстр 1: {m1.name}, Здоровье: {m1.hp}, Урон: {m1.damage}")
print(f"Монстр 2: {m2.name}, Здоровье: {m2.hp}, Урон: {m2.damage}")