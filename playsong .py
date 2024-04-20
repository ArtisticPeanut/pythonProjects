import re

def process_request(command):
    # Define patterns for different ways users might request to play a song
    play_patterns = [
        r"play\s+me\s+(?:the\s+)?song\s+(?P<song_name>.+)",
        r"play\s+(?P<song_name>.+)\s+song",
        r"play\s+(?P<song_name>.+)",
        r"play\s+song\s+(?P<song_name>.+)",
    ]

    # Try to match the command with each pattern
    for pattern in play_patterns:
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            song_name = match.group("song_name")
            return song_name.strip()

    # If no match is found, return None
    return None

if __name__ == "__main__":
    # Example usage
    user_command = input("Enter your command: ")

    song_name = process_request(user_command)
    if song_name:
        print(f"User wants to play the song: {song_name}")
        # Call your play_song function with the extracted song_name
    else:
        print("Sorry, I couldn't understand the command.")
