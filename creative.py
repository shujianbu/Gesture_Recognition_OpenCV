'''
    Creative Part
'''

import os
import sys
import cv
import numpy
import getpass
import imgproc, skin, gesture
from player1 import Rule_Player1
from player2 import Rule_Player2

''' ImageProcessSession Class and Its Functions'''

class ImageProcessSession(object):

  def __init__(self, skin_detector):
    self.skin_detector = skin_detector

  def process(self, bgrimg):
    img = self.skin_detector.detectSkin(bgrimg) # Call the function in skin.py
    contours = imgproc.find_contours(img)
    return contours

''' Functions For Images Input'''

def get_input_pics(number): 
	im1 = cv.LoadImage('2_setting/' + str(number) + '/1.png')
	im2 = cv.LoadImage('2_setting/' + str(number) + '/2.png')
	im3 = cv.LoadImage('2_setting/' + str(number) + '/3.png')

	if (im1 is None) or (im2 is None) or (im3 is None): 
		print 'The input images can not be recognized! Please restore your images!' 
	
  	if (im1 is not None) and (im2 is not None) and (im3 is not None): 
  		initHueThreshold = 42
    	initIntensityThreshold = 170
    	skin_detector = skin.SkinDetector()
    	skin_detector.setHueThreshold(initHueThreshold)
    	skin_detector.setIntensityThreshold(initIntensityThreshold)

    	session = ImageProcessSession(skin_detector)
    	ga = gesture.GestureAnalyzer()

    	cv.Flip(im1, None, 1)
        contours1 = session.process(im1)
        img1 = cv.CreateImage((im1.width, im1.height), 8, 3)
        if contours1:
        	ges1, area1, depth1 = ga.recognize(contours1)
        	# print ges1
        else: 
        	ges1 = None

    	cv.Flip(im2, None, 1)
        contours2 = session.process(im2)
        img2 = cv.CreateImage((im2.width, im2.height), 8, 3)
        if contours2:
        	ges2, area2, depth2 = ga.recognize(contours2)
        	# print ges2
        else: 
        	ges2 = None			        	

    	cv.Flip(im3, None, 1)
        contours3 = session.process(im3)
        img3 = cv.CreateImage((im3.width, im3.height), 8, 3)
        if contours3:
        	ges3, area3, depth3 = ga.recognize(contours3)
        	# print ges3
        else: 
        	ges3 = None		

	return ges1, ges2, ges3

	# cv.ShowImage('show1', gesture_palm) 
	# cv.ShowImage('show2', gesture_scissors)      
	# cv.ShowImage('show3', gesture_fist)      
	# cv.WaitKey(0)

''' Main Functions in this System '''

def mainFunction():
  ges1, ges2, ges3 = get_input_pics(1) 
  if (str(ges1) == 'Palm') and (str(ges2) == 'Scissors') and (str(ges3) == 'Fist'): 
  	setting_gesture1 = ['Palm', 'Scissors', 'Fist'] 
  elif (str(ges1) == 'Palm') and (str(ges2) == 'Fist') and (str(ges3) == 'Scissors'):
  	setting_gesture1 = ['Palm', 'Fist', 'Scissors'] 
  elif (str(ges1) == 'Scissors') and (str(ges2) == 'Palm') and (str(ges3) == 'Fist'):
  	setting_gesture1 = ['Scissors', 'Palm', 'Fist'] 
  elif (str(ges1) == 'Scissors') and (str(ges2) == 'Fist') and (str(ges3) == 'Palm'): 
  	setting_gesture1 = ['Scissors', 'Fist', 'Palm'] 
  elif (str(ges1) == 'Fist') and (str(ges2) == 'Palm') and (str(ges3) == 'Scissors'): 
  	setting_gesture1 = ['Fist', 'Palm', 'Scissors'] 
  elif (str(ges1) == 'Fist') and (str(ges2) == 'Scissors') and (str(ges3) == 'Palm'): 
  	setting_gesture1 = ['Fist', 'Scissors', 'Palm'] 
  else: 
  	print 'The input images for 1st player can not form a right combination of Rock-Paper-Scissors! Please restore his/her images!'	

  ges2_1, ges2_2, ges2_3 = get_input_pics(2) 	
  if (str(ges2_1) == 'Palm') and (str(ges2_2) == 'Scissors') and (str(ges2_3) == 'Fist'): 
  	setting_gesture2 = ['Palm', 'Scissors', 'Fist'] 
  elif (str(ges2_1) == 'Palm') and (str(ges2_2) == 'Fist') and (str(ges2_3) == 'Scissors'):
  	setting_gesture2 = ['Palm', 'Fist', 'Scissors'] 
  elif (str(ges2_1) == 'Scissors') and (str(ges2_2) == 'Palm') and (str(ges2_3) == 'Fist'):
  	setting_gesture2 = ['Scissors', 'Palm', 'Fist'] 
  elif (str(ges2_1) == 'Scissors') and (str(ges2_2) == 'Fist') and (str(ges2_3) == 'Palm'): 
  	setting_gesture2 = ['Scissors', 'Fist', 'Palm'] 
  elif (str(ges2_1) == 'Fist') and (str(ges2_2) == 'Palm') and (str(ges2_3) == 'Scissors'): 
  	setting_gesture2 = ['Fist', 'Palm', 'Scissors'] 
  elif (str(ges2_1) == 'Fist') and (str(ges2_2) == 'Scissors') and (str(ges2_3) == 'Palm'): 
  	setting_gesture2 = ['Fist', 'Scissors', 'Palm'] 
  else: 
  	print 'The input images for 2nd player can not form a right combination of Rock-Paper-Scissors! Please restore his/her images!'

  print ''
  p1 = getpass.getpass("1st Player, please enter your number, 0 - 9: ")
  print ''
  p2 = getpass.getpass("2nd Player, please enter your number, 0 - 9: ")   
  print '' 

  gesture_p1 = Rule_Player1.GSC[int(p1)]
  gesture_p2 = Rule_Player2.GSC[int(p2)]
  
  # print setting_gesture1 
  # print setting_gesture2

  print 'The 1st player throws', setting_gesture1[gesture_p1-1] 
  print 'The 2nd player throws', setting_gesture2[gesture_p2-1] 

  # Pictures Could be show if needed
  if ((setting_gesture1[gesture_p1-1] == 'Palm') and (setting_gesture2[gesture_p2-1] == 'Scissors')): 
  	win = 'The winner is Player2!'
  elif ((setting_gesture1[gesture_p1-1] == 'Palm') and (setting_gesture2[gesture_p2-1] == 'Fist')): 
  	win = 'The winner is player1!'
  elif ((setting_gesture1[gesture_p1-1] == 'Scissors') and (setting_gesture2[gesture_p2-1] == 'Palm')): 
  	win = 'The winner is Player1!'
  elif ((setting_gesture1[gesture_p1-1] == 'Scissors') and (setting_gesture2[gesture_p2-1] == 'Fist')): 
  	win = 'The winner is Player2!'
  elif ((setting_gesture1[gesture_p1-1] == 'Fist') and (setting_gesture2[gesture_p2-1] == 'Palm')): 
  	win = 'The winner is Player2!'
  elif ((setting_gesture1[gesture_p1-1] == 'Fist') and (setting_gesture2[gesture_p2-1] == 'Scissors')):
    win = 'The winner is Player1!'
  elif (setting_gesture1[gesture_p1-1] == setting_gesture2[gesture_p2-1]): 
  	win = 'It is a tie!'

  print win
  print ''


if __name__=='__main__':
  mainFunction()
