'''
    Main Function 
'''
import os
import sys
import cv
import numpy
import imgproc, skin, gesture

''' ImageProcessSession Class and Its Functions'''

class ImageProcessSession(object):

  def __init__(self, skin_detector):
    self.skin_detector = skin_detector

  def process(self, bgrimg):
    img = self.skin_detector.detectSkin(bgrimg) # Call the function in skin.py
    contours = imgproc.find_contours(img)
    return contours

''' Functions For Images Input'''

def get_input_pics_filename(): 
    test_fn = int(raw_input("Enter test folder name, from 1 to 10: ")) 
    if (test_fn > 0) and (test_fn < 6): 
      path_1 = 'test_' + str(test_fn) + '/1.png'
      path_2 = 'test_' + str(test_fn) + '/2.png'
      im_1   = cv.LoadImage(path_1)
      im_2   = cv.LoadImage(path_2)
      im_3   = None
      # cv.ShowImage('show1', im_1)
      # cv.ShowImage('show2', im_2)      
      # # cv.ShowImage('show3', im_3)      
      # cv.WaitKey(0)
    elif (test_fn > 5) and (test_fn < 8): 
      path_1 = 'test_' + str(test_fn) + '/1.png'
      path_2 = 'test_' + str(test_fn) + '/2.png'
      path_3 = 'test_' + str(test_fn) + '/3.png'
      im_1   = cv.LoadImage(path_1)
      im_2   = cv.LoadImage(path_2)
      im_3   = cv.LoadImage(path_3)
      # cv.ShowImage('show1', im_1)
      # cv.ShowImage('show2', im_2)      
      # cv.ShowImage('show3', im_3)
      # cv.WaitKey(0)
    elif (test_fn > 7) and (test_fn < 10): 
      path_1 = 'test_' + str(test_fn) + '/1.png'
      path_2 = 'test_' + str(test_fn) + '/2.png'
      im_1   = cv.LoadImage(path_1)
      im_2   = cv.LoadImage(path_2)
      im_3   = None
    elif (test_fn == 10): 
      path_1 = 'test_' + str(test_fn) + '/1.png'
      path_2 = 'test_' + str(test_fn) + '/2.png'
      path_3 = 'test_' + str(test_fn) + '/3.png'
      im_1   = cv.LoadImage(path_1)
      im_2   = cv.LoadImage(path_2)
      im_3   = cv.LoadImage(path_3)        
    else: 
      print 'Invalid input number!!'
      print ''
      im_1 = None
      im_2 = None
      im_3 = None  
    return im_1, im_2, im_3

''' Main Functions in this System '''

def mainFunction():
  im1, im2, im3 = get_input_pics_filename()
  if (im1 is not None) or (im2 is not None) or (im3 is not None): 
    initHueThreshold = 42
    initIntensityThreshold = 170
    skin_detector = skin.SkinDetector()
    skin_detector.setHueThreshold(initHueThreshold)
    skin_detector.setIntensityThreshold(initIntensityThreshold)
    print ''
    print 'Current Hue Threshold: ', initHueThreshold
    print 'Current Intensity Threshold: ', initIntensityThreshold
    print ''

    session = ImageProcessSession(skin_detector)
    ga = gesture.GestureAnalyzer()

    if im1 is not None: 
      print 'Result For 1st Image: '
      cv.Flip(im1, None, 1)
      contours1 = session.process(im1)
      img1 = cv.CreateImage((im1.width, im1.height), 8, 3)
      if contours1:
          ges1, area1, depth1 = ga.recognize(contours1) # main recognize
          print 'Area: ', float(area1) 
          print 'Depth: ', depth1  
          x1, y1, r1, b1, isCenter1 = imgproc.find_max_rectangle(contours1)
          print 'Coordinate (x1, y1, x2, y2): ', x1, y1, r1, b1
          if isCenter1 == 1:
            print 'The gesture is placed at the center!' 
          elif isCenter1 == 0:
            print 'The gesture is placed at the corner!'
          else: 
            print 'The gesture position is not recognized!'
          # cv.Rectangle(img1, (x1,y1), (r1, b1), imgproc.color.RED)
          # cv.DrawContours(img1, contours1, imgproc.color.RED, imgproc.color.GREEN, 1, thickness=3)
          print 'Detected Gesture For 1st Image is: ', ges1
          print ''

    if im2 is not None: 
      print 'Result For 2nd Image: '
      cv.Flip(im2, None, 1)
      contours2 = session.process(im2)
      img2 = cv.CreateImage((im2.width, im2.height), 8, 3)
      if contours2:
          ges2, area2, depth2 = ga.recognize(contours2) # main recognize
          print 'Area: ', float(area2) 
          print 'Depth: ', depth2
          x2, y2, r2, b2, isCenter2 = imgproc.find_max_rectangle(contours2)
          print 'Coordinate (x1, y1, x2, y2): ', x2, y2, r2, b2
          if isCenter2 == 1:
            print 'The gesture is placed at the center!' 
          elif isCenter2 == 0:
            print 'The gesture is placed at the corner!'   
          else: 
            print 'The gesture position is not recognized!'                          
          # cv.Rectangle(img2, (x2,y2), (r2, b2), imgproc.color.RED)
          # cv.DrawContours(img2, contours2, imgproc.color.RED, imgproc.color.GREEN, 1, thickness=3)
          print 'Detected Gesture For 2nd Image is: ', ges2
          print ''

    if im3 is not None: 
      print 'Result For 3rd Image: '
      cv.Flip(im3, None, 1)
      contours3 = session.process(im3)
      img3 = cv.CreateImage((im3.width, im3.height), 8, 3)
      if contours3:
          ges3, area3, depth3 = ga.recognize(contours3) # main recognize
          print 'Area: ', float(area3) 
          print 'Depth: ', depth3
          x3, y3, r3, b3, isCenter3 = imgproc.find_max_rectangle(contours3)
          print 'Coordinate (x1, y1, x2, y2): ', x3, y3, r3, b3
          if isCenter3 == 1:
            print 'The gesture is placed at the center!' 
          elif isCenter3 == 0:
            print 'The gesture is placed at the corner!'
          else: 
            print 'The gesture position is not recognized!'
          # cv.Rectangle(img3, (x3,y3), (r3, b3), imgproc.color.RED)
          # cv.DrawContours(img3, contours3, imgproc.color.RED, imgproc.color.GREEN, 1, thickness=3)
          print 'Detected Gesture For 3rd Image is: ', ges3 
          print ''
    else: 
      ges3 = None      

    ''' AUTHENTICATION PART '''  

    Password = ['Palm', 'Fist']  

    if ((str(ges1) == Password[0]) and (str(ges2) == Password[1])) or (ges3 and (str(ges2) == Password[0]) and (str(ges3) == Password[1])): 
      print 'AUTHENTICATED!'
      print ''
    else: 
      print 'WARNING: NOT AUTHENTICATED!'
      print ''

if __name__=='__main__':
  mainFunction()
