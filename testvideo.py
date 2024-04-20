import vlc
import pygame
import threading

# Function to play video in full-screen mode
def play_video(video_path):
    instance = vlc.Instance('--no-xlib')  # Use --no-xlib to avoid conflicts with pygame
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    media.get_mrl()
    player.set_media(media)

    player.set_fullscreen(True)
    player.play()

    while True:
        pass

# Function to play audio
def play_audio(audio_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Main function
def main():
    # Replace 'path/to/your/video.mp4' and 'path/to/your/audio.mp3' with the actual paths
    video_path = 'C:/Users/HomePC/Desktop/python tutorials/system_project.mp4'
    audio_path = 'C:/Users/HomePC/Desktop/python tutorials/systemaudio.mp3'

    # Start a thread to play video
    video_thread = threading.Thread(target=play_video, args=(video_path,))
    video_thread.start()

    # Play audio in the main thread
    play_audio(audio_path)

if __name__ == "__main__":
    main()
