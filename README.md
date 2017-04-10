# Update Drive Files

This project's goal is to be able to modify a file on your google drive

## Installation

First [install PyDrive](https://pypi.python.org/pypi/PyDrive).

Follow this explanation to create your google credentials [here](https://support.google.com/googleapi/answer/6158849).

Then :
* Download the json file containing the credentials. 
Take the *client_id* and *client_secret* values, and replace the default values assigned in **settings.ymal**
* Enable the Drive API in your [developer console](https://console.developers.google.com/apis/library?project=update-ip).

## Usage

run `python run.py`

It will, in this example, get your public IP, and save it in a file named "CurrentIP". 
It will then save the document id in a hidden file named ".fileToUploadId", so that it only update the same file in your 
drive, and not create one every time the scipt is launched.
