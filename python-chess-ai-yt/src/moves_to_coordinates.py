
import chess
import chess.pgn

class ChessMoves:
    def __init__(self, file):
        self.moves_made = []
        self.moves_as_mouse_positions = []
        self.moves_made_UCI = []
        self.get_moves(file)
        self.convert_coordinate_to_positions()
    
    def get_moves(self, file):
        pgn = open("../../master_games.pgn")
        game = chess.pgn.read_game(pgn)
        for move in game.mainline_moves():
            self.moves_made_UCI.append(move.uci())
        self.uci_to_numeric()
        
    def uci_to_numeric(self):

        file_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        rank_map = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
        
        for move in self.moves_made_UCI:
            start = move[:2]
            end = move[2:]
            start_numeric = (rank_map[start[1]], file_map[start[0]])
            end_numeric = (rank_map[end[1]], file_map[end[0]])
            self.moves_made.append([start_numeric, end_numeric])
            print(f"uci {[start_numeric, end_numeric]}")
    
    def get_coordinates(self, move):
        start_x = move[0][0]
        start_y = move[0][1]
        dest_x  = move[1][0]
        dest_y  = move[1][1] 
        return start_x, start_y, dest_x, dest_y
    
    def convert_coordinate(self, original):
        x, y = original
        new_x = 100 * x + 50
        new_y = 100 * y + 50
        return (new_x, new_y)

    def convert_coordinate_to_positions(self):
        for pair in self.moves_made:
            converted_pair = [self.convert_coordinate(pair[0]), self.convert_coordinate(pair[1])]
            self.moves_as_mouse_positions.append(converted_pair)

        
# game = ChessMoves("something")
# print(game.moves_made[0])
# print(game.get_coordinates(game.moves_made[0]))