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
        # Skip device.bat execution
        eel.hideLoader()
        # Temporarily skip face authentication
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Hello, Welcome Sir, How can i Help You")
        eel.hideStart()
        playAssistantSound()
    
    # Use default browser instead of Chrome app mode
    eel.start('index.html', mode='default', host='localhost', port=8000, block=True)