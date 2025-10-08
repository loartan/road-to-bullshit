count_members = int(input("Сколько в банде члэнов? "))
band = []
total_money = 0

for i in range(1, count_members + 1):
    name = input(f"Введи имя члэна {i}: ")
    band.append(name)
    money = int(input(f"Сколько занес {name}? "))
    total_money += money
    
print("--- ИТОГИ СХОДКИ ---")
print(f"Всего бойцов: {len(band)}")
print(f"Наша братва: {band}")
print("Общак:", total_money)
print(f"В среднем каждый скинулся по {total_money/len(band)}")
