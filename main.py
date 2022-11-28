from random import randint
from os import system

#OUTPUT_IMAGE - двумерный массив, который содержит строку в качестве первого аргумента и место в этой строке - в качестве второго.
#Получается, что координата "у" увеличивается к низу выводимого в консоль изображения, "х" - стандартно, увеличивается вправо 
#относительно изображения, причем при обращении к этому двумерному массиву первым аргументом обращаемся к "у", 
#затем - к "х". В дальнейшем коде при использовании ординаты точки следует помнить об этом.
OUTPUT_IMAGE = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ]

#Ставим фигуры по местам, инициализируем заданные правилами игры переменные. Буквенные короткие перменные для более простой отладки кода.
OUTPUT_IMAGE[6][2] = 'O'
OUTPUT_IMAGE[7][6] = 'H'
OUTPUT_IMAGE[1][4] = 'W1'
OUTPUT_IMAGE[2][1] = 'W2'
OUTPUT_IMAGE[2][7] = 'W3'
wolfs_amount = 3
hp_w1 = 2
hp_w2 = 2
hp_w3 = 2


#Очистка консоли, чтобы игра начиналась с чистого листа.
system("cls||clear")

#Вывод игрового поля в консоль.
for line_words in OUTPUT_IMAGE:
       for word in line_words:
           print(word, end="")
       print("\n", end="")

#Печатаем пустую строку для лучшей читабельности
print('\n')

#Определение позиции фигуры офицера на поле (в двумерном массиве)
officer_x = 0
officer_y = 0
count_x = 0
count_y = 0
for line_words in OUTPUT_IMAGE:
    count_y += 1
    for word in line_words:
        count_x += 1
        if word == 'O':
            count_x -= 1
            count_y -= 1
            officer_x = count_x % 8
            officer_y = count_y

#Определение позиции фигуры коня на поле
horse_x = 0
horse_y = 0
count_x = 0
count_y = 0
for line_words in OUTPUT_IMAGE:
    count_y += 1
    for word in line_words:
        count_x += 1
        if word == 'H':
            count_x -= 1
            count_y -= 1
            horse_x = count_x % 8
            horse_y = count_y

#Определение позиции фигуры первого волка на поле
w1_x = 0
w1_y = 0
count_x = 0
count_y = 0
for line_words in OUTPUT_IMAGE:
    count_y += 1
    for word in line_words:
        count_x += 1
        if word == 'W1':
            count_x -= 1
            count_y -= 1
            w1_x = count_x % 8
            w1_y = count_y

#Определение позиции фигуры второго волка на поле
w2_x = 0
w2_y = 0
count_x = 0
count_y = 0
for line_words in OUTPUT_IMAGE:
    count_y += 1
    for word in line_words:
        count_x += 1
        if word == 'W2':
            count_x -= 1
            count_y -= 1
            w2_x = count_x % 8
            w2_y = count_y

#Определение позиции фигуры третьего волка на поле
w3_x = 0
w3_y = 0
count_x = 0
count_y = 0
for line_words in OUTPUT_IMAGE:
    count_y += 1
    for word in line_words:
        count_x += 1
        if word == 'W3':
            count_x -= 1
            count_y -= 1
            w3_x = count_x % 8
            w3_y = count_y


while wolfs_amount > 0:
    #Считываем ход офицера
    officer_moveX = 0
    officer_moveY = 0
    flag_officer = False
    while flag_officer == False:
        officer_move = input('Куда ходит офицер? Возможные варианты: 0 - остаться на месте, 1 - вверх влево, 2 - вверх, 3 - вверх вправо, 4 - влево, 5 - вправо, 6 - вниз влево, 7 - вниз, 8 - вниз вправо\n')
        if officer_move == '1':
            officer_moveX = -1
            officer_moveY = -1
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n')                
        elif officer_move == '2':
            officer_moveX = 0
            officer_moveY = -1
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        elif officer_move == '3':
            officer_moveX = +1
            officer_moveY = -1
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        elif officer_move == '4':
            officer_moveX = -1
            officer_moveY = 0   
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        elif officer_move == '0':
            officer_moveX = 0
            officer_moveY = 0
            flag_officer = True
        elif officer_move == '5':
            officer_moveX = +1
            officer_moveY = 0
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        elif officer_move == '6':
            officer_moveX = -1
            officer_moveY = +1
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        elif officer_move == '7':
            officer_moveX = 0
            officer_moveY = +1
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        elif officer_move == '8':
            officer_moveX = +1
            officer_moveY = +1
            try:
                if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] not in ['H', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
                    OUTPUT_IMAGE[officer_y][officer_x] = "."
                    officer_x = officer_x + officer_moveX
                    officer_y = officer_y + officer_moveY
                    flag_officer = True
                else:
                    print('Поле занято другим существом. Выберите другую клетку.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения\n') 
        else:
            print('Введите корректное направление движения офицера.\n')

    #Печатаем пустую строку для лучшей читабельности
    print('\n')

    #Вывод игрового поля в консоль после хода офицера.
    for line_words in OUTPUT_IMAGE:
        for word in line_words:
           print(word, end="")
        print("\n", end="")

    #Печатаем пустую строку для лучшей читабельности
    print('\n')


    #Атака офицера: выходим из цикла, когда получаем корректное направление атаки.
    officer_attack = 0
    flag_officer_attack = False
    while flag_officer_attack == False:  
        officer_attack = input('В каком направлении атакует офицер? Возможные варианты: 1 - вверх влево, 2 - вверх вправо, 3 - вниз влево, 4 - вниз вправо, 0 - пропуск атаки.\n')
        if officer_attack == '0':
            flag_officer_attack == True
            break
        elif officer_attack == '1':
            officer_attack_x = -1
            officer_attack_y = -1
            try:
                if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] not in ['H', 'O', "."]:
                    if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w1 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w2 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w3 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    else:
                        print('Ошибка. Введите поле, на котором присутствуют объекты для атаки или выберите пропуск хода.\n')
                else:
                    print('Выберите клетку для атаки, на которой присутствует волк.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для атаки\n')    
        elif officer_attack == '2':
            officer_attack_x = +1
            officer_attack_y = -1
            try:
                if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] not in ['H', 'O', "."]:
                    if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w1 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w2 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w3 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    else:
                        print('Ошибка. Введите поле, на котором присутствуют объекты для атаки или выберите пропуск хода.\n')
                else:
                    print('Выберите клетку для атаки, на которой присутствует волк.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для атаки\n') 
        elif officer_attack == '3':
            officer_attack_x = -1
            officer_attack_y = +1
            try:
                if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] not in ['H', 'O', "."]:
                    if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w1 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w2 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w3 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    else:
                        print('Ошибка. Введите поле, на котором присутствуют объекты для атаки или выберите пропуск хода.\n')
                else:
                    print('Выберите клетку для атаки, на которой присутствует волк.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для атаки\n') 
        elif officer_attack == '4':
            officer_attack_x = +1
            officer_attack_y = +1
            try:
                if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] not in ['H', 'O', "."]:
                    if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w1 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w2 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                        OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
                        hp_w3 = 0
                        wolfs_amount -= 1
                        flag_officer_attack = True
                    else:
                        print('Ошибка. Введите поле, на котором присутствуют объекты для атаки или выберите пропуск хода.\n')
                else:
                    print('Выберите клетку для атаки, на которой присутствует волк.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для атаки\n') 
        else: 
            print('Введите корректное направление атаки офицера из перечисленного списка.\n')

    #Печатаем пустую строку для лучшей читабельности
    print('\n')

    #Вывод игрового поля в консоль после атаки офицера.
    for line_words in OUTPUT_IMAGE:
        for word in line_words:
           print(word, end="")
        print("\n", end="")

    #Печатаем пустую строку для лучшей читабельности
    print('\n')


    #Ход коня.    
    horse_moveX = 0
    horse_moveY = 0
    flag_horse = False
    while flag_horse == False:
        horse_move = input('Куда ходит конь? Возможные варианты: 1 - вверх на 2 и влево на 1, 2 - вверх на 2 и вправо на 1, 3 - влево на 2 и вверх на 1, 4 - влево на 2 и вниз на 1, 5 - вниз на 2 и влево на 1, 6 - вниз на 2 и вправо на 1, 7 - вправо на 2 и вниз на 1, 8 - вправо на 2 и вверх на 1\n')
        if horse_move == '1':
            horse_moveX = -1
            horse_moveY = -2
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n')            
        elif horse_move == '2':
            horse_moveX = +1
            horse_moveY = -2
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n')      
        elif horse_move == '3':
            horse_moveX = -1
            horse_moveY = -1
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n')  
        elif horse_move == '4':
            horse_moveX = -2
            horse_moveY = +1  
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n')  
        elif horse_move == '5':
            horse_moveX = -1
            horse_moveY = +2
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n')  
        elif horse_move == '6':
            horse_moveX = +1
            horse_moveY = +2
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n') 
        elif horse_move == '7':
            horse_moveX = +2
            horse_moveY = +1
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n') 
        elif horse_move == '8':
            horse_moveX = +2
            horse_moveY = -1
            try:
                if OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] not in ['O', 'W1', 'W2', 'W3']:
                    OUTPUT_IMAGE[horse_y + horse_moveY][horse_x + horse_moveX] = 'H'
                    OUTPUT_IMAGE[horse_y][horse_x] = "."
                    horse_x = horse_x + horse_moveX
                    horse_y = horse_y + horse_moveY
                    flag_horse = True
                else:
                    print('Указанное поле занято.\n')
            except IndexError:
                print('Вы вышли за границы игрового поля. Введите существующую клетку для перемещения коня.\n') 
        else:
            print('Введите корректное направление движения коня из перечисленного списка.\n')

    #Печатаем пустую строку для лучшей читабельности
    print('\n')

    #Вывод игрового поля в консоль после хода коня.
    for line_words in OUTPUT_IMAGE:
        for word in line_words:
           print(word, end="")
        print("\n", end="")

    #Печатаем пустую строку для лучшей читабельности
    print('\n')


    #Атака коня: выходим из цикла, когда получаем корректное направление атаки.
    horse_attack = 0
    flag_horse_attack = False
    while flag_horse_attack == False:  
        horse_attack = input('В каком направлении атакует конь? Возможные варианты: 1 - вверх на 2 и влево на 1, 2 - вверх на 2 и вправо на 1, 3 - влево на 2 и вверх на 1, 4 - влево на 2 и вниз на 1, 5 - вниз на 2 и влево на 1, 6 - вниз на 2 и вправо на 1, 7 - вправо на 2 и вниз на 1, 8 - вправо на 2 и вверх на 1, 0 - пропуск атаки.\n')
        if horse_attack == '0':
            flag_horse_attack = True
            break
        elif horse_attack == '1':
            horse_attack_x = -1
            horse_attack_y = -2
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')
        elif horse_attack == '2':
            horse_attack_x = +1
            horse_attack_y = -2
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')
        elif horse_attack == '3':
            horse_attack_x = -2
            horse_attack_y = -1
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n') 
        elif horse_attack == '4':
            horse_attack_x = -2
            horse_attack_y = +1
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')
        elif horse_attack == '5':
            horse_attack_x = -1
            horse_attack_y = +2
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')  
        elif horse_attack == '6':
            horse_attack_x = +1
            horse_attack_y = +2
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')
        elif horse_attack == '7':
            horse_attack_x = +2
            horse_attack_y = +1
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')
        elif horse_attack == '8':
            horse_attack_x = +2
            horse_attack_y = -1
            try:   
                if OUTPUT_IMAGE[horse_y + horse_attack_x][horse_x + horse_attack_y] not in ['O', 'H', '.']: 
                    if OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W1':
                        hp_w1 -= 1
                        if hp_w1 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W2':     
                        hp_w2 -= 1
                        if hp_w2 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    elif OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] == 'W3':
                        hp_w3 -= 1
                        if hp_w3 == 0:
                            wolfs_amount -= 1
                            OUTPUT_IMAGE[horse_y + horse_attack_y][horse_x + horse_attack_x] = 'H'
                            OUTPUT_IMAGE[horse_y][horse_x] = "."
                            horse_x = horse_x + horse_attack_x
                            horse_y = horse_y + horse_attack_y
                            flag_horse_attack = True
                    else:
                        print('Ошибка. Введите корректную цель атаки.\n') 
                else:
                    print('Выберите корректную цель для атаки. Если она отсутствует - пропустите ход.\n')
            except IndexError:
                print('Поле атаки выходит за границы игрового поля. Введите существующую клетку для атаки.\n')
        else:
            print('Введите корректное направление атаки из приведенного списка.\n')  

    #Печатаем пустую строку для лучшей читабельности
    print('\n')

    #Вывод игрового поля в консоль после атаки коня.
    for line_words in OUTPUT_IMAGE:
        for word in line_words:
           print(word, end="")
        print("\n", end="")

    #Печатаем пустую строку для лучшей читабельности
    print('\n')


    print('Теперь ход волков:\n')

    #Ход первого волка.
    w1_moveX = 0
    w1_moveY = 0
    flag_wolf1 = False
    while flag_wolf1 == False:
        w1_move = randint(1, 9)
        w1_moveX = 0
        w1_moveY = 0
        if w1_move == 1:
            w1_moveX = -1
            w1_moveY = -1
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True
            except IndexError:
                continue
        elif w1_move == 2:
            w1_moveX = 0
            w1_moveY = -1
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w1_move == 3:
            w1_moveX = +1
            w1_moveY = -1
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w1_move == 4:
            w1_moveX = -1
            w1_moveY = 0
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w1_move == 5:
            w1_moveX = 0
            w1_moveY = 0
            flag_wolf1 = True
        elif w1_move == 6:
            w1_moveX = +1
            w1_moveY = 0
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w1_move == 7:
            w1_moveX = -1
            w1_moveY = +1
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w1_move == 8:
            w1_moveX = 0
            w1_moveY = +1
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w1_move == 9:
            w1_moveX = +1
            w1_moveY = +1
            try:   
                if OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] == ".":  
                    OUTPUT_IMAGE[w1_y + w1_moveY][w1_x + w1_moveX] = 'W1'  
                    OUTPUT_IMAGE[w1_y][w1_x] = "."
                    w1_x = w1_x + w1_moveX
                    w1_y = w1_y + w1_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        
    #Ход второго волка.
    w2_moveX = 0
    w2_moveY = 0
    flag_wolf1 = False
    while flag_wolf1 == False:
        w2_move = randint(1, 9)
        w2_moveX = 0
        w2_moveY = 0
        if w2_move == 1:
            w2_moveX = -1
            w2_moveY = -1
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True
            except IndexError:
                continue
        elif w2_move == 2:
            w2_moveX = 0
            w2_moveY = -1
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w2_move == 3:
            w2_moveX = +1
            w2_moveY = -1
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w2_move == 4:
            w2_moveX = -1
            w2_moveY = 0
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w2_move == 5:
            w2_moveX = 0
            w2_moveY = 0
            flag_wolf1 = True
        elif w2_move == 6:
            w2_moveX = +1
            w2_moveY = 0
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w2_move == 7:
            w2_moveX = -1
            w2_moveY = +1
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w2_move == 8:
            w2_moveX = 0
            w2_moveY = +1
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w2_move == 9:
            w2_moveX = +1
            w2_moveY = +1
            try:   
                if OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] == ".":  
                    OUTPUT_IMAGE[w2_y + w2_moveY][w2_x + w2_moveX] = 'W2'  
                    OUTPUT_IMAGE[w2_y][w2_x] = "."
                    w2_x = w2_x + w2_moveX
                    w2_y = w2_y + w2_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
    
    #Ход третьего волка.
    w3_moveX = 0
    w3_moveY = 0
    flag_wolf1 = False
    while flag_wolf1 == False:
        w3_move = randint(1, 9)
        w3_moveX = 0
        w3_moveY = 0
        if w3_move == 1:
            w3_moveX = -1
            w3_moveY = -1
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True
            except IndexError:
                continue
        elif w3_move == 2:
            w3_moveX = 0
            w3_moveY = -1
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w3_move == 3:
            w3_moveX = +1
            w3_moveY = -1
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w3_move == 4:
            w3_moveX = -1
            w3_moveY = 0
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w3_move == 5:
            w3_moveX = 0
            w3_moveY = 0
            flag_wolf1 = True
        elif w3_move == 6:
            w3_moveX = +1
            w3_moveY = 0
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w3_move == 7:
            w3_moveX = -1
            w3_moveY = +1
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True  
            except IndexError:
                continue
        elif w3_move == 8:
            w3_moveX = 0
            w3_moveY = +1
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
        elif w3_move == 9:
            w3_moveX = +1
            w3_moveY = +1
            try:   
                if OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] == ".":  
                    OUTPUT_IMAGE[w3_y + w3_moveY][w3_x + w3_moveX] = 'W3'  
                    OUTPUT_IMAGE[w3_y][w3_x] = "."
                    w3_x = w3_x + w3_moveX
                    w3_y = w3_y + w3_moveY
                    flag_wolf1 = True 
            except IndexError:
                continue
    
    #Вывод игрового поля в консоль после того, как все 3 волка походили.
    for line_words in OUTPUT_IMAGE:
        for word in line_words:
           print(word, end="")
        print("\n", end="")

    #Печатаем пустую строку для лучшей читабельности
    print('\n')


print('Ура, вы победили всех волков!\n')

#Заготовки картинок эмоджи и их коды в юникоде для обозначения существ на игровом поле для готовой программы:
#print('🐺') то же самое, что print('\U0001F43A')
#print('🐎') '\U0001F40E'
#print('👮') '\U0001F46E'
#print('🟩') '\U0001F7E9'

