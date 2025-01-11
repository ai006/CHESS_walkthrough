import os
import shutil

def move_files_to_passed(input_paths):
    # Create the PASSED directory if it doesn't exist
    passed_dir = 'PASSED'
    if not os.path.exists(passed_dir):
        os.makedirs(passed_dir)
    
    for path in input_paths:
        # Ensure the path is valid
        if os.path.exists(path):
            # Extract the file name from the path
            file_name = os.path.basename(path)
            # Create the destination path for the file in the PASSED directory
            dest_path = os.path.join(passed_dir, file_name)
            # Move the file to the PASSED directory
            shutil.move(path, dest_path)
            print(f"Moved {file_name} to {passed_dir}")
        else:
            print(f"File {path} does not exist")

# Example input paths
input_paths = [
"games/game554.pgn",
"games/game39.pgn",
"games/game390.pgn",
"games/game391.pgn",
"games/game392.pgn",
"games/game393.pgn",
"games/game394.pgn",
"games/game395.pgn",
"games/game396.pgn",
"games/game397.pgn",
"games/game398.pgn",
"games/game399.pgn",
"games/game4.pgn",
"games/game40.pgn",
"games/game400.pgn",
"games/game401.pgn",
"games/game402.pgn",
"games/game403.pgn",
"games/game404.pgn",
"games/game405.pgn",
"games/game406.pgn",
"games/game407.pgn",
"games/game408.pgn",
"games/game409.pgn",
"games/game41.pgn",
"games/game410.pgn",
"games/game411.pgn",
"games/game412.pgn",
"games/game413.pgn",
"games/game414.pgn",
"games/game415.pgn",
"games/game416.pgn",
"games/game417.pgn",
"games/game418.pgn",
"games/game419.pgn",
"games/game42.pgn",
"games/game420.pgn",
"games/game421.pgn",
"games/game422.pgn",
"games/game423.pgn",
"games/game424.pgn",
"games/game425.pgn",
"games/game426.pgn"
]

# Call the function to move files
move_files_to_passed(input_paths)


