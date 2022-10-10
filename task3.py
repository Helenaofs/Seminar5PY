# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))


def game_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')


def move(choice_player):
    trigger = False
    while not trigger:
        player_index = input(choice_player + ' - выберите ячейку от 1 до 9: ')
        try:
            player_index =int(player_index)
        except:
            print('Некорректный ввод, попробуйте еще раз')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in ('X' or '0')):
                board[player_index-1] = choice_player
                trigger = True
            else:
                print('Эта ячейка занята, выберите другую')
        else:
            print('Введите еще раз')


def win_line(board):
    win = ((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def game(board):
    count = 0
    trigger = False
    while not trigger:
        game_board(board)
        if count % 2 == 0:
            move('X')
        else:
            move('0')
        count +=1
        if count > 4:
            any_win = win_line(board)
            if any_win:
                print(any_win, ' - победил!')
                trigger = True
                break
            if count == 9:
                print('Ничья!')
        game_board(board)


game(board)
game_board(board)
