#OUTPUT_IMAGE - двумерный массив, который содержит строку в качестве первого аргумента и место в этой строке - в качестве второго.
#Получается, что координата "у" увеличивается к низу выводимого в консоль изображения, "х" - стандартно, увеличивается вправо 
#относительно изображения, причем при обращении к обозначенному выше двумерному массиву первым аргументом обращаемся к "у", 
#затем - к "х".
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

#Вывод игрового поля в консоль.
for line_words in OUTPUT_IMAGE:
       for word in line_words:
           print(word, end="")
       print("\n", end="")

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
            officer_moveY = +1
        if officer_move == 'вверх':
            officer_moveX = 0
            officer_moveY = +1
        if officer_move == 'вверх вправо':
            officer_moveX = +1
            officer_moveY = +1
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
            officer_moveY = -1
        if officer_move == 'вниз':
            officer_moveX = 0
            officer_moveY = -1
        if officer_move == 'вниз вправо':
            officer_moveX = +1
            officer_moveY = -1
        if OUTPUT_IMAGE[officer_y + officer_moveY][officer_x + officer_moveX] != '.':
            print('Повторите ход.')
    
    