__author__ = 'Eason Yang'

def testNetwork (url) :
    import urllib2
    import socket
    try:
        response=urllib2.urlopen(url,timeout=3)
        return True
    except urllib2.URLError as e:
        return False
    except socket.error as e:
        return False