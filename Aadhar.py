from pathlib import Path
import re
import cv2 as cv
import keras_ocr
from pathlib import Path


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

def ApplyPatch(aadhar, prediction):
	# To store coordinates where we need to draw the white patches
	rectangle = {
	    1:[],
	    2:[]
	}

	#CreateFolder() # Creating Folder to Store Images


	# Checking over consequtive numbers 
	for i in range(len(prediction[0])):
	    if prediction[0][i][0] == aadhar[0:4]:
	        if prediction[0][i+1][0] == aadhar[5:9]:
	            if prediction[0][i+2][0] == aadhar[10:]:
	                rectangle[1].append((prediction[0][i][1][0::2]))
	                rectangle[2].append((prediction[0][i+1][1][0::2]))
	  

	# Drawing rectangle
	for i in rectangle.keys():
	    for x in rectangle[i]:
	        color_img = cv.rectangle(color_img, tuple(x[0]), tuple(x[1]), color = (255, 255, 255), thickness = -1)

	cv.imshow("image", color_img)
	cv.waitKey(1000)

def OCR(images):

	# Create a pipeline first of all
	pipeline = keras_ocr.pipeline.Pipeline()

	file = open("Aadhar Number.txt", "a")
	for image in images:
		prediction = pipeline.recognize([image])

		values = [x[0] for x in prediction[0]]
		string = " ".join(values)
		aadhar = re.findall(r'[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}', string) # all the aadhar numbers found
		try :

			aadhar = aadhar[0]
			file.write(str(aadhar) + "\n")


			ApplyPatch(aadhar, prediction)

		except :

			pass

		

def ReadAllImages():
	'''This function is to load all the images'''
	images = []
	labels = File_Names()
	for label in labels:
		images.append(cv.imread(label))

	# Converting all images into Grayscale
	images = list(map(lambda x : cv.cvtColor(x, cv.COLOR_BGR2RGB), images))


	OCR(images)
ReadAllImages()

