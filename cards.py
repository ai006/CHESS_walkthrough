import pygame
import pygame.freetype

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BACKGROUND_COLOR = (240, 240, 240)  # Light gray background
CARD_COLOR = (255, 255, 255)  # White card background
SHADOW_COLOR = (200, 200, 200)  # Shadow color
TEXT_COLOR = (70, 130, 180)  # Steel Blue (complementary to white)
MAX_FONT_SIZE = 24
MIN_FONT_SIZE = 12
CARD_WIDTH, CARD_HEIGHT = 400, 300
PADDING = 20  # Padding inside the card

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Beautiful Card in Pygame")

# Information to display
venue = "Grand Chess Tour Croatia Rapid & Blitz"
player1 = "White: Kasparov"
rating1 = "Elo: 2801"
vs_text = "VS"
player2 = "Black: Korobov"
rating2 = "Elo: 2668"
event_date = "Date: July 7, 2024"

# Helper function to draw rounded rectangles
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

# Function to dynamically adjust font size so text fits in one line
def get_fitting_font_size(font_name, text, max_width):
    font_size = MAX_FONT_SIZE
    font = pygame.freetype.SysFont(font_name, font_size, bold=True)

    # Reduce the font size until the text fits the card width
    while font.get_rect(text).width > max_width - 2 * PADDING and font_size > MIN_FONT_SIZE:
        font_size -= 1
        font = pygame.freetype.SysFont(font_name, font_size, bold=True)

    return font, font_size

# Function to draw the card with text fitting and alignment
def draw_card_with_shadow(x, y, width, height):
    # Shadow
    shadow_rect = pygame.Rect(x + 5, y + 5, width, height)
    draw_rounded_rect(screen, SHADOW_COLOR, shadow_rect, 20)
    
    # Card
    card_rect = pygame.Rect(x, y, width, height)
    draw_rounded_rect(screen, CARD_COLOR, card_rect, 20)
    
    # Add text inside the card
    current_y = y + PADDING

    # Draw venue at the top
    font, _ = get_fitting_font_size("Georgia", venue, width)
    font.render_to(screen, (x + PADDING, current_y), venue, TEXT_COLOR)
    current_y += font.get_sized_height() + 10  # Adjust vertical spacing

    # Draw player 1 and rating
    font.render_to(screen, (x + width // 2 - font.get_rect(player1).width // 2, current_y), player1, TEXT_COLOR)
    current_y += font.get_sized_height() + 5  # Adjust vertical spacing
    font.render_to(screen, (x + width // 2 - font.get_rect(rating1).width // 2, current_y), rating1, TEXT_COLOR)
    current_y += font.get_sized_height() - 30  # Larger space before VS

    # # Draw VS in the middle
    # font.render_to(screen, (x + width // 2 - font.get_rect(vs_text).width // 2, current_y), vs_text, TEXT_COLOR)
    # current_y += font.get_sized_height() + 20  # Larger space after VS

    # Load the versus image
    vs_image = pygame.image.load("python-chess-ai-yt/assets/images/game_details/three.png")

    # Draw VS in the middle
    vs_image = pygame.transform.scale(vs_image, (vs_image.get_width()*0.35, vs_image.get_height()*0.35))  # Adjust size as needed
    screen.blit(vs_image, (x + width // 2 - vs_image.get_width() // 2, current_y))
    current_y += vs_image.get_height() - 30  # Larger space after VS

    # Draw player 2 and rating
    font.render_to(screen, (x + width // 2 - font.get_rect(player2).width // 2, current_y), player2, TEXT_COLOR)
    current_y += font.get_sized_height() + 5  # Adjust vertical spacing
    font.render_to(screen, (x + width // 2 - font.get_rect(rating2).width // 2, current_y), rating2, TEXT_COLOR)
    current_y += font.get_sized_height() + 20  # Space before date

    # Draw event date at the bottom
    font.render_to(screen, (x + width // 2 - font.get_rect(event_date).width // 2, current_y), event_date, TEXT_COLOR)

# Main loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    
    # Draw the card with the aligned text
    draw_card_with_shadow(100, 50, CARD_WIDTH, CARD_HEIGHT)
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
