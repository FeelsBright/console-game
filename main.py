#OUTPUT_IMAGE - двумерный массив, который содержит строку в качестве первого аргумента и место в этой строке - в качестве второго.
#Получается, что координата "у" увеличивается к низу выводимого в консоль изображения, "х" - стандартно, увеличивается вправо 
#относительно изображения, причем при обращении к обозначенному выше двумерному массиву первым аргументом обращаемся к "у", 
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

#Ставим фигуры по местам.
OUTPUT_IMAGE[6][2] = 'O'
OUTPUT_IMAGE[7][6] = 'H'
OUTPUT_IMAGE[1][4] = 'W1'
OUTPUT_IMAGE[2][1] = 'W2'
OUTPUT_IMAGE[2][7] = 'W3'
wolfs_amount = 3
hp_w1 = 2
hp_w2 = 2
hp_w3 = 2

#Вывод игрового поля в консоль.
for line_words in OUTPUT_IMAGE:
       for word in line_words:
           print(word, end="")
       print("\n", end="")

#Тест. Проверка на обращение к относительному индексу массива.
#x = 1
#y = 1
#print(OUTPUT_IMAGE[6+x][2+y])
#OUTPUT_IMAGE[0][1]

#Определение позиции фигуры на поле
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


while wolfs_amount > 0:

    #Определяем позицию офицера в двумерном массиве
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

    #Считываем ход офицера
    officer_moveX = 0
    officer_moveY = 0
    while OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] != ".":
        officer_move = input('Куда ходит офицер? Возможные варианты: вверх влево, вверх, вверх вправо, влево, остаться на месте, вправо, вниз влево, вниз, вниз вправо\n')
        if officer_move == 'вверх влево':
            officer_moveX = -1
            officer_moveY = -1
        if officer_move == 'вверх':
            officer_moveX = 0
            officer_moveY = -1
        if officer_move == 'вверх вправо':
            officer_moveX = +1
            officer_moveY = -1
        if officer_move == 'влево':
            officer_moveX = -1
            officer_moveY = 0   
        if officer_move == 'остаться на месте':
            officer_moveX = 0
            officer_moveY = 0
        if officer_move == 'вправо':
            officer_moveX = +1
            officer_moveY = 0
        if officer_move == 'вниз влево':
            officer_moveX = -1
            officer_moveY = +1
        if officer_move == 'вниз':
            officer_moveX = 0
            officer_moveY = +1
        if officer_move == 'вниз вправо':
            officer_moveX = +1
            officer_moveY = +1
        if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] != ".":
            print('Ошибка. Повторите ход.')
    
    OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] = 'O'
    OUTPUT_IMAGE[officer_y][officer_x] = "."
    officer_x = officer_x + officer_moveX
    officer_y = officer_y + officer_moveY

    #Атака офицера: выходим из цикла, когда получаем верное направление атаки.
    officer_attack = 0
    while officer_attack not in ['вверх влево', 'вверх вправо', 'вниз влево', 'вниз вправо']:  
        officer_attack = input('В каком направлении атакует офицер? Возможные варианты: вверх влево, вверх вправо, вниз влево, вниз вправо.')
        if officer_attack == 'вверх влево':
            officer_attack_x = -1
            officer_attack_y = -1
            if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                hp_w1 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':     
                hp_w2 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                hp_w3 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            else:
                print('Ошибка. Введите направление атаки.')
        if officer_attack == 'вверх вправо':
            officer_attack_x = +1
            officer_attack_y = -1
            if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                hp_w1 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':     
                hp_w2 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                hp_w3 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            else:
                print('Ошибка. Введите направление атаки.')
        if officer_attack == 'вниз влево':
            officer_attack_x = -1
            officer_attack_y = +1
            if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                hp_w1 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':     
                hp_w2 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                hp_w3 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            else:
                print('Ошибка. Введите направление атаки.')
        if officer_attack == 'вниз вправо':
            officer_attack_x = +1
            officer_attack_y = +1
            if OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W1':
                hp_w1 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W2':     
                hp_w2 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            elif OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] == 'W3':
                hp_w3 = 0
                OUTPUT_IMAGE[officer_y + officer_attack_y][officer_x + officer_attack_x] = "."
            else:
                print('Ошибка. Введите направление атаки.')
