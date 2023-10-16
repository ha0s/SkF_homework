#################### Запускать лучше в терминале UNIX в штатном Windows Терминале не работают ANSI кода)#####################
import random
symbol_user = 'X'
symbol_comp = 'O'
symbol_null = '-'

## Функция инициализации пустого поля. Возвращает матрицу(список-списков) игрового поля.
def gen_field(size = 3):
    size += 1
    p = [[symbol_null for j in range(size)] for i in range(size)] # Генерируем пустое поле
    for i in range(1, size): # Заполняем горизонтальный заголовок
        p[0][i] = str(i)
    for i in range(1, size): # Заполняем вертикальный заголовок
        p[i][0] = str(i)
    p[0][0] = ' '
    return  p

## Функция вывода поля в консоль.
def print_field(field):
    print("\033[H\033[J")
    print('\033[34m--------------------------------------------------\033[0m')
    print('\033[34m---------------КРЕСТИКИ - НОЛИКИ------------------\033[0m')
    print('\033[34m--------------------------------------------------\033[0m')
    for i in field:
        print ('            ', i)

## Функция выода результата игры.
def print_result(result):
    if result == 1:
        print('\033[33m--------------------------------------------------\033[0m')
        print('\033[33m----------------------НИЧЬЯ!----------------------\033[0m')
        print('\033[33m--------------------------------------------------\033[0m')
    elif result == 2:
        print('\033[32m--------------------------------------------------\033[0m')
        print('\033[32m+++++++++++++++++++ВЫ ПОБЕДИЛИ!+++++++++++++++++++\033[0m')
        print('\033[32m--------------------------------------------------\033[0m')
    elif result == 3:
        print('\033[31m--------------------------------------------------\033[0m')
        print('\033[31m----------------ПОБЕДИЛ КОМПЬЮТЕР!----------------\033[0m')
        print('\033[31m--------------------------------------------------\033[0m')

## Функция проверки и фиксации хода. Возвращает матрицу(список-списков) игрового поля.
def move_check(field, move, symbol, symbol_null = '-'):
    if field[int(move[1])][int(move[0])] == symbol_null: # Проверяем содержимое ячейки
        field[int(move[1])][int(move[0])] = symbol # Записываем в ячейку
        return field
    return False

## Функция хода кожаного мешка). Возвращает матрицу(список-списков) игрового поля.
def move_user(field):
    l = len(field) - 1
    while True:
        move = input (f'Ваш ход(Две цифры подряд от 1 до {l} :СтрокаКолонка пример"23"): ')[::-1]
        if len(move) != 2:
            print('Неправильное количество символов!')
        elif not move.isdigit():
            print('Вводить можно только цифры!')
        elif 0 < int(move[0]) <= l and 0 < int(move[1]) <= l:
            fiel = move_check(field, move, symbol_user)
            if type(fiel) == list:
                return fiel
            else:
                print('Такой ход уже был!')
        else:
            print(f'Ход вне диапазона игрового поля {l} на {l} невозможен!')

## Функция хода компьютера. Возвращает матрицу(список-списков) игрового поля.
def move_comp(field):
    while True:
        move = str(random.randint(1, len(field) - 1)) + str(random.randint(1, len(field) - 1))
        fiel = move_check(field, move, symbol_comp)
        if type(fiel) == list:
            return fiel

## Функция проверки условий выигрыша или ничьи. Возвращает True если игра окончена.
def check_conditions(field):
    field_ = []
    fields = []
    list_temp = []
    #Пересобераем массив без 0й строчки и 0й колонки.
    for i in range(1, len(field)):
        for j in range(1, len(field)):
            list_temp.append(field[i][j])
        field_.append(list_temp)
        list_temp = []
    n = len(field_)
    # Генерация строк
    for i in range(n):
        for j in range(n):
            list_temp.append(field_[i][j])
        fields.append(list_temp)
        list_temp = []
    # Генерация столбцов
    for i in range(n):
        for j in range(n):
            list_temp.append(field_[j][i])
        fields.append(list_temp)
        list_temp = []
    # Генерация диаганалей
    for i in range(n): # 1я диаганаль
        list_temp.append(field_[i][i])
    fields.append(list_temp)
    list_temp = []
    for i in range(n): # 2я диаганаль
        list_temp.append(field_[i][n - i -1])
    fields.append(list_temp)
    list_temp = []
    # Проверка победы
    for i in fields:
        if not symbol_null in i and not symbol_comp in i: # Победа пользователя
            print_result(2)
            return True
        elif not symbol_null in i and not symbol_user in i: # Победа компьютера
            print_result(3)
            return True
    # Проверка ничьи
    for i in field_:
        list_temp += i  # объединяем списки в один список
    if not symbol_null in list_temp:
        print_result(1)
        return True
    
## Функция инициализации
def init():
    field = []
    field = gen_field()
    print("\033[H\033[J") # Очистка вывода терминала
    print_field(field)
    return field

## Функция игрового процесса
def game_proc(field):
    while True:
        field = move_user(field)
        print_field(field)
        if check_conditions(field) == True:
            input('Продолжаем?')
            break
        field = move_comp(field)
        print_field(field)
        if check_conditions(field) == True:
            input('Продолжаем?')
            break






## ТЕЛО
while True:
    field = init()
    field = game_proc(field)


    


