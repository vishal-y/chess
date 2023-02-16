def chess_notation_to_row_col(chess_notation):
    """
    Convert chess notation in the format of 'e2e4' to row and column numbers.
    Returns a tuple of integers in the format (start_row, start_col, end_row, end_col).
    """
    column_dict = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }
    start_col = column_dict[chess_notation[0]]
    start_row = int(chess_notation[1]) - 1
    end_col = column_dict[chess_notation[2]]
    end_row = int(chess_notation[3]) - 1
    return (start_row, start_col, end_row, end_col)

move = input("enter your move : ")
start_row, start_col, end_row, end_col = chess_notation_to_row_col(move)
print("Notation in algebric format : ")
print(start_row + 1, start_col + 1)  # Output: 2, 5
print(end_row + 1, end_col + 1)  # Output: 4, 5
