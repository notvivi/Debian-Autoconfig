# Debian VPS Autoconfiguration
This python script is about autoconfiguring debian virtual private servers via ssh

## Description of terms in UI
- `Password` that is used on all servers
- `Number of threads` is used for time manipulation (More threads = Less time)
- `LOG file` is used for error logging
- `Debian vps file` is used as storage for servers (there is also status about configuration)
- `Run script button` is used for starting script
- `Output` shows final time and errors 

## Requirements
- python 3.10.0 and more
- pyinstaller and paramiko

## How to download pyinstaller and paramiko
1. Open terminal
2. Copy `pip install pyinstaller` and paste it into terminal, press enter
3. Copy `pip install paramiko` and paste it into terminal, press enter
4. Make sure its installed

## How to START
After setting up everything, find exe in `\dist\userinterface.exe`

