from pyautogui import press, typewrite, hotkey, moveTo, size, position, click
import traceback
from statistics import mode
import time
from datetime import date
from collections import Counter
import os

numLines = 100
delay = 30

X_FACTOR = 1877 / 1920
Y_FACTOR = 980 / 1080

'''
EDIT THE VARIABLES IMMEDIATELY ABOVE

DEFAULTS:
numLines = 100
delay = 30

'''

def main(pathToTxt, nWords):
	try:
		# get all texts
		f = open(pathToTxt, "r")
		data = f.readlines()
		newData = []
		for line in data[-nWords:]:
			try:
				newData.append(line[-line[::-1].index(':')+1:-1])
			except ValueError:
				continue
		# find average word of last n words
		mostCommon = '' # print nothing if broken
		try:
			common = Counter(newData).most_common()
			mostCommon = common[0][0]
		except:
			mostcommon = newData[0]
		typewrite(mostCommon + '\n')
		return mostCommon

	except:
		traceback.print_exc()


def saveZoomChat(zoomPath, ID):
	# requires zoom window be selected, chat window maximized, and cursor in 'chat' section
	# hotkey('alt', 'h') # get chat window
	hotkey('shift', 'tab') # get more icon in chat ? think this works
	press('enter')
	(screenWidth, screenHeight) = size()
	moveTo(int(screenWidth * X_FACTOR), int(screenHeight * Y_FACTOR))
	click()
	hotkey('tab')
	press('enter')
	# at this point, the chat has been saved.
	# should be saved to zoomPath/******* ID/meeting_saved_chat.txt
	try:
		subdirs = os.listdir(zoomPath)
	except FileNotFoundError:
		print("Incorrect Path to Zoom directory entered. Please enter again : ")
		semimain()
	today = date.today().strftime("%Y/%m/%d").replace('/','-')
	desiredMeeting = [meeting for meeting in subdirs if meeting.startswith(today) and meeting.endswith(str(ID))]
	if len(desiredMeeting) == 0:
		raise FileNotFoundError("Desired Meeting directory not found")
	elif len(desiredMeeting) > 1:
		raise FileNotFoundError("Multiple Meetings found")
	else:
		return zoomPath + '/' + desiredMeeting[0] + "/meeting_saved_chat.txt"

def semimain():
	zoomPath = 0
	zoomMeetingID = ''
	while type(zoomPath) != str:
		zoomPath = input("Enter zoom meeting document path (eg C:/Users/Benjamin/Documents/Zoom/): ")
	while type(zoomMeetingID) != int:
		try:
			zoomMeetingID = int(input("Enter zoom meeting ID (should be 10 digit number, eg 92295112497) : "))
			if len(str(zoomMeetingID)) != 10:
				raise ValueError("Incorrect length")
		except ValueError:
			print("Please enter a 10 digit integer")
	print("Navigate to chat window, fullscreen on primary monitor, and place your cursor in the chat box")
	time.sleep(5)
	while True:
		pathToFile = saveZoomChat(zoomPath, zoomMeetingID)
		print('Typewriter wrote : ' + main(pathToFile, numLines))
		time.sleep(delay)


if __name__ == "__main__":
	semimain()

else:
	pass
