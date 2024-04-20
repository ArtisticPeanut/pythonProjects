import PySimpleGUI as sg
import speech_recognition as sr

def main():
    sg.theme('DarkGrey5')

    layout = [
      
        [sg.Text("Say 'Hello' to the AI Assistant")],
        [sg.InputText(key='-OUTPUT-', size=(20, 1))],
        [sg.Button('Listen'), sg.Button('Exit')]
    ]

    window = sg.Window('AI Assistant', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Listen':
            text = listen_for_hello()
            window['-OUTPUT-'].update(text)

    window.close()

def listen_for_hello():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say 'Hello'...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        if 'hello' in text:
            return "Hello, friend!"
        else:
            return "Sorry, I didn't hear 'Hello'."

    except sr.UnknownValueError:
        return "Sorry, I could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    main()
