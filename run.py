from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import urllib2, os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
localFileName = '.fileToUploadId'
adressFileName = '.lastKnownAdress'
localIdPath = dir_path +'/'+ localFileName
localAdressPath = dir_path +'/'+ adressFileName
driveFileInformations = {'title': 'CurrentIP'}


def writeNewIP(filename, ip):
    file = open(filename, 'w')
    file.write(ip)
    file.close()

def hasSameIp(filename, ip):
    if os.path.exists(filename):
        localFile = open(filename, 'r')
        lastIp = localFile.read()
        localFile.close()
        if lastIp != ip :
            writeNewIP(filename, ip)
            return False
        else:
            return True
    writeNewIP(filename, ip)
    return False


currentIp = urllib2.urlopen('http://ip.42.pl/raw').read()
print "Current IP : %s" % currentIp

if hasSameIp(localAdressPath, currentIp):
    sys.exit(0)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
print "Auth to Google"

drive = GoogleDrive(gauth)

if os.path.exists(localIdPath):
    localFile = open(localIdPath, 'r')
    driveFileInformations['id'] = localFile.read()
    localFile.close()

fileToUpdate = drive.CreateFile(driveFileInformations)
fileToUpdate.SetContentString(currentIp)
fileToUpdate.Upload()
print "File Uploaded"
if not os.path.exists(localIdPath):
    localFile = open(localIdPath, 'w')
    localFile.write(fileToUpdate['id'])
    localFile.close()
