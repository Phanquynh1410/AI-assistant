#ST in letter -> reply by letter. The brain of robot
from datetime import date, datetime

def understand(you):

    if "hello" in you:
        robot_brain = "Hello you"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S secounds")
    else:
        robot_brain = "I can't hear you. Repeat"

    print("Robot: " +robot_brain)
    return robot_brain

