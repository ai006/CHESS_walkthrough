import pygame
import pygame.freetype

class ChessEventCard:
    def __init__(self, card_position, card_size):
        self.x, self.y = card_position
        self.width, self.height = card_size
        self.background_color = (240, 240, 240)  # Light gray background
        self.card_color = (252, 251, 244)  # White card background
        self.shadow_color = (200, 200, 200)  # Shadow color
        self.text_color = (10, 150, 180)  # Steel Blue (complementary to white)
        self.padding = 20  # Padding inside the card
        self.font_name = "Georgia"
        self.max_font_size = 24
        self.min_font_size = 12

        self.found_font_size = False
        self.font_found = None
        self.font_size_found = 0

        self.scaled_image = None

        # Information to display
        self.venue = "Grand Chess Tour Croatia Rapid & Blitz"
        self.player1 = "White: Kasparov"
        self.rating1 = "Elo: 2801"
        self.vs_text = "VS"
        self.player2 = "Black: Korobov"
        self.rating2 = "Elo: 2668"
        self.event_date = "Date: July 7, 2024"
        self.vs_image_path = "../assets/images/game_details/three.png"

    # Helper function to draw rounded rectangles
    def draw_rounded_rect(self, surface, color, rect, corner_radius):
        pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

    # Function to dynamically adjust font size so text fits in one line
    def get_fitting_font_size(self, text, max_width):
        font_size = self.max_font_size
        font = pygame.freetype.SysFont(self.font_name, font_size, bold=True)

        # Reduce the font size until the text fits the card width
        while font.get_rect(text).width > max_width - 2 * self.padding and font_size > self.min_font_size:
            font_size -= 1
            font = pygame.freetype.SysFont(self.font_name, font_size, bold=True)

        return font, font_size

    # Function to draw the card with text fitting and alignment
    def draw(self, surface):

        image = None
        if self.scaled_image == None:                
            # Load the image
            image = pygame.image.load("../assets/images/game_details/background10.png")
            image = pygame.transform.scale(image,(200,300))
            self.scaled_image = image
        else:
            image = self.scaled_image

        # Draw the card with shadow
        shadow_rect = pygame.Rect(self.x + 5, self.y + 5, self.width, self.height)
        self.draw_rounded_rect(surface, self.shadow_color, shadow_rect, 20)
        
        card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw_rounded_rect(surface, self.card_color, card_rect, 20)

        # Add text and image inside the card
        current_y = self.y + self.padding

        # Draw the image at the top with padding
        surface.blit(image, (self.x + self.padding+ 50, current_y))
        current_y += image.get_height() + 10  # Adjust vertical spacing after the image

        font = None
        # Draw venue at the top, after the image
        if self.found_font_size:
            font = self.font_found
        else:
            font, _ = self.get_fitting_font_size(self.venue, self.width)
            self.font_found = font
            self.found_font_size = True

        font.render_to(surface, (self.x + self.padding, current_y), self.venue, self.text_color)
        current_y += font.get_sized_height() + 10  # Adjust vertical spacing

        # Draw player 1 and rating
        font.render_to(surface, (self.x + self.width // 2 - font.get_rect(self.player1).width // 2, current_y), self.player1, self.text_color)
        current_y += font.get_sized_height() + 5  # Adjust vertical spacing
        font.render_to(surface, (self.x + self.width // 2 - font.get_rect(self.rating1).width // 2, current_y), self.rating1, self.text_color)
        current_y += font.get_sized_height() - 30  # Larger space before VS

        # Load and draw VS image
        vs_image = pygame.image.load(self.vs_image_path)
        vs_image = pygame.transform.scale(vs_image, (vs_image.get_width() * 0.35, vs_image.get_height() * 0.35))  # Adjust size as needed
        surface.blit(vs_image, (self.x + self.width // 2 - vs_image.get_width() // 2, current_y))
        current_y += vs_image.get_height() - 30  # Larger space after VS

        # Draw player 2 and rating
        font.render_to(surface, (self.x + self.width // 2 - font.get_rect(self.player2).width // 2, current_y), self.player2, self.text_color)
        current_y += font.get_sized_height() + 5  # Adjust vertical spacing
        font.render_to(surface, (self.x + self.width // 2 - font.get_rect(self.rating2).width // 2, current_y), self.rating2, self.text_color)
        current_y += font.get_sized_height() + 20  # Space before date

        # Draw event date at the bottom
        font.render_to(surface, (self.x + self.width // 2 - font.get_rect(self.event_date).width // 2, current_y), self.event_date, self.text_color)
