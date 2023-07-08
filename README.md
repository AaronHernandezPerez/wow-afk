# WOW Afk

A simple python script to prevent AFK in World of Warcraft. It clicks in the middle of the screen and a little below in case you are disconnected from the server. You can start/stop by pressing "s" and exit the program by pressing "esc"

It was made to be able to play during the WOW classic launch, since the queue times were 8 hours+.

To compile it you need to install pynput, pyinstaller and run the following command:

```
pip install pynput pyinstaller

pyinstaller --onefile --icon=icon.ico --name=wow-afk .\main.py
```

The .exe build will appear in the dist folder