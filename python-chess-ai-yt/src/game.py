import pygame

from const import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square

class Game:

    def __init__(self):
        self.next_player = 'white'
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    # blit methods

    def show_bg(self, surface):
        theme = self.config.theme
        
        for row in range(ROWS):
            for col in range(COLS):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

                # row coordinates
                if col == 0:
                    # color
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(str(ROWS-row), 1, color)
                    lbl_pos = (5, 5 + row * SQSIZE)
                    # blit
                    surface.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    # label
                    lbl = self.config.font.render(Square.get_alphacol(col), 1, color)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    # blit
                    surface.blit(lbl, lbl_pos)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
    
    # function used to show all the possible moves that a chess piece can make
    def show_moves(self, surface):
        theme = self.config.theme

        if self.dragger.dragging:
            piece = self.dragger.piece

            # loop all valid moves
            for move in piece.moves:
                # color
                # color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                color = "#cacbb3"
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                #cirle
                circl = (move.final.col* SQSIZE + 50, move.final.row* SQSIZE + 50)
                # blit
                # pygame.draw.rect(surface, color, rect)
                pygame.draw.circle(surface, color, circl, 15)


    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=3)

    def create_display_text(self, text):

        #Load the font
        font = pygame.font.SysFont('arial', 19)
        text_surface = font.render(text, True, (0, 0, 0))
        # text_surface = font.render(text, True, (220, 220, 220))

        return text_surface

    def show_game_details(self, surface):
        # Define the rectangle
        color = (252, 251, 244)
        rect = (825, 25, 350, 600)
        
        # Draw the rectangle
        pygame.draw.rect(surface, color, rect)
        
        # Load the image
        image = pygame.image.load("../assets/images/game_details/background10.png")
        
        # Calculate the position to center the image in the rectangle
        image_x = rect[0] + (rect[2] - image.get_width()) // 2
        # image_y = rect[1] + (rect[3] - image.get_height()) // 2
        
        # Draw the image
        surface.blit(image, (image_x, 30))

        venue = "Grand Chess Tour Croatia Rapid & Blitz"
        players = "white: Kasparov  vs  black: Korobov"
        rating = "whiteElo: 2801  blackElo: 2668"
        #Load the font
        surface.blit(self.create_display_text(venue), (image_x, image.get_height()+20))
        surface.blit(self.create_display_text(players), (image_x, image.get_height()+40))
        surface.blit(self.create_display_text(rating), (image_x, image.get_height()+60))


    # other methods

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()

    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self):
        self.__init__()