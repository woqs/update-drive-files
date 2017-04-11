from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import urllib2, os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
localFileName = '.fileToUploadId'
adressFileName = '.lastKnownAdress'
localIdPath = dir_path +'/'+ localFileName
localAdressPath = dir_path +'/'+ adressFileName
driveFileInformations = {'title': 'CurrentIP'}

def hasSameIp(filename, ip):
    if os.path.exists(filename):
        localFile = open(filename, 'r')
        lastIp = localFile.read()
        localFile.close()
        if lastIp != ip :
            localFile = open(filename, 'w')
            localFile.write(ip)
            localFile.close()
            return False
        else:
            return True
    localFile = open(filename, 'w')
    localFile.write(ip)
    localFile.close()
    return False



currentIp = urllib2.urlopen('http://ip.42.pl/raw').read()

if hasSameIp(localAdressPath, currentIp):
    sys.exit(0)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

if os.path.exists(localIdPath):
    localFile = open(localIdPath, 'r')
    driveFileInformations['id'] = localFile.read()
    localFile.close()

fileToUpdate = drive.CreateFile(driveFileInformations)
fileToUpdate.SetContentString(currentIp)
fileToUpdate.Upload()

if not os.path.exists(localIdPath):
    localFile = open(localIdPath, 'w')
    localFile.write(fileToUpdate['id'])
    localFile.close()
