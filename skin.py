'''
    Skin Detector Module
'''

import cv
import imgproc
from constants import SkinCons

''' SkinDetector Class and Its Functions, Return Mask'''

class SkinDetector(object):
  def __init__(self):
    self.calibrating = False
    self.storage=cv.CreateMemStorage(0)
    self.v_low = SkinCons.INTENSITY_LT
    self.v_high = SkinCons.INTENSITY_UT
    self.h_low = SkinCons.HUE_LT
    self.h_high = SkinCons.HUE_UT

  def checkRange(self, src, lowBound, highBound):
    size = imgproc.size(src)
    mask = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
    gt_low = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
    cv.CmpS(src, lowBound, gt_low, cv.CV_CMP_GT)
    lt_high = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
    cv.CmpS(src, highBound, lt_high, cv.CV_CMP_LT) 
    # CmpS Performs the per-element comparison of 2 arrays/1 array and scalar value.
    cv.And(gt_low, lt_high, mask)
    return mask

  def toggle_calibrate(self):
    self.calibrating = self.calibrating ^ True

  def segment(self, bgrimg):
    segmented = cv.CreateImage(imgproc.size(bgrimg), bgrimg.depth, bgrimg.nChannels)
    cv.PyrSegmentation(bgrimg, segmented, self.storage, 3, 188, 60)
    return segmented

  def setHueThreshold(self, hueThreshold):
    self.h_low, self.h_high = max(hueThreshold-55,0), min(hueThreshold+55,255)
    # print self.h_low, self.h_high 

  def setIntensityThreshold(self, intensityThreshold):
    self.v_low, self.v_high = max(intensityThreshold-40,0), min(intensityThreshold+40,255)
    # print self.v_low, self.v_high

  def detectSkin(self, bgrimg):
    img_temp = cv.CreateImage(imgproc.size(bgrimg), bgrimg.depth, bgrimg.nChannels)
    #cv.SaveImage("test.png", bgrimg) 
    cv.Smooth(bgrimg, img_temp, cv.CV_MEDIAN, 15)#, 0, 20, 20)
    #cv.SaveImage("smooth.png", img_temp)
    # cv.ShowImage("Obtain From Input", img_temp)
    # cv.WaitKey(0)
    #skin_o = self._detectSkin(bgrimg)
    #cv.SaveImage("skin_o.png", skin_o)
    skin = self._detectSkin(img_temp)
    #cv.SaveImage("skin_s.png", skin)
    return skin

  def _detectSkin(self, bgrimg):
    hsvimg = imgproc.bgr2hsv(bgrimg) # Trasform BGR to HSV
    h,s,v = imgproc.split3(bgrimg)   # Calculate H,S,V 3 Channels 
    skin_mask = cv.CreateImage(imgproc.size(hsvimg), cv.IPL_DEPTH_8U, 1) 
    h_mask = cv.CreateImage(imgproc.size(hsvimg), cv.IPL_DEPTH_8U, 1)
    v_mask = cv.CreateImage(imgproc.size(hsvimg), cv.IPL_DEPTH_8U, 1)

    v_mask = self.checkRange(v, self.v_low, self.v_high)
    h_mask = self.checkRange(h, self.h_low, self.h_high)    
    cv.And(h_mask, v_mask, skin_mask)

    return skin_mask