import pygame
import os
from random import shuffle
import mutagen

class Sound:
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)


class SoundManager:
    def __init__(self):
        # Initialize the mixer with specific settings
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        
        # Set up different channels
        pygame.mixer.set_num_channels(8)  # Allocate channels for simultaneous sounds
        self.music_channel = pygame.mixer.Channel(0)  # Reserved for background music
        self.effects_channel = pygame.mixer.Channel(1)  # Reserved for game effects
        
        self.music_list = []
        self.music_info = {}  # Dictionary to store metadata for each song
        self.current_music_index = 0
        self.music_volume = 0.05  # 30% volume for background music
        self.effects_volume = 1.0  # 100% volume for effects
        
        # Set up music end event
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 4)
    
    def load_music_directory(self, directory_path):
        """Load all music files from a directory"""
        supported_formats = ('.mp3', '.wav', '.ogg')
        self.music_list = [
            os.path.join(directory_path, f) 
            for f in os.listdir(directory_path) 
            if f.lower().endswith(supported_formats)
        ]
        shuffle(self.music_list)  # Randomize playlist order
        
        # Extract metadata for each song
        for song_path in self.music_list:
            self.extract_metadata(song_path)
            
        if self.music_list:
            self.start_playlist()

    def extract_metadata(self, song_path):
        """Extract song title and artist metadata from an audio file"""
        try:
            audio = mutagen.File(song_path)
            
            # Initialize with defaults
            title = os.path.basename(song_path)
            artist = "Unknown Artist"
            
            # Extract metadata based on file type
            if audio:
                # For MP3 files
                if hasattr(audio, 'tags') and audio.tags:
                    if 'TIT2' in audio.tags:  # Title tag
                        title = str(audio.tags['TIT2'])
                    if 'TPE1' in audio.tags:  # Artist tag
                        artist = str(audio.tags['TPE1'])
                
                # For FLAC, OGG, etc.
                elif hasattr(audio, 'get'):
                    if audio.get('title'):
                        title = audio.get('title')[0]
                    if audio.get('artist'):
                        artist = audio.get('artist')[0]
            
            self.music_info[song_path] = {
                'title': title,
                'artist': artist
            }
            
        except Exception as e:
            print(f"Error extracting metadata from {song_path}: {e}")
            # Use filename as fallback
            self.music_info[song_path] = {
                'title': os.path.basename(song_path),
                'artist': "Unknown Artist"
            }
    
    def get_current_song_info(self):
        """Return information about the currently playing song"""
        if not self.music_list:
            return {"title": "No song playing", "artist": ""}
            
        current_song = self.music_list[self.current_music_index]
        return self.music_info.get(current_song, {"title": os.path.basename(current_song), "artist": "Unknown Artist"})

    
    def start_playlist(self):
        """Start playing the first song in the playlist"""
        if self.music_list:
            pygame.mixer.music.load(self.music_list[0])
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play()
            
            # You can print or use the current song info
            song_info = self.get_current_song_info()
            print(f"Now playing: {song_info['title']} by {song_info['artist']}")
    
    def play_next_song(self):
        """Play the next song in the playlist"""
        if not self.music_list:
            return
            
        self.current_music_index = (self.current_music_index + 1) % len(self.music_list)
        current_song = self.music_list[self.current_music_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        
        # You can print or use the current song info
        song_info = self.get_current_song_info()
        print(f"Now playing: {song_info['title']} by {song_info['artist']}")
    
    def handle_music_end(self):
        """Handle the music end event by playing the next song"""
        self.play_next_song()
    
    def play_effect(self, sound):
        """Play a sound effect"""
        sound.sound.set_volume(self.effects_volume)
        self.effects_channel.play(sound.sound)
    
    def stop_music(self):
        """Stop the background music"""
        pygame.mixer.music.stop()
    
    def pause_music(self):
        """Pause the background music"""
        pygame.mixer.music.pause()
    
    def unpause_music(self):
        """Unpause the background music"""
        pygame.mixer.music.unpause()
    
    def set_music_volume(self, volume):
        """Set background music volume (0.0 to 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)
    
    def set_effects_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)"""
        self.effects_volume = max(0.0, min(1.0, volume))