class Monster:
    def __init__(self, name = "Неизвестный", hp = 100, damage = 0):
        self.name = name
        self.hp = hp
        self.damage = damage

data1 = input("Введите первого монстра (Имя, Здоровье, Урон): ").split()
m1 = Monster(data1[0], int(data1[1]), int(data1[2]))

data2 = input("Введите второго монстра (Имя, Здоровье, Урон): ").split()
m2 = Monster(data2[0], int(data2[1]), int(data2[2]))

# print(f"Монстр 1: {m1.name}, Здоровье: {m1.hp}, Урон: {m1.damage}")
# print(f"Монстр 2: {m2.name}, Здоровье: {m2.hp}, Урон: {m2.damage}")

print()

while True:
    m2.hp -= m1.damage
    if m2.hp < 0:
        m2.hp = 0

    print(f"{m1.name} наносит удар!")
    print(f"У {m2.name} осталось {m2.hp} HP")
    print()
    
    if m2.hp == 0:
        print(f"Победил {m1.name}!")
        break

    m1.hp -= m2.damage
    if m1.hp <0:
        m1.hp = 0

    print(f"{m2.name} наносит удар!")
    print(f"У {m1.name} осталось {m1.hp} HP")
    print()

    if m1.hp == 0:
        print(f"Победил {m2.name}!")
        break