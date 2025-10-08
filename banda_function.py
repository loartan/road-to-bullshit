def collecting_data():
    print("--- НАЧИНАЕМ СБОР ДАНИ ---")
    band_data = {}
    count = int(input("Сколько членов в банде? "))
    for i in range(count):
        name = input(f"Как зовут члена {i+1}? ")
        money = int(input(f"Сколько внес {name}? "))
        band_data[name] = money
    return band_data

def analizing_and_report(data_dict: dict):
    print("\n--- АНАЛИТИЧЕСКИЙ ОТДЕЛ ДОКЛАДЫВАЕТ ---")
    count = len(data_dict)
    total = sum(data_dict.values())
    rich = max(data_dict, key=data_dict.get)
    max_amount = data_dict[rich]

    print(f"Количество членов: {count}")
    print(f"Общая сумма: {total}")
    print(f"Член, который внес больше всех: {rich}")
    print(f"Он внес: {max_amount}")

our_band = collecting_data()
print(f"DEBUG: Собрано: {analizing_and_report}")
analizing_and_report(our_band)
print("\n--- Сходка окончена, расходимся ---")
