from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import urllib2
import os 

localFileName = '.fileToUploadId'
driveFileInformations = {'title': 'CurrentIP'}
dir_path = os.path.dirname(os.path.realpath(__file__))
localFilePath = dir_path + '/' + localFileName

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

if os.path.exists(localFilePath):
    localFile = open(localFilePath, 'r')
    driveFileInformations['id'] = localFile.read()
    localFile.close()

fileToUpdate = drive.CreateFile(driveFileInformations)
fileToUpdate.SetContentString(urllib2.urlopen('http://ip.42.pl/raw').read())
fileToUpdate.Upload()

if not os.path.exists(localFilePath):
    localFile = open(localFilePath, 'w')
    driveFileInformations['id'] = localFile.write(fileToUpdate['id'])
    localFile.close()
