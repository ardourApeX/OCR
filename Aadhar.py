from pathlib import Path
import re
import cv2 as cv
import keras_ocr



def File_Names(path = "./images"):
	'''This function is to store the path of all images preset in the directed path'''

	labels = [] #Store PATH

	p = Path(path)
	dirs = p.glob("*") 
 
	for file in dirs:
		labels.append(str(file)) #Store path of each image

	return labels


def CreateFolder():
	path = os.path.join("Converted Images")
	
	try: 
		#Try to create folder if its is not already there
		os.makedirs(path, exist_ok = True)

	except:
		# If folder is there, pass then
		pass
