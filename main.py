import os
import eel
import subprocess

from engine.features import *
from engine.command import *
from engine.auth import recoganize
def start():
    
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        # Temporarily skip face authentication
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Hello, Welcome Sir, How can i Help You")
        eel.hideStart()
        playAssistantSound()
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)