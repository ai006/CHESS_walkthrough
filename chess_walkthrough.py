import chess.pgn
import pygame

def piece_to_image(piece):
  """Converts a chess piece to its corresponding image file path."""
  piece_color = "white" if piece.color else "black"
  piece_type = str(piece.piece_type).lower()
  return f"{piece_color}_{piece_type}.png"

def draw_board(board, screen):
  """Draws the chess board and pieces onto the Pygame screen.

  Args:
    board: A chess.Board object representing the current board state.
    screen: A Pygame Surface object representing the display surface.
  """
  square_size = 80  # Adjust this for desired board size
  for rank in range(8):
    for file in range(8):
      square_color = (210, 180, 140) if (rank + file) % 2 else (139, 69, 19)
      pygame.draw.rect(screen, square_color,
                       pygame.Rect(file * square_size, rank * square_size, square_size, square_size))
      piece = board.piece_at(chess.square(rank, file))
      if piece:
        image_path = piece_to_image(piece)
        piece_image = pygame.image.load(image_path)
        screen.blit(piece_image, (file * square_size, rank * square_size))

def process_pgn_game(game, screen):
  """Processes a chess game from a PGN object and displays moves on the Pygame screen.

  Args:
    game: A chess.pgn.Game object representing the chess game.
    screen: A Pygame Surface object representing the display surface.
  """

  # Extract game details (excluding moves)
  game_details = {
      "Event": game.headers["Event"],
      "White": game.headers["White"],
      "Black": game.headers["Black"],
      "Result": game.headers["Result"],
      # ... Include other desired details
  }

  print("Game Details:")
  for key, value in game_details.items():
    print(f"\t{key}: {value}")

  board = chess.Board()
  draw_board(board, screen)
  pygame.display.flip()

  clock = pygame.time.Clock()
  for move in game.mainline_moves():
    print(f"Move: {move}")

    # Simulate a delay for move animation (adjust delay as needed)
    pygame.time.delay(500)

    board.push(move)
    draw_board(board, screen)
    pygame.display.flip()

    # Handle user input (e.g., pause, next move, etc.)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

if __name__ == "__main__":
  pygame.init()
  screen_size = 640  # Adjust this for desired display size
  screen = pygame.display.set_mode((screen_size, screen_size))
  pygame.display.set_caption("Chess Game Visualization")

  with open("master_games.pgn", "r") as f:
    game = chess.pgn.read_game(f)
    process_pgn_game(game, screen)

  pygame.quit()
