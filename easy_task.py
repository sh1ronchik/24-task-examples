file = open('24.txt') # открытие файла
s = file.readline() # чтение строки из файла

# инициализируем два счётчика: для текущей длины и для максимальной длины последовательности символов "B"
current_length = 1
max_length = 1

for i in range(len(s)-1): # запускаем цикл для всех символов, кроме последнего
    # если соседние символы равны нужному("B"), то увеличиваем длину текущей последовательности на единицу
    if s[i] == 'B' and s[i+1] == 'B':
        current_length += 1
        # выбираем максимум из счетчиков текущей и максимальной длины и присваиваем это значение счетчику максимальной длины
        max_length = max(max_length, current_length)
    else:
        current_length = 1 # последовательность прервалась - возращаемз значение счетчика к стандартному

print(max_length) # вывод максимальной длины последовательности символов "В"
