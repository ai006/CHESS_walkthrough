def algebraic_to_coordinates(square):
    file_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    rank_map = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    
    if len(square) == 2:
        file, rank = square
        return (rank_map[rank], file_map[file])
    return None

def initialize_board():
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def find_piece(board, piece, end_coords, start_file=None, start_rank=None):
    for r in range(8):
        for c in range(8):
            if board[r][c] == piece:
                if start_file is not None and c != start_file:
                    continue
                if start_rank is not None and r != start_rank:
                    continue
                if (r, c) != end_coords:
                    return r, c
    return None

def convert_moves(moves):
    board = initialize_board()
    coordinates = []
    
    piece_symbols = {
        'K': 'k', 'Q': 'q', 'R': 'r', 'B': 'b', 'N': 'n',
        'k': 'K', 'q': 'Q', 'r': 'R', 'b': 'B', 'n': 'N'
    }
    file_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    rank_map = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    for move in moves:
        start = end = None
        is_capture = 'x' in move

        if move == "O-O":  # kingside castling
            if len(coordinates) % 2 == 0:  # white to move
                start, end = (7, 4), (7, 6)  # e1 to g1
                board[7][4], board[7][6] = '.', 'K'
                board[7][7], board[7][5] = '.', 'R'
            else:  # black to move
                start, end = (0, 4), (0, 6)  # e8 to g8
                board[0][4], board[0][6] = '.', 'k'
                board[0][7], board[0][5] = '.', 'r'
        elif move == "O-O-O":  # queenside castling
            if len(coordinates) % 2 == 0:  # white to move
                start, end = (7, 4), (7, 2)  # e1 to c1
                board[7][4], board[7][2] = '.', 'K'
                board[7][0], board[7][3] = '.', 'R'
            else:  # black to move
                start, end = (0, 4), (0, 2)  # e8 to c8
                board[0][4], board[0][2] = '.', 'k'
                board[0][0], board[0][3] = '.', 'r'
        else:
            move = move.replace('+', '').replace('#', '')
            
            if '=' in move:
                move = move.split('=')[0]

            if len(move) == 2:  # pawn move like e4
                end = move
                piece = 'P' if len(coordinates) % 2 == 0 else 'p'
                end_coords = algebraic_to_coordinates(end)
                start_coords = find_piece(board, piece, end_coords)
            elif len(move) == 3:  # piece move like Nf3
                piece, end = move[0], move[1:]
                piece = piece_symbols[piece] if len(coordinates) % 2 == 0 else piece.lower()
                end_coords = algebraic_to_coordinates(end)
                start_coords = find_piece(board, piece, end_coords)
            elif len(move) == 4:  # disambiguating move like Nbd7 or e2e4
                if move[1].islower():  # Nbd7
                    piece, start_file, end = move[0], move[1], move[2:]
                    piece = piece_symbols[piece] if len(coordinates) % 2 == 0 else piece.lower()
                    end_coords = algebraic_to_coordinates(end)
                    start_coords = find_piece(board, piece, end_coords, file_map[start_file])
                else:  # e2e4
                    start, end = move[:2], move[2:]
                    start_coords = algebraic_to_coordinates(start)
                    end_coords = algebraic_to_coordinates(end)
                    piece = board[start_coords[0]][start_coords[1]]
            elif len(move) == 5:  # pawn capture like cxd5
                start_file, end = move[0], move[2:]
                piece = 'P' if len(coordinates) % 2 == 0 else 'p'
                end_coords = algebraic_to_coordinates(end)
                start_coords = find_piece(board, piece, end_coords, file_map[start_file])
            
            if start_coords is None:
                raise ValueError(f"Could not find piece for move: {move}")

            coordinates.append((start_coords, end_coords))
            board[end_coords[0]][end_coords[1]] = piece
            board[start_coords[0]][start_coords[1]] = '.'

    return coordinates

moves = ["c4", "e6", "d4", "d5", "Nf3", "Nf6", "e3", "Be7", "Bd3", "O-O", "b3", "b6", "O-O", "Bb7", "Bb2", 
         "Nc3", "a6", "Rc1", "Bd6",  "Ne2", "Re8", "Ng3", "Ne4", "Qc2",  "Nf6", "Ne5", 
         "Qe7", "b4", "Ne4", "b5",  "Rec8", "Nc6", "Qg5", "a4", "h5", "Qe2", "h4", 
         "g3", "Qg5", "Rc2", "Re8", "Kg2", "Re6"]

coordinates = convert_moves(moves)
for move, coord in zip(moves, coordinates):
    print(f"Move: {move}, Coordinates: {coord}")
