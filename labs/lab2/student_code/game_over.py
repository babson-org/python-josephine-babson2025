
from calc_score import calc_score
def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    
    # TODO: Check if all cells are filled (abs(cell) == 10)
    
    all_filled = all(abs(cell) == 10 for cell in board)
    if all_filled:
        return True

    # TODO: Use calc_score to check if someone has won

    if calc_score(board) != 0:  # if it equals 30 or -30 means X or O has won
        return True

    # TODO: Return True if game over, otherwise False

    return False
    pass

    


