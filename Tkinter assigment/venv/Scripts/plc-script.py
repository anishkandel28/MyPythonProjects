#!"C:\Users\dell\PycharmProjects\Tkinter assigment\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pillowcover==1.2.1','console_scripts','plc'
__requires__ = 'pillowcover==1.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pillowcover==1.2.1', 'console_scripts', 'plc')()
    )
