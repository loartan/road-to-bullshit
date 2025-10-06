vova = 15000
petya = 25000
artem = 3500

total_cash = vova + petya + artem

print("Пацаны, слушай сюда!")
print(f"В нашем общаке сейчас: {total_cash} рублей")

vova_share = (vova / total_cash) * 100
petya_share = (petya / total_cash) * 100
artem_share = (artem / total_cash) * 100

print(f"Доля Вована: {vova_share:.2f}%")
print(f"Доля Пети: {petya_share:.2f}%")
print(f"Доля Артёма: {artem_share:.2f}%")