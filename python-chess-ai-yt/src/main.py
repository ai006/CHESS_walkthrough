import pygame
import sys
import os

from const import *
from game import Game
from square import Square
from move import Move
from debug import debug, debugPiece, debugPieceCoord
from mouse_events import Mouse_Events
import time

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH+400, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.mouse_events = Mouse_Events("nothing")
        
        # pass the game details
        self.game.cardDetails.update_game_details(self.mouse_events.chessMoves.game_data)

        #create a custom event that will be used to create other events
        self.POST_EVENT_TIMER = pygame.USEREVENT + 1
        self.POSITION_MOUSE = pygame.USEREVENT + 2
        self.pgn_games = []
        self.getAllGamePaths()

    # read all the games paths
    def getAllGamePaths(self):
        # Iterate over all .pgn files in the input folder
        for filename in os.listdir('../../games/games'):
            if filename.endswith('.pgn'):
                file_path = os.path.join('../../games/games', filename)
                self.pgn_games.append(file_path)
        self.pgn_games.sort()

    def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        tmp_str = "hello"
        tmp_piece = ""
        tmp_xy = ""
        pygame.time.set_timer(self.POST_EVENT_TIMER, 15)
        while True:
            # show methods
            game.show_game_details(screen)
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)
            debug(tmp_str)
            debugPiece(tmp_piece)
            debugPieceCoord(tmp_xy)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                # click
                # MOUSEBUTTONDOWN is only a single action meaning this if statement is only 
                # entered on a click
                if event.type == pygame.MOUSEBUTTONDOWN:                
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    # clicked_row = start_x
                    # clicked_col = start_y
                    tmp_str = str(clicked_row) + " " + str(clicked_col)
                    # print(event)
                    

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # print(piece)
                        # valid piece (color) ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    tmp_piece = str(event.pos[1]) + " " + str(event.pos[0])
                    tmp_xy = str(motion_row) + " " + str(motion_col)
                    
                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                        # debug(tmp_str)
                        # debugPiece(tmp_piece)
                        # debugPieceCoord(tmp_xy)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    # print(event)
                    # if dragger.dragging:
                    if True:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE
                        # released_row = dest_x
                        # released_col = dest_y

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)                            

                            # sounds
                            game.play_sound(captured)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            # next turn
                            game.next_turn()
                            # debug(tmp_str)
                            # debugPiece(tmp_piece)
                            # debugPieceCoord(tmp_xy)
                    
                    dragger.undrag_piece()
                
                # key press
                elif event.type == pygame.KEYDOWN:
                    
                    # changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                     # changing themes
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                # create the chess move events
                elif event.type == pygame.USEREVENT + 1:
                    if(len(self.mouse_events.events) > 1):
                        pygame.event.post(self.mouse_events.events[0])
                        self.mouse_events.events.pop(0)
                    elif len(self.mouse_events.events) == 1 :
                        pygame.event.post(self.mouse_events.events[0])
                        self.mouse_events.events.pop(0)
                        pygame.time.set_timer(self.POST_EVENT_TIMER, 0)
                        pygame.time.set_timer(self.POST_EVENT_TIMER, 10000)
                    else:
                        if game.gameOver == True:
                            # print("RESET GAME")
                            game.reset()
                            game = self.game
                            game.change_theme()
                            board = self.game.board
                            dragger = self.game.dragger
                            game.gameOver = False
                            self.mouse_events.reset(self.pgn_games.pop(0))
                             # pass the game details
                            self.game.cardDetails.update_game_details(self.mouse_events.chessMoves.game_data)
                            pygame.time.set_timer(self.POST_EVENT_TIMER, 15)
                
                #Reposition mouse before move events
                elif event.type == pygame.USEREVENT + 2:
                    pygame.mouse.set_pos(event.pos)
                # get the event which will show the winners
                elif event.type == pygame.USEREVENT + 3:
                    # print("GETTING GAME OUTCOME")
                    game.gameOutcome = event.game_outcome
                    game.gameOver = True


            pygame.display.update()


main = Main()
main.mainloop()