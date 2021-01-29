from pyautogui import press, typewrite, hotkey
import traceback
from statistics import mode
import time

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
		mostCommon = mode(newData)
		typewrite(mostCommon + '\n')
		return mostCommon

	except:
		traceback.print_exc()


if __name__ == "__main__":
	filename="C:/Users/Benjamin/Documents/Zoom/2021-01-22 15.20.24 ME 3034_ Writing as a Mechanical Engineer 94482445948/meeting_saved_chat.txt"
	time.sleep(5)
	while True:
		print('Typewriter wrote : ' + main(filename, 100))
		time.sleep(30)

else:
	pass