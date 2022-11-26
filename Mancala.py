class Player:
    """A class to represent the player, including their name"""

    def __init__(self, name):
        """Initializes the player and assigns a name attribute"""
        self._name = name


class Mancala:
    """A class to represent the game, including the game board, and players."""

    def __init__(self, name):
        """Constructor for the Mancala class.Initializes the required data members.All data members are private"""
        pass

    def create_player(self, player_name):
        """takes one parameter of the player’s name as a string and returns the player object. """
        pass

    def print_board(self):
        """Prints the game board in the following format(taking no parameters):
        player1:

        store: number
        of
        seeds in player
        1’s
        store

        player
        1
        seeds
        number
        from pit
        1
        to
        6 in a
        list

        player2:

        store: number
        of
        seeds in player
        2’s
        store

        player
        2
        seeds
        number
        from pit
        1
        to
        6 in a
        list
        """
        pass

    def return_winner(self):
        """If the game is over, returns the winner in the following format:

        Winner is player
        1( or 2, based
        on
        the
        actual
        winner): player’s
        name, if the game is a tie return ‘It’s a tie’, if the game is ongoing returns ‘Game has not ended’"""
        pass

    def play_game(self, player_index, pit_index):
        """
        Takes in two parameters: the player index(1 or 2) and the pit index(1 - 6), both as integers.This class follows
        the rules of the game (including the special rules) and changes the number of seeds in the pits and player
        stores following the move.

        If
        an
        invalid
        pit
        number is given,
        return "Invalid number for pit index"

        If
        the
        game is ended
        at
        this
        point,
        return "Game is ended"

        If
        the
        player
        1
        win
        an
        extra
        round
        following
        the
        special
        rule
        1, print
        out “player
        1
        take
        another
        turn
        "

        At
        the
        end, the
        method
        should
        return a
        list
        of
        the
        current
        seed
        number in this
        format:
        [player1 pit1, player1 pit2, player1 pit3, player1 pit4, player1 pit5, player1 pit6, player1 store, Player2
         pit1, player2 pit2, player2 pit3, player2 pit4, player2 pit5, player2 pit6, player2 store, ]

        """

        pass



