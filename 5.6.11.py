stol = list(range(1, 10))


def draw_board(stol):
    print("-" * 13)
    for x in range(3):
        print("|", stol[0 + x * 3], "|", stol[1 + x * 3], "|", stol[2 + x * 3], "|")
        print("-" * 14)


def take_input(player):
    valid = False
    while not valid:
        player_x = input("Куда поставим " + player + "? ")
        try:
            player_x = int(player_x)
        except:
            print("Ошибка. Вы уверены, что ввели число?")
            continue
        if 1 <= player_x <= 9:
            if str(stol[player_x - 1]) not in "XO":
                stol[player_x - 1] = player
                valid = True
            else:
                print("Клетка уже занята")



def check_win (stol):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if stol[each[0]] == stol[each[1]] == stol[each[2]]:
            return stol[each[0]]
    return False



def main(stol):
    counter = 0
    win = False
    while not win:
        draw_board(stol)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(stol)
            if tmp:
                print(tmp, "Вы выиграли")
                win = True

                break



        if counter == 9:
            print("Ничья")
            break

        if counter == 10:
            print("Начать игру заново")
        break
    draw_board(stol)