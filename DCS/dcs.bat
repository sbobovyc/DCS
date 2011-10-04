    set PIP=C:\Python27\pyinstaller-1.5.1\
    python %PIP%pyinstaller.py --onefile --noconsole --icon src\dcs.ico --name DCS -p src\ src\gui\main.py
    copy src\dcs.ico dist\
    copy src\utils\build\libutils.dll dist\

