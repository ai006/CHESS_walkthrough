import os

# Initialize the global counter
global_counter = 0  # Starting value for the file count, change as needed.

def process_all_pgn_files(input_folder, output_folder, start_count=0):
    """
    Process all .pgn files in the input folder, split each into individual games,
    and write each game to a separate file in the output folder.
    The filenames use a global counter starting from `start_count`.
    """
    global global_counter  # Declare the counter as global to modify it
    global_counter = start_count  # Set the initial value for the counter

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all .pgn files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pgn'):
            file_path = os.path.join(input_folder, filename)

            # Read the PGN file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Split the content into individual games
            games = content.strip().split("\n\n\n\n\n\n")  # Adjust the delimiter as needed for PGN format

            # Write each game to a separate file
            for game in games:
                global_counter += 1  # Increment the global counter
                game_filename = f'game{global_counter}.pgn'
                game_path = os.path.join(output_folder, game_filename)
                with open(game_path, 'w', encoding='utf-8') as game_file:
                    game_file.write(game)

            print(f'Processed {len(games)} games from {file_path}.')

    print(f'All files processed. Global counter is now at {global_counter}.')

# Example usage:
# Specify input folder, output folder, and starting counter
input_folder = '.'
output_folder = 'games'
starting_count = 1  # Start counting from 100
process_all_pgn_files(input_folder, output_folder, starting_count)
