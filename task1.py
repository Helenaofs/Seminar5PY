# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = "оыватплйо лыабвва ывлабвдо ывдл23л ывда25лт 1абв ывл"
print(my_str)

my_list = my_str.split()

result = []
for word in my_list:
    if "абв" not in word:
        result.append(word)

print(' '.join(result))
