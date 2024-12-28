import tkinter as tk

class Player:
    """A class to represent the player, including their name"""

    def __init__(self, name):
        """Initializes the player and assigns a name attribute"""
        self._name = name

    def get_player_name(self):
        """Returns the player object's name"""
        return self._name


class Mancala:
    """A class to represent the game, including the game board, and players."""

    def __init__(self):
        """
        Constructor for the Mancala class.Initializes the required data members. All data members are private.

        The game board list has the corresponding pits and stores:
        [player1 pit1, player1 pit2, player1 pit3, player1 pit4, player1 pit5, player1 pit6, player1 store, Player2
         pit1, player2 pit2, player2 pit3, player2 pit4, player2 pit5, player2 pit6, player2 store, ]
        """
        self._game_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._player_names = []

    def player_storage(self, player_name):
        """Adds player names to list"""
        self._player_names.append(player_name)

    def create_player(self, player_name):
        """takes one parameter of the player’s name as a string and returns the player object. """
        player = Player(player_name)
        self.player_storage(player_name)
        return player

    def print_board(self):
        """Prints the current state of the game board, split into player pits and stores"""
        board = self._game_board
        p1_store = board[6]
        p1_pits = board[0:6]
        p2_store = board[13]
        p2_pits = board[7:13]

        print(f"player1: \nstore: {p1_store} \n{p1_pits} \nplayer2: \nstore: {p2_store} \n{p2_pits} \n ")

    def return_num_seeds(self, i):
        """Returns the number of seeds at a specific index on the game board"""
        return self._game_board[i]

    def return_winner(self):
        """Returns the winner of the game. If the game isn't over, returns 'Game is not ended'"""
        board = self._game_board
        p1_pits = board[0:6]
        p2_pits = board[7:13]
        p1_name = self._player_names[0]
        p2_name = self._player_names[1]

        if set(p1_pits) == {0}:
            p1_total = board[6]
            p2_total = sum(board[7:14])
            if p1_total > p2_total:
                return f"Winner is player 1: {p1_name}"
            else:
                return f"Winner is player 2: {p2_name}"

        elif set(p2_pits) == 0:
            p1_total = sum(board[0:7])
            p2_total = board[13]
            if p1_total > p2_total:
                return f"Winner is player 1: {p1_name}"
            else:
                return f"Winner is player 2: {p2_name}"

        else:
            return "Game has not ended"

    def play_game(self, player_index, pit_index):
        """
        Taskes in the player index (1 or 2) and the pit index (1-6). Conducts the move at the corresponding pit, and
        takes into consideration the special rules of the game.

        If an invalid pit number is given, return "Invalid number for pit index"

        If the game is ended at this point, return "Game is ended"

        If the player 1 win an extra round following the special rule1, print out “player 1
        take another turn"

        At the end returns a list of the current seed number as a list
        """
        board = self._game_board
        p1_pits = board[0:6]
        p2_pits = board[7:13]

        # catches if the input pit number is incorrect
        if not 0 <= pit_index <= 6:
            return "Invalid number for pit index"
        # converts p1 and p2 pits to a set to see if all values are 0 to determine of the game has ended
        elif set(p1_pits) == {0} or set(p2_pits) == {0}:
            return "Game is ended"
        # if neither of the upper cases are true, move the seeds
        else:
            if player_index == 1:
                board_index = pit_index - 1
            else:
                board_index = pit_index + 6
            seeds_moving = board[board_index]
            board[board_index] = 0

            p1_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            p2_indexes = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13]
            # for the matching of opposite pits, for use with special rule
            opposite_pits_p1 = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7}
            opposite_pits_p2 = {7: 5, 8: 4, 9: 3, 10: 2, 11: 1, 12: 0}

            if player_index == 1:
                count = 0
                for num in p1_indexes[(board_index + 1):(board_index + seeds_moving + 1)]:
                    board[num] = board[num] + 1
                    count += 1

                    # if last seed goes to p1 store, mention to take another turn
                    if count == seeds_moving and num == 6:
                        print("player 1 take another turn")

                    elif count == seeds_moving and board[num] == 1:
                        # remove the seed and put it in store
                        board[num] = board[num] - 1
                        board[6] += 1

                        # remove opponents seeds and put in your store, and set the opposite to 0
                        board[6] += board[opposite_pits_p1[num]]
                        board[opposite_pits_p1[num]] = 0

                if set(board[0:6]) == {0}:
                    p2_total = sum(board[7:14])
                    board[13] = p2_total
                    for num in range(7, 13):
                        board[num] = 0

            if player_index == 2:
                count = 0
                for num in p2_indexes[(board_index):(board_index + seeds_moving)]:
                    board[num] = board[num] + 1
                    count += 1

                    # if last seed goes to p1 store, mention to take another turn
                    if count == seeds_moving and num == 13:
                        print("player 2 take another turn")

                    elif count == seeds_moving and board[num] == 1:
                        # remove the seed and put it in store
                        board[num] = board[num] - 1
                        board[13] += 1

                        # remove opponents seeds and put in your store, and set the opposite to 0
                        board[13] += board[opposite_pits_p2[num]]
                        board[opposite_pits_p2[num]] = 0

                if set(board[7:12]) == {0}:
                    p1_total = sum(board[0:7])
                    board[6] = p1_total
                    for num in range(0, 6):
                        board[num] = 0

            # return the list of the current seed number at the end
            return board

# game = Mancala()
# player1 = game.create_player("Lily")
# player2 = game.create_player("Lucy")
# print(game.play_game(1, 3))
# print(game.play_game(1, 1))
# print(game.play_game(2, 3))
# print(game.play_game(2, 4))
# print(game.play_game(1, 2))
# print(game.play_game(2, 2))
# print(game.play_game(1, 1))
# game.print_board()
# print(game.return_winner())


class MancalaBoard:
    def __init__(self, master, game):
        self.master = master
        self.master.title("Mancala Board")
        self.master.geometry("750x100")

        # Create the stores (larger buttons)
        self.store1 = tk.Button(self.master, text=str(game.return_num_seeds(6)), font=("Arial", 16), width=8, height=2)
        self.store1.grid(row=1, column=0, rowspan=2)

        self.store2 = tk.Button(self.master, text=str(game.return_num_seeds(13)), font=("Arial", 16), width=8, height=2)
        self.store2.grid(row=1, column=7, rowspan=2)

        # Create Player 1's pits (top section)
        self.pits1 = []
        for i in range(6):
            pit_button = tk.Button(self.master, text=str(game.return_num_seeds(5 - i)), font=("Arial", 14), width=6, height=2, command=lambda i=i: self.play(1, 6 - i))
            pit_button.grid(row=1, column=i + 1)
            self.pits1.append(pit_button)

        # Create Player 2's pits (bottom section)
        self.pits2 = []
        for i in range(7, 13):
            pit_button = tk.Button(self.master, text=str(game.return_num_seeds(i)), font=("Arial", 14), width=6, height=2, command=lambda i=i: self.play(2, i - 6))
            pit_button.grid(row=2, column=i - 6)
            self.pits2.append(pit_button)

    def play(self, player, pit_index):
        print(game.print_board())
        print(player)
        print(pit_index)
        print(game.play_game(player, pit_index))
        for i in range(6):
            self.pits1[i].config(text=str(game.return_num_seeds(5 - i)))
        for i in range(7, 13):
            self.pits2[i-6].config(text=str(game.return_num_seeds(i)))
        
        # Update the stores' values in the GUI
        self.store1.config(text=str(game.return_num_seeds(6)))
        self.store2.config(text=str(game.return_num_seeds(13)))
        

# Set up the tkinter root window
if __name__ == "__main__":
    game = Mancala()
    player1 = game.create_player("Player 1")
    player2 = game.create_player("Player 2")
    root = tk.Tk()
    board = MancalaBoard(root, game)
    root.mainloop()