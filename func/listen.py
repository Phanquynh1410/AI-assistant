#listen user -> user letter

import speech_recognition

def listen():
    robot_listen = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        print("Robot: ...")
        audio = robot_listen.listen(mic)

    try:
        # ST robot listen from user
        you = robot_listen.recognize_google(audio)
    except:
        you = ""

    print("You: "+you)
    return you
