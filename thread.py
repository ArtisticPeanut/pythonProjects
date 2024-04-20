import cv2
import speech_recognition as sr
import threading

# Function to play video in a separate thread
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            cv2.imshow('Video Player', frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to recognize voice commands
def listen_and_execute(video_path, audio_path):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if 'play video' in command:
                video_thread = threading.Thread(target=play_video, args=(video_path,))
                video_thread.start()
            elif 'stop video' in command:
                cv2.destroyAllWindows()
            elif 'hello' in command:
                print("JAVIER: Hello! How can I assist you?")
                # Add your response logic here, e.g., engine.say("Hello! How can I assist you?")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Replace 'path/to/your/video.mp4' with the actual path to your video file
    video_path = 'path/to/your/video.mp4'
    # Replace 'C:/Users/HomePC/Desktop/python tutorials/systemaudio.mp3' with the actual path to your audio file
    audio_path = 'C:/Users/HomePC/Desktop/python tutorials/systemaudio.mp3'

    # Start a thread to listen for voice commands
    voice_thread = threading.Thread(target=listen_and_execute, args=(video_path, audio_path))
    voice_thread.start()

    # Main thread plays the video
    play_video(video_path)
