print("--- Сходка. Скидываемся в общак ---")

vova_input = input("Сколько Вован занёс? ")
petya_input = input("Сколько Петя занёс? ")
artem_input = input("Сколько Артём занёс? ")

if vova_input.isdigit() and petya_input.isdigit() and artem_input.isdigit():
    total_input = int(vova_input) + int(petya_input) + int(artem_input)

    dolya_vova = int(vova_input) / total_input * 100
    dolya_petya = int(petya_input) / total_input * 100
    dolya_artem = int(artem_input) / total_input * 100
    
    print(f"Доля Вовы: {dolya_vova:.2f}%")
    print(f"Доля Пети: {dolya_petya:.2f}%")
    print(f"Доля Артём: {dolya_artem:.2f}%")
    
else:
    print("Ты долбаеб? Че ты ввел?")