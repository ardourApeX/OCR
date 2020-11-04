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


def OCR(images):

	# Create a pipeline first of all
	pipeline = keras_ocr.pipeline.Pipeline()

	for image in images:
		prediction = pipeline.recognize([image])

		values = [x[0] for x in prediction[0]]
		string = " ".join(values)
		aadhar = re.findall(r'[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}', string) # all the aadhar numbers found
		try :

			aadhar = aadhar[0]
		except :
			aadhar = "Not Found"

		print(aadhar)

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