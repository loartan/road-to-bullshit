count_members = int(input("Сколько в банде члэнов? "))
band = []
money_band = []

for i in range(1, count_members + 1):
    name = input(f"Введи имя члэна {i}: ")
    band.append(name)
    money = int(input(f"Сколько занес {name}? "))
    money_band.append(money)
    
print("--- ИТОГИ СХОДКИ ---")
print(f"Всего бойцов: {len(band)}")
print(f"Наша братва: {band}")
print("Общак:", sum(money_band))
print(f"В среднем каждый скинулся по {sum(money_band)/len(band)}")
