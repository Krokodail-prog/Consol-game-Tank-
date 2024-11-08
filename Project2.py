from random import randint


class Tank:
    def __init__(self, tank_name, armor, min_damage, max_damage, HP, armor_angle):
        self.tank_name = tank_name
        self.armor = armor
        self.HP = HP
        self.damage = randint(min_damage, max_damage)
        self.armor_angle = armor_angle

    def print_info(self):
        print(
            f"Танк {self.tank_name} имеет лобовую броню - {self.armor}, имеет {self.HP} здоровья, а его урон равен {self.damage}")

    def health_down(self, enemy_damage, armor):
        current_damage = enemy_damage - enemy_damage * (armor / 1000)
        self.HP -= current_damage
        print(f"По танку {self.tank_name} был нанесен урон в размере {current_damage} и у него осталось {self.HP}")

    def shot(self, enemy):
        if randint(0, 100) > enemy.armor_angle:
            print(f"Рикошет по {enemy.tank_name}")
        else:
            if enemy.HP <= 0 or self.damage >= enemy.HP:
                enemy.HP = 0
                print(f"Танк {enemy.tank_name} уничтожен")
            else:
                enemy.health_down(self.damage, enemy.armor)
                print(f"Танк {enemy.tank_name} получил выстрел")


enemy = Tank("ENEMY", 50, 50, 75, 1000, 85)
tank = Tank("T-34", 100, 100, 160, 1000, 50)

while enemy.HP > 0 and tank.HP > 0:
    print("Выберите одно из действий")
    print('1 - shot')
    print('2 - info')

    choice = int(input("---->"))

    if choice == 1:
        enemy.shot(tank)
        tank.shot(enemy)

    if choice == 2:
        tank.print_info()
        enemy.print_info()
