name = input("Hello, whats your name?")
print(name)
board_size = input(name + ", please choose board size:")
print(board_size)
number_of_mines = input(name + ", for board size " + board_size + ", choose number of mines to allocate:")
print(name + ", the board size is: "+board_size+", number of mines is: "+number_of_mines + ". ENJOY!")
board_size = int(board_size)
number_of_mines = int(number_of_mines)
