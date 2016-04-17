__author__ = 'Eason Yang'

def restart () :
    import win32api
    from time import sleep
    win32api.ShellExecute(0, 'open', 'D:\iSoft\software\HEUApartment.exe', '','',0)
    sleep(60)