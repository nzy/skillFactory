import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали


def game_core_v3(number):

    nmin = 1
    nmax = 101

    count = 1
    predict = int(nmax/2)

    while number != predict:
        count += 1
        if number > predict:
            nmin = predict
            predict = nmin + (nmax - nmin)//2
        elif number < predict:
            nmax = predict
            predict = nmin + (nmax - nmin)//2
    return count # выход из цикла, если угадали


# Проверяем
# score_game(game_core_v2)
score_game(game_core_v3)