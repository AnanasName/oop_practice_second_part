import random


class Cell:
    def __init__(self, taken=False, taken_by_first_player=False, number: int = 0):
        self.__taken = taken
        self.__taken_by_first_player = taken_by_first_player
        self.__number = number

    def is_taken(self):
        return self.__taken

    def is_taken_by_first_player(self):
        return self.__taken_by_first_player

    def get_number(self):
        return self.__number

    def take_cell(self, taken_by_first_player):
        self.__taken = True
        self.__taken_by_first_player = taken_by_first_player


class Board:

    def __init__(self):
        self.__cells = list()
        for i in range(1, 10):
            self.__cells.append(Cell(number=i))

    def print_board(self):
        self.__print_game_row(list(range(1, 4)))
        print("-+-+-")

        self.__print_game_row(list(range(4, 7)))
        print("-+-+-")

        self.__print_game_row(list(range(7, 10)))

    def is_cell_taken(self, index: int):
        return self.__get_cell(index).is_taken()

    def take_cell(self, index: int, taken_by_first_player: bool):
        self.__get_cell(index).take_cell(taken_by_first_player)

    def check_if_win(self, is_first_player: bool) -> bool:
        if self.__check_three_in_row([1, 2, 3], is_first_player):
            return True
        if self.__check_three_in_row([1, 4, 7], is_first_player):
            return True
        if self.__check_three_in_row([1, 5, 9], is_first_player):
            return True
        if self.__check_three_in_row([4, 5, 6], is_first_player):
            return True
        if self.__check_three_in_row([7, 8, 9], is_first_player):
            return True
        if self.__check_three_in_row([2, 5, 8], is_first_player):
            return True
        if self.__check_three_in_row([3, 6, 9], is_first_player):
            return True
        if self.__check_three_in_row([3, 5, 7], is_first_player):
            return True
        return False

    def __check_three_in_row(self, indexes: list[int], is_first_player: bool) -> bool:
        for index in indexes:
            if (not self.__get_cell(index).is_taken_by_first_player() == is_first_player) or not self.is_cell_taken(
                    index):
                return False
        return True

    def __get_cell(self, index: int) -> Cell:
        return next(filter(lambda cell: cell.get_number() == index, self.__cells))

    def __print_game_row(self, indexes: list):
        print(self.__get_symbol_to_print(self.__get_cell(indexes[0])), end="|")
        print(self.__get_symbol_to_print(self.__get_cell(indexes[1])), end="|")
        print(self.__get_symbol_to_print(self.__get_cell(indexes[2])), end=f" {indexes[0]} {indexes[1]} {indexes[2]}\n")

    def __get_symbol_to_print(self, cell: Cell) -> str:
        if cell.is_taken() and cell.is_taken_by_first_player():
            return "X"
        elif cell.is_taken() and not cell.is_taken_by_first_player():
            return "O"
        else:
            return " "


class Player:
    def __init__(self, won=False):
        self.__won = won

    def is_won(self):
        return self.__won

    def make_won(self):
        self.__won = True


class Game:
    def __init__(self, first_player_turn=True):
        self.first_player_turn = first_player_turn

    def try_take_cell(self, game_board: Board, index: int, taken_by_first_player: bool) -> bool:
        if not game_board.is_cell_taken(index):
            game_board.take_cell(index, taken_by_first_player)
            return True
        return False

    def main(self):
        hum_player = Player()
        ai_player = Player()
        game_board = Board()

        counter = 9

        print("Welcome to tic-tac-toe!")
        game_board.print_board()

        while not hum_player.is_won or not ai_player.is_won or counter > 0:
            if self.first_player_turn:
                print("What is X's move? (1-9)")
                cell_number = input()
                while not self.try_take_cell(game_board, int(cell_number), True):
                    print("This cell already taken! Choose another!")
                    cell_number = input()
                game_board.print_board()
                if game_board.check_if_win(True):
                    hum_player.is_won()

            else:
                print("What is O's move? (1-9)")
                cell_number = random.randint(1, 9)
                while not self.try_take_cell(game_board, int(cell_number), False):
                    cell_number = random.randint(1, 9)
                print(cell_number)
                game_board.print_board()
                if game_board.check_if_win(False):
                    ai_player.make_won()

            self.first_player_turn = not self.first_player_turn
            counter = counter - 1

        if hum_player.is_won():
            print("X has won the game!")
        elif ai_player.is_won():
            print("O has won the game!")
        else:
            print("Game tied!")

        print("Thanks for playing!")


Game().main()
