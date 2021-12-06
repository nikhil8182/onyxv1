from main import *
from main import say


def turnOffAdminRoomLights():
    requests.get('http://o.j:8000/Tube_Light_1_Button_Admin_Room/0')


def turnOffAllLights():
    print('all lights will be off')


def turnOnAllLights():
    print('all lights will be on')


def turnOnAdminRoomLights():
    requests.get('http://o.j:8000/Tube_Light_1_Button_Admin_Room/1')

    say('do you need to turn off all lights')
def ASkWhichRoomlightoff():
    print('ask which room function should be offed?????????????????????')
    say('do you need to off all lights')
    _x = takeVoiceInputFromUser()
    if _x == 'yes':
        turnOffAllLights()
    elif _x == 'no':
        say('which room lights should be offed')
        _room = takeVoiceInputFromUser()
        if _room in rooms:
            {}
        else:
            say('sorry the room is invalid')
    else:
        say('plese say yes or no')
        ASkWhichRoomlightoff()

    # turnOffAdminRoomLights()