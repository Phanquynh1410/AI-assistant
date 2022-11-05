#robot brain -> say ST

import pyttsx3

def say(robot_brain):
    robot_say = pyttsx3.init()
    robot_say.say(robot_brain)
    robot_say.runAndWait()