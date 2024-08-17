import pygame
from moves_to_coordinates import ChessMoves

class Mouse_Events:
    
	def __init__(self):
		self.chessMoves = ChessMoves("nothing")
		# Create a list of events to simulate
		self.events = []
		self.create_mouse_events()
          
	def create_mouse_events(self):
		for moves in self.chessMoves.moves_as_mouse_positions:
			print(f"moves {moves}")
			start_x, start_y, dest_x, dest_y = self.chessMoves.get_coordinates(moves)
			print(f"(start_x, start_y) {(start_x, start_y)}")
			self.events.append(pygame.event.Event(pygame.USEREVENT+2, pos=(start_y, start_x), button=1))
			self.events.append(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(start_y, start_x), button=1))
			# self.events.append(pygame.event.Event(pygame.USEREVENT+2, pos=(start_x, start_y), button=1))
			# self.events.append(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(start_x, start_y), button=1))

			# step_size used to calculate what the speed of the movements
			step_size = 1
			# used calculate the rel values
			tmp_x=start_x
			tmp_y=start_y
			# Loop until the start coordinates match the destination coordinates
			while start_x != dest_x or start_y != dest_y:
				if start_x > dest_x:
					start_x -= step_size
				elif start_x < dest_x:
					start_x += step_size

				if start_y > dest_y:
					start_y -= step_size
				elif start_y < dest_y:
					start_y += step_size

				#finding the relative variable
				rel_x=start_x - tmp_x
				rel_y=start_y - tmp_y
				tmp_x=start_x
				tmp_y=start_y

				self.events.append(pygame.event.Event(pygame.MOUSEMOTION, pos=(start_y, start_x), rel=(rel_x, rel_y), buttons=(1, 0, 0)))
				# self.events.append(pygame.event.Event(pygame.MOUSEMOTION, pos=(start_x, start_y), rel=(rel_x, rel_y), buttons=(1, 0, 0)))
			assert start_y == dest_y
			assert start_x == dest_x
			self.events.append(pygame.event.Event(pygame.MOUSEBUTTONUP, pos=(start_y, start_x), button=1))
			# self.events.append(pygame.event.Event(pygame.MOUSEBUTTONUP, pos=(start_x, start_y), button=1))

