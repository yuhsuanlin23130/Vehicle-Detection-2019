# !pip install bs4
from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import PIL.Image
import urllib
page = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03791053")# synset
print(page.content)
# BeautifulSoup is an HTML parsing library
soup = BeautifulSoup(page.content, 'html.parser')#puts the content of the website into the soup variable, each url on a different line

str_soup=str(soup)#convert soup to string so it can be split
type(str_soup)
split_urls=str_soup.split('\r\n')#split so each url is a different possition on a list
print(len(split_urls))#print the length of the list so you know how many urls you have

# !mkdir content\\train\\police_van #create the folder

img_rows, img_cols = 32, 32 #number of rows and columns to convert the images to
input_shape = (img_rows, img_cols, 3)#format to store the images (rows, columns,channels) called channels last
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image

n_of_training_images=len(split_urls)#the number of training images to use
for progress in range(465,n_of_training_images):#store all the images on a directory
    # Print out progress whenever progress is a multiple of 20 so we can follow the
    # (relatively slow) progress
    if(progress%20==0):
        print(progress)
    if not split_urls[progress] == None:
        try:
            I = url_to_image(split_urls[progress])
            if (len(I.shape))==3: #check if the image has width, length and channels
                label = "%06d" % progress
                save_path = 'scooter/img'+label+'.jpg'#create a name of each image
                cv2.imwrite(save_path,I)
        except:
            None

        
#Ambulance: n02701002 #done
#Taxi: n02930766  #done
#Fire truck: n03345487 #done
#Garbage truck: n03417042  #done
#Minibus: n03769881  #done
#Minivan: n03770679   #done
#Motor scooter: n03791053
#Mountain bike: n03792782
#Moving van: n03796401
#Police van: n03977966
#Tow truck: n04461696
#Trailer truck: n04467665
#Compact car: n03079136
