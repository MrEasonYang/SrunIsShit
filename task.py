__author__ = 'Eason Yang'

def getPid (name = 'a23aa2f03cf90b7cb868e701825376e5.exe') :
    import win32com.client
    wmi = win32com.client.GetObject('winmgmts:')
    pidList = []
    for p in wmi.InstancesOf('win32_process'):
        if p.Name ==  name:
            pidList.append(p.Properties_('ProcessId'))
    return pidList

def checkProcess (name = 'a23aa2f03cf90b7cb868e701825376e5.exe') :
    import win32com.client
    wmi=win32com.client.GetObject('winmgmts:')
    result = False
    for p in wmi.InstancesOf('win32_process'):
        if p.Name ==  name:
            result =  True
    return result