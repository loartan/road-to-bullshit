my_dict = {}
count_members = int(input("Сколько членов в нашей банде? "))

for i in range(count_members):
    name = input(f"Введите имя члэна {i+1}: ")
    money = int(input(f"Сколько внес {name}? "))
    my_dict[name] = money
    
most_money = max(my_dict.values())
rich_member = ""
# for member in my_dict.keys():
#     if my_dict[member] == most_money:
#         rich_member = member
rich_member = max(my_dict, key=my_dict.get)
print("--- ИТОГИ СХОДКИ ---")
print(f"Количество члэнов в банде: {len(my_dict)}")
print(f"Список члэнов: {my_dict.keys()}")
print(f"Общая сумма в сейфе: {sum(my_dict.values())}")
print(f"Больше всех занес: {rich_member}")
print(f"Этот член внес: {most_money}")