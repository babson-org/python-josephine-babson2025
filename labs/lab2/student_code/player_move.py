    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # TODO: Convert input to integer
            move = int(input(prompt))
            # TODO: Validate move is in range and not taken
            if move < 1 or move > 9:
                prompt = "Number must be 1-9. Try again: "
                continue
            if abs(board[move - 1]) == 10:
                prompt = "Cell already taken. Choose another: "
                continue
            break
            pass
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
            
    # TODO: Assign score['player'] to the selected cell on the board
    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8

    board[move - 1] = score['player']
pass
